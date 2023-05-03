from curses.ascii import HT
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from wikihow_app.models import Person
import wikihowapi_pk as wha



# Create your views here.

def firstTest(request):
    return HttpResponse("docker is now working")
    
class PersonList(ListView):
    model = Person
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update( {'lst': [11.23, 2.4532, 3.45223, 4.2123313]})
        # print(context)
        """{'paginator': None, 'page_obj': None, 'is_paginated': False, 'object_list': <QuerySet [<Person: Person object (0)>]>, 
        'person_list': <QuerySet [<Person: Person object (0)>]>, 
        'view': <personal_info.views.PersonList object at 0x104605580>, 
        'lst': [11.23, 2.4532, 3.45223, 4.2123313]}"""
        return context

def method_get(self):
    """Method to return a dictionary of Method data members.

    Returns:
        dict: A dictionary of Method data members
    """
    step_list= []
    for step in self.steps:
        step_list.append(step.get())
    return {
        'method_number': self.number,
        'title': self.title,
        # 'steps': self.steps
        'steps': step_list
    }

def searchWikihow(request):
    wha.Methods.get= method_get
    max_results = 1 
    """ provide more choices, choose the one that corresponse to the user's preferences
    may be select the highest rate or with professioncy """
    # how_tos = wha.search_wikihow("how to cook spaghetti", max_results)
    # article = how_tos[0] # assume this is the one we want to present to the user
    # article = wha.Article('https://www.wikihow.com/Train-a-Dog')
    article = wha.Article('https://www.wikihow.com/Cook-Pasta')

    # parse methods
    # methods_list = []
    # for method in article.methods:
    #     methods_list.append(method.get())
        
    # article_json = {
    #     "url": article.url,                         # URL of the article
    #     "title": article.title,                     # Title of the article
    #     "intro": article.intro,                     # Introduction of the article
    #     "n_methods": article.n_methods,             # Number of methods in the article
    #     "methods": methods_list,                 # List of methods in the article
    #     "num_votes": article.num_votes,             # Number of votes given to the article
    #     "percent_helpful": article.percent_helpful, # Percentage of helpful votes given to the article
    #     "is_expert": article.is_expert,             # True if the article is written by an expert, False otherwise
    #     "last_updated": str(article.last_updated),  # Date when the article was last updated
    #     "views": article.views,                     # Number of views received by the article
    #     "co_authors": article.co_authors,           # Number of co-authors of the article
    #     "references": article.references,           # Number of references in the article
    #     "summary": article.summary,                 # Summary of the article
    #     "warnings": article.warnings,               # List of warnings associated with the article
    #     "tips": article.tips                        # List of tips associated with the article
    # }
    
    return JsonResponse(article.get())


