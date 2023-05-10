from curses.ascii import HT # not supported for windows: pip install windows-curses
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from wikihow_app.models import Person
import wikihowapi_pk as wha

from django.contrib.auth.decorators import login_required

#from rest_framework import viewsets
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated


#from .models import Article
#from .serializers import ArticleSerializer


#class ArticleViewSet(viewsets.ModelViewSet):
#    authentication_classes = (BasicAuthentication,)
#    permission_classes = (IsAuthenticated,)
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer






# Create your views here.


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

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
    # example test/search?query=how_to_cook_chicken
    query:str = request.GET.get('query')
    wha.Methods.get= method_get
    # max_results = 10 
    """ provide more choices, choose the one that corresponse to the user's preferences
    may be select the highest rate or with professioncy """
    # how_tos: list = wha.search_wikihow_link("housing bubble")
    query = query.replace("_", " ")
    how_tos: list = wha.search_wikihow_link(query)

    print(query)
    # article = how_tos[0] # assume this is the one we want to present to the user
    # article = wha.Article('https://www.wikihow.com/Train-a-Dog')
    # article = wha.Article('https://www.wikihow.com/Cook-Pasta')
    # article = wha.Article("https://www.wikihow.com/Cook-Chicken")

    # return JsonResponse(article.get())
    # print(how_tos)
    return JsonResponse({"results": how_tos})


# use wha to search with different questions and return json response

    
