from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.
class IndexPage(TemplateView):

    def get(self , request , **kwargs):
        article_data=[]
        all_articles=Article.objects.all()[:9]
        for article in all_articles:
            article_data.append({
                'title':article.title,
                'cover':article.cover.url,
                'created':article.created_at.strftime('%B %d, %Y'),
                'category':article.category.title,
            })
        context = {
            'article_data' : article_data,
        }
        return render(request,'index.html',context)
