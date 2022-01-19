from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
# Create your models here.


class Tag(models.Model):

    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=['name'])

    @property
    def get_tagged_articles(self):
        return Article.objects.filter(tag=self)


class Author(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField()
    profile_image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024,
                                null=True,
                                blank=True,
                                validators=[URLValidator])
    slug = AutoSlugField(populate_from=['name'])


class Article(models.Model):

    title = models.CharField(max_length=250)
    author = models.ManyToManyField('Author', related_name="authors")
    date = models.DateField(auto_now=True)
    body = models.TextField()
    # likes = models.ForeignKey(User,
    #                          on_delete=models.CASCADE,
    #                          related_name='liked_by',
    #                          default=0
    #                         )
    article_image = models.ImageField(null=True, blank=True)
    article_image_url = models.URLField(max_length=1024,
                                        null=True,
                                        blank=True, validators=[URLValidator])
    # slug will be used for article url
    # Consider reoplacing with autoslugfield from django extensions
    slug = AutoSlugField(max_length=50, populate_from=['title', 'id'])
    teaser = models.TextField(max_length=250,
                              blank=True)
    tag = models.ManyToManyField('Tag', related_name="tags")

    def save(self, *args, **kwargs):
        self.teaser = str((str(self.body)[0:250]).rsplit(". ", maxsplit=1)[0])+"..."
        super().save(*args, **kwargs)

    @property
    def comment_count(self):
        return Comment.objects.filter(article=self).count()


class Comment(models.Model):
    """
    TODO: Replace Name field with User - require log in to comment
    """
    article = models.ForeignKey('Article',
                                on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{str(self.user)}, {self.article.title[:20]}'

