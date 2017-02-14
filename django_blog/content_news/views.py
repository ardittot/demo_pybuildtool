""" Views for ContentNews.
"""

from django.shortcuts import render

def list_view(request):
    """ Front page of ContentNews.
    """
    return render(request, context={'message': 'hallo! apa kabar'},
                  template_name='content_news/list_view.html')
