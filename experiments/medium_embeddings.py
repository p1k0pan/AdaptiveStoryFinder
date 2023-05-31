import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
import clean_dataset
import json
import time
import datetime
import os


if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available():
    device = 'mps'
else:
    device = 'cpu'

model = SentenceTransformer('paraphrase-MiniLM-L6-v2', device=device)

def read_history() -> pd.DataFrame:
    with open('/Users/piko/code/AdaptiveStoryFinder/experiments/food_health_data.json') as f:
        data = json.load(f)

    history= []
    for index in data:
        history.append(data[index])
    user_history = pd.DataFrame(history, columns=['sentence'])
    user_history = clean_dataset.clean_sentences(user_history)
    # print(user_history.head())
    return user_history

def read_dataset(path)-> pd.DataFrame:
    df = pd.read_csv(path)
    # Remove null description
    df = df[~df.isna()]
    # Renaming the description column

    df.insert(2,'sentence','')
    for _, row in df.iterrows():
        row['sentence'] = str(row['title'])+": "+str(row['text'])
        # row['sentence'] = row['article_name']+": "+row['article_desc']
    # Sampling the first 5000 rows
    # df = df.iloc[:5000]
    # print(df.head())
    return df

def embed_text(text):
    return model.encode(text, convert_to_tensor=True,show_progress_bar=True)

def getTopResult(embedd1, embedd2, topk, df) -> pd.DataFrame:
    cos_scores = util.pytorch_cos_sim(embedd1, embedd2)[0]

    top_results = torch.topk(cos_scores, k=topk)

    print("\n\n======================\n\n")
    # print("Query:", test_sentence)
    print(f"\nTop {topk} most similar sentences in corpus:")

    # result = top_results.indices.tolist()
    result_index = [] # get the top10 item from df

    for score, idx in zip(top_results[0], top_results[1]):
        score = score.cpu().data.numpy() 
        idx = idx.cpu().data.numpy()
        print(f"{idx}: {df[['title']].iloc[idx]}")
        result_index.append(idx)
        # result.append(df[['clean_sentence']].iloc[idx].item())

    return df.iloc[result_index].copy()

def first_load():
    dataset_path = 'medium_articles.csv'
    print("read and clean data")
    df: pd.DataFrame = read_dataset(dataset_path)
    df = clean_dataset.clean_sentences(df)
    df.to_csv('cleaned_meidium_articles.csv',',')

    print("start embedding corpus")
    corpus_embeddings = embed_text(df.clean_sentence.values)
    print("end embedding corpus")
    torch.save(corpus_embeddings, 'corpus_embeddings.pt')
    print("saved")

if __name__ == "__main__":
    # user_history: pd.DataFrame = read_history()
    # first_load
    start_time = time.perf_counter()
    first_load()
    end_time = time.perf_counter()
    elapsed_time_readable = str(datetime.timedelta(seconds=end_time - start_time))
    print(elapsed_time_readable)

    # test_sentence = "start my own restaurant"
    # query_embedding = embed_text(test_sentence)

    # # get result from corpus and query, then embedd the result 
    # query_corpus_result:pd.DataFrame = getTopResult(query_embedding, corpus_embeddings, 10, df)
    # query_corpus_result_embedding = embed_text(query_corpus_result.clean_sentence.values)

    # # user history embedding
    # user_keyword_embeddings = embed_text(user_history.clean_sentence.values)

    # top3 = getTopResult(user_keyword_embeddings, query_corpus_result_embedding, 3, query_corpus_result)
