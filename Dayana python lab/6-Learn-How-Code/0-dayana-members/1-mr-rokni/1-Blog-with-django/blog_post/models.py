from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# on_delete= # ;
#   CASECADE) or  SET_NULL, null = True) or PROTECT) or   SET_DEFAULT, default = )


class Article(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category =models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pubdate = models.DateField(default=timezone.now)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ('-updated', '-created' ) # - : from last to first

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog_post:article_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return f"{self.title} - {self.body[ :30]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]


class Massage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="likes", verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -  {self.article.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ("-created_at", )