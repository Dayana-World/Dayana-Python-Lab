from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView, CreateView, DetailView

from blog_post.models import Article, Category, Comment, Massage, Like
from .forms import ContactUsForm , MassageForm
from django.urls import reverse_lazy
from .mixins import customLoginRequiredMixin

# Create your view with def & class(class base view)

def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    # Create new comment
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, 'blog_post/article_detail.html', {'article': article})

class ArticleDetailView(DetailView):
    model = Article
    # Liked system
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context

def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1) # Pagination
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog_post/article_list.html', {'articles': objects_list})

def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'blog_post/article_list.html', {'articles': articles})

def search(request): # Search article
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog_post/article_list.html', {'articles': objects_list})


def contactus(request):
    if request.method == 'POST':
        form = MassageForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = MassageForm()
    return render(request, 'blog_post/contact_us.html', {'form': form})


class ArticleListView(customLoginRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 1

class ContactUsView(FormView):
    template_name = 'blog_post/contact_us.html'
    form_class = MassageForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Massage.objects.create(**form_data)
        return super().form_valid(form)


class MaasageView(CreateView):
    model = Massage
    fields =('title', 'text')
    success_url = reverse_lazy('home:home')
    template_name = 'blog_post/contact_us.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)

# Generate AJAX system for like
def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({"response": "unliked"})
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({"response": "liked"})


