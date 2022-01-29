from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article, Author, Comment, Tag
from .forms import CommentForm
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.conf import settings
# Create your views here.


def all_articles(request):

    author = None
    all_articles = []
    articles_by_author = []
    context = {}

    if request.GET:
        if 'author' in request.GET:
            author = request.GET['author']
            articles = Article.objects.filter(author__slug=author)
            author = Author.objects.get(slug=author)
            for article in articles:
                article_dictionary = {}
                article_dictionary['title'] = article.title
                article_dictionary['authors'] = article.author.all()
                article_dictionary['image_url'] = article.article_image_url
                article_dictionary['id'] = article.id
                article_dictionary['tags'] = article.tag.all()
                article_dictionary['comment_count'] = article.comment_count
                article_dictionary['likes_count'] = article.likes_count
                article_dictionary['comments'] = Comment.objects.filter(article=article)
                articles_by_author.append(article_dictionary)

            context = {
                "page_title": f'Articles by {author.name}',
                "articles": articles_by_author,
                "current_author": author,
                "articles_by_author": articles_by_author
                }
    else:
        articles = Article.objects.all()
        for article in articles:
            article_dictionary = {}
            article_dictionary['title'] = article.title
            article_dictionary['authors'] = article.author.all()
            article_dictionary['image_url'] = article.article_image_url
            article_dictionary['id'] = article.id
            article_dictionary['tags'] = article.tag.all()
            article_dictionary['comment_count'] = article.comment_count
            article_dictionary['likes_count'] = article.likes_count
            article_dictionary['comments'] = Comment.objects.filter(article=article)
            all_articles.append(article_dictionary)

            context = {
                    "page_title": 'All Articles',
                    "articles": all_articles,
                    "current_author": author,
                    "articles_by_author": articles_by_author
                    }
    return render(request,
                  'articles/articles.htmldjango',
                  context=context)


def article_page(request, article_id):

    # Retrieve Article object by id
    article = Article.objects.get(id=int(article_id))
    tags = article.tag.all()
    # Retrieve authors from many-to-many table
    art_authors = article.author.all()
    comments = Comment.objects.filter(article=article)

    user = request.session.get('user', {})

    if request.POST:
        form = CommentForm(
                           {
                            'article': article,
                            'body': request.post['body'],
                            'user': user,
                           }
                            )
        if form.is_valid():
            comment = form.save()
            messages.info(request, 'Your comment has been posted and is awaiting moderation')
            return redirect(reverse('article_page'))
        else:
            messages.error(request, 'Sorry. Your comment could not be posted.')
    else:
        if article.is_restricted:
            if request.user.is_authenticated:
                if request.user.groups.filter(name='Subscriber'):
                    comment_form = CommentForm()
                    context = {"article": article,
                               "authors": art_authors,
                               "tags": tags,
                               "comment_count": article.comment_count,
                               "likes": article.likes_count,
                               "comments": comments,
                               "comment_form": comment_form
                               }
                    return render(request,
                                  'articles/article_page.htmldjango',
                                  context=context)
                else:
                    context = {
                            "article_teaser": article.teaser,
                            "article_title": article.title,
                            "authors": art_authors,
                            "article_date": article.date,
                            "tags": tags,
                            "comment_count": article.comment_count
                            }
                    return render(request,
                                  'articles/paywall.htmldjango',
                                  context=context)
            else:
                messages.info(request, 'You must be logged in to view this page')
                return redirect(f'{settings.LOGIN_URL}?next={request.path}')
        else:
            comment_form = CommentForm()
            context = {"article": article,
                       "authors": art_authors,
                       "tags": tags,
                       "comment_count": article.comment_count,
                       "likes": article.likes_count,
                       "comments": comments,
                       "comment_form": comment_form
                       }
            return render(request,
                          'articles/article_page.htmldjango',
                          context=context)




def article_section(request, tag_name):
    article_section = []

    articles = Article.objects.filter(tag__slug=tag_name)
    tag_name = Tag.objects.get(slug__exact=tag_name)

    for article in articles:
        article_dictionary = {}
        article_dictionary['title'] = article.title
        article_dictionary['authors'] = article.author.all()
        article_dictionary['image_url'] = article.article_image_url
        article_dictionary['id'] = article.id
        article_dictionary['tags'] = article.tag.all()
        article_dictionary['comment_count'] = article.comment_count
        article_dictionary['likes_count'] = article.likes_count
        article_dictionary['comments'] = Comment.objects.filter(article=article)
        article_section.append(article_dictionary)

    context = {
               "page_title": f'{tag_name.name}',
               "articles": article_section,
                }

    return render(request, 'articles/articles.htmldjango', context=context)




