import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
import clean_dataset
import json
import time
import datetime
import argparse
from gradio_client import Client

# Create the argument parser
parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('--clean_corpus', action='store_true', help='Flag to generate dataset')
parser.add_argument('--gen_corpus_tensor', action='store_true', help='Flag to generate corpus tensor')

# Parse the arguments
args = parser.parse_args()


if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available():
    device = 'mps'
else:
    device = 'cpu'

model = SentenceTransformer('paraphrase-MiniLM-L6-v2', device=device)

def read_history() -> pd.DataFrame:
    with open('food_health_data.json') as f:
        data = json.load(f)

    history= []
    for index in data:
        history.append(data[index])
    user_history = pd.DataFrame(history, columns=['sentence'])
    user_history = clean_dataset.clean_sentences(user_history)
    # print(user_history.head())
    return user_history

def embed_text(text):
    return model.encode(text, convert_to_tensor=True,show_progress_bar=True)

def getTopResult(embedd1, embedd2, topk, df) -> pd.DataFrame:
    cos_scores = util.pytorch_cos_sim(embedd1, embedd2)[0]
    print(f"cos: {cos_scores}")

    top_results = torch.topk(cos_scores, k=topk)

    print("\n\n======================\n\n")
    print(f"Top {topk} most similar sentences in corpus:")

    # result = top_results.indices.tolist()
    result_index = [] # get the top10 item from df

    for score, idx in zip(top_results[0], top_results[1]):
        score = score.cpu().data.numpy() 
        idx = idx.cpu().data.numpy()
        print(f"{idx}: {df[['title']].iloc[idx].values}")
        result_index.append(idx)
        # result.append(df[['clean_sentence']].iloc[idx].item())

    return df.iloc[result_index].copy()

def load_corpus():
    if args.clean_corpus:
        dataset_path = 'medium_articles.csv'
        print("clean corpus dataset")
        df = pd.read_csv(dataset_path)
        df['sentence'] = df['title'] + ': ' + df['text']
        df['sentence'] = df['sentence'].astype(str)
        df = clean_dataset.clean_sentences(df)
        df.to_csv('cleaned_medium_articles.csv',',')
    else:
        dataset_path = 'cleaned_medium_articles.csv'
        print("load corpus dataset")
        df = pd.read_csv(dataset_path)
    return df

def load_corpus_tensor(df:pd.DataFrame):
    if args.gen_corpus_tensor:
        print("start embedding corpus")
        corpus_embeddings = embed_text(df.clean_sentence.values)
        print("end embedding corpus")
        torch.save(corpus_embeddings, 'corpus_embeddings.pt')
        print("saved")
    else:
        print("load corpus embedding")
        corpus_embeddings = torch.load('corpus_embeddings.pt').to(device)

    return corpus_embeddings

def model_from_HF(df:pd.DataFrame, query)->pd.DataFrame:
    """
        use uploaded api to get model
    """

    print(query)
    client = Client("https://adaptivestoryfinder-medium-query-topk.hf.space/")
    result = client.predict(
                    "10",	# str  in 'topk' Textbox component
                    query,
                    api_name="/predict"
    )
    result = list(map(int, result))
    top10_df = df.iloc[result].copy()
    return top10_df

def model_from_local(df:pd.DataFrame, query)->pd.DataFrame:
    corpus_embeddings = load_corpus_tensor(df)

    print(query)
    query_embedding = embed_text(query)

    query_corpus_result:pd.DataFrame = getTopResult(query_embedding, corpus_embeddings, 10, df)
    return query_corpus_result


if __name__ == "__main__":

    query:str = "start my own restaurant",	# str  in 'query' Textbox component
    df = load_corpus()

    # query_corpus_result = model_from_HF(df, query)
    query_corpus_result = model_from_local(df, query)

    query_corpus_result_embedding = embed_text(query_corpus_result.clean_sentence.values)

    # # user history embedding
    user_history = read_history()
    user_keyword_embeddings = embed_text(user_history.clean_sentence.values)

    top3 = getTopResult(user_keyword_embeddings, query_corpus_result_embedding, 10, query_corpus_result)
