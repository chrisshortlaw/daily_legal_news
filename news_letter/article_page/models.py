from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
# Create your models here.


class Tag(models.Model):
    '''
    Creates Tag which can be attached to articles
    Fields:
    - name: charfield, max_length of 50
    - slug: created automatically.
    '''
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=['name'])

    @property
    def get_tagged_articles(self):
        return Article.objects.filter(tag=self)

    def __str__(self):
        # string method allows for friendlier display on admin page
        return f'{self.name}'


class Author(models.Model):
    '''
    Creates an Author instance for Articles
    Fields:
    - name: charfield (req'd)
    - email: EmailField (req'd)
    - profile_image: ImageField(blank=True, null=True)
    - image_url: URLField()
    - slug: Auto-generated
    '''
    name = models.CharField(max_length=250)
    email = models.EmailField()
    profile_image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024,
                                null=True,
                                blank=True,
                                validators=[URLValidator])
    slug = AutoSlugField(populate_from=['name'])

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    '''
    Class holds the Articles which will be uploaded to the site
    Fields:
    - title: max_length = 250
    - author: ManytoManyField. Instance of Author
    - date: auto-generated
    - body: Text Field;
    - article_image: ImageField
    - article_image_url
    - slug: auto-generated
    - teaser: created on save
    - tag: ManytoManyField. Instances of Tag. 
    '''
    title = models.CharField(max_length=250)
    author = models.ManyToManyField('Author',
                                    related_name="authors")
    date = models.DateField(auto_now=True)
    body = models.TextField()
    # likes = models.ForeignKey('Likes',
    #                          on_delete=models.CASCADE,
    #                          related_name='liked_by',
    #                          default=0
    #                        )
    article_image = models.ImageField(null=True,
                                      blank=True)
    article_image_url = models.URLField(max_length=1024,
                                        null=True,
                                        blank=True,
                                        validators=[URLValidator])
    # slug will be used for article url
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

    @property
    def likes_count(self):
        return Likes.objects.filter(article=self).count()

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    """
    Holds comments which are made by users and attached to articles.
    Fields:
        - article: Type[Article]
        - User: Type[User]
        - body: TextField, limit of 300
        - date: DateField - auto-generated
        - parent: Type[Comment] - a parent comment of this comment (optional)
        - approved: Boolean - whether comment is approved or not
    """
    article = models.ForeignKey('Article',
                                on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Comment',
                               on_delete=models.CASCADE,
                               related_name="replies",
                               null=True,
                               blank=True,
                               default=None)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{str(self.user)}, {self.article.title[:20]}'

    @property
    def comment_body(self):
        return f'{self.body}'

    @property
    def get_parent(self):
        if self.parent:
            return f'{self.parent.id}'
        else:
            return f'{self.article.id}'


class Likes(models.Model):
    '''
    Contains likes which users can add to articles
    Fields:
        - article: Type[Article] - foreign key
        - user: Type[User]
    '''
    article = models.ForeignKey('Article',
                                on_delete=models.CASCADE,
                                related_name='liked_article')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="liked_by")
