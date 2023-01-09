from django.urls import path
from . import views

app_name = 'blog_post'
urlpatterns = [
    path('detail/<str:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('list', views.ArticleListView.as_view(), name='articles_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search_articles'),
    path('contactus/', views.MaasageView.as_view(), name='contact_us'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like')
]