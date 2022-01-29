from django.urls import path

from . import views

urlpatterns = [
        path('', views.all_articles, name='articles'),
        path('<int:article_id>',
             views.article_page,
             name='article_page'),
        path('section/<tag_name>',
             views.article_section,
             name='section')
        ]
