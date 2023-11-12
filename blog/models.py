from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


class Category(models.Model):
    name = models.CharField(max_length=100)
    class CategoryManager(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset()
    def __str__(self):
        return self.name
    objects = models.manager

class Post(models.Model):
    class PostManager(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status="published")

    status_choices = (("published", "Published"), ("draft", "Draft"))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(
        choices=status_choices, max_length=100, default="published"
    )

    objects = models.Manager()
    postobjects = PostManager()

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title
