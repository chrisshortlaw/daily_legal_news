from django.shortcuts import render
from django.http import HttpResponse
from article_page.models import Author, Article, Comment
from products.models import Category, Product
# Create your views here.


def index(request):

    front_page_articles = Article.objects.all()

    head_articles = Article.objects.order_by('date')[:4]
    art_authors = [article.author.all() for article in front_page_articles]
    head_liner = head_articles[0]
    head_liner_author = head_liner.author.all()
    head_liner_article = {
                          "head_liner": head_liner,
                          "head_liner_title": head_liner.title,
                          "head_liner_id": head_liner.id,
                          "head_liner_author_name": head_liner_author[0].name,
                          "head_liner_author_id": head_liner_author[0].id,
                          "head_liner_author_slug": head_liner_author[0].slug,
                          "head_liner_image_url": head_liner.article_image_url,
                          "head_liner_comment_count": head_liner.comment_count,
                          "date": head_liner.date
                          }

    top_articles = []
    for article in head_articles[1:]:
        top_art_dict = {}
        top_art_dict["title"] = article.title
        top_art_dict["id"] = article.id
        top_art_dict["top_art_date"] = article.date
        top_art_dict['comment_count'] = article.comment_count
        art_author = article.author.all()
        top_art_dict["author"] = []
        for author in art_author:
            author_dict = {}
            author_dict["id"] = author.id
            author_dict["name"] = author.name
            author_dict["author_slug"] = author.slug
            top_art_dict["author"].append(author_dict)
        top_articles.append(top_art_dict)

    block_articles = []
    for article in front_page_articles[1:]:
        block_art_dict = {}
        block_art_dict["title"] = article.title
        block_art_dict["id"] = article.id
        block_art_dict["top_art_date"] = article.date
        block_art_dict['comment_count'] = article.comment_count
        block_art_dict['image_url'] = article.article_image_url
        block_art_dict['teaser'] = article.teaser
        art_author = article.author.all()
        block_art_dict["author"] = []
        for author in art_author:
            author_dict = {}
            author_dict["id"] = author.id
            author_dict["name"] = author.name
            author_dict["author_slug"] = author.slug
            block_art_dict["author"].append(author_dict)
        block_articles.append(block_art_dict)

    context = {
            "head_liner_article": head_liner_article,
            "top_articles": top_articles,
            "Articles": front_page_articles,
            "Authors": art_authors,
            "block_articles": block_articles
            }

    return render(request=request,
                  template_name='home_page/index.htmldjango',
                  context=context)

def headline(request):

    front_page_articles = Article.objects.all()

    head_articles = Article.objects.order_by('date')[:5]
    art_authors = [article.author.all() for article in front_page_articles]
    head_liner = head_articles[0]
    head_liner_author = head_liner.author.all()
    head_liner_article = {"head_liner": head_liner,
                          "head_liner_title": head_liner.title,
                          "head_liner_id": head_liner.id,
                          "head_liner_author_name": head_liner_author[0].name,
                          "head_liner_author_id": head_liner_author[0].id,
                          "head_liner_author_slug": head_liner_author[0].slug,
                          "head_liner_image_url": head_liner.article_image_url,
                          "head_liner_comment_count": head_liner.comment_count}

    top_articles = []
    for article in head_articles[1:]:
        top_art_dict = {}
        top_art_dict["title"] = article.title
        top_art_dict["id"] = article.id
        top_art_dict["top_art_date"] = article.date
        top_art_dict['comment_count'] = article.comment_count
        art_author = article.author.all()
        top_art_dict["author"] = []
        for author in art_author:
            author_dict = {}
            author_dict["id"] = author.id
            author_dict["name"] = author.name
            top_art_dict["author"].append(author_dict)
        top_articles.append(top_art_dict)

    context = {
            "head_liner_article": head_liner_article,
            "top_articles": top_articles,
            "Articles": front_page_articles,
            "Authors": art_authors,
            }

    return render(request=request,
                  template_name='home_page/alt_index.htmldjango',
                  context=context)

