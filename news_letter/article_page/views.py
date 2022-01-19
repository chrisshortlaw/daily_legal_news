from django.shortcuts import render
from .models import Article, Author, Comment 
# Create your views here.


def all_articles(request):

    articles = Article.objects.all()
    author = None
    all_articles = []
    articles_by_author = []

    if request.GET:
        if 'author' in request.GET:
            print("AUTHOR REQUEST MADE")
            author = request.GET['author']
            articles = Article.objects.filter(author__slug=author)
            authors = Author.objects.filter(slug__in=author)
            for article in articles:
                article_dictionary = {}
                article_dictionary['title'] = article.title
                article_dictionary['authors'] = article.author.all()
                article_dictionary['image_url'] = article.article_image_url
                article_dictionary['id'] = article.id
                articles_by_author.append(article_dictionary)

        print('Moving to base GET')

    for article in articles:
        article_dictionary = {}
        article_dictionary['title'] = article.title
        article_dictionary['authors'] = article.author.all()
        article_dictionary['image_url'] = article.article_image_url
        article_dictionary['id'] = article.id
        all_articles.append(article_dictionary)

    context = {
            "articles": all_articles,
            "current_author": author,
            "articles_by_author": articles_by_author
            }
    print(context)
    return render(request,
                  'articles/articles.htmldjango',
                  context=context)


def article_page(request, article_id):

    # Retrieve Article object by id
    article = Article.objects.get(id=int(article_id))
    # Retrieve authors from many-to-many table
    art_authors = article.author.all()
    context = {"Article": article, "Authors": art_authors}
    return render(request,
                  'articles/article_page.htmldjango',
                  context=context)
