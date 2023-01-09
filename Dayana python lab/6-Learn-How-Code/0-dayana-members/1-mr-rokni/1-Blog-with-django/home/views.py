from django.shortcuts import render
from blog_post.models import Article
# Create your views here.
def home (request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    return render(request, "home/index.html", {'articles': articles})