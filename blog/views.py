from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.
class IndexPage(TemplateView):

    def get(self , request , **kwargs):
        article_data=[]
        all_articles=Article.objects.all().order_by('-created_at')[:9]
        for article in all_articles:
            article_data.append({
                'title':article.title,
                'cover':article.cover.url,
                'created':article.created_at.strftime('%B %d, %Y'),
                'category':article.category.title,
            })
        promote_data=[]
        all_promote_article= Article.objects.filter(promote=True)
        for promote_article in all_promote_article:
            promote_data.append({
                'category':promote_article.category.title,
                'title':promote_article.title,
                'cover':promote_article.cover.url,
                'author':promote_article.author.user.first_name,
                'avatar':promote_article.author.avatar.url if promote_article.author.avatar else None,
                'created_at':promote_article.created_at.strftime('%B %d, %Y'),
            })





        context = {
            'article_data' : article_data,
            'promote_article_data' : promote_data,
        }
        return render(request,'index.html',context)
