from django.test import TransactionTestCase
from django.contrib.auth.models import User
from ..models import Author, Article, Comment, Likes, Tag
from ..forms import CommentForm
from django.test import Client

# Create your tests here.


class TestArticles(TransactionTestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        login = self.client.login(username='testuser',
                                  password='123435')

        self.user2 = User.objects.create_user(username='testuser2',
                                              password='12345')

        login2 = self.client.login(username='testuser2',
                                   password='12345')

        test_tag = Tag(name='test tag')
        test_tag.save()
        test_Author = Author(
                             name='test auth',
                             email='auth@testmail.com',
                             image_url=""
                             )
        test_Author.save()
        test_Article = Article(
                               title="test title",
                               body="This is a test"
                               )
        test_Article.save()
        test_Article.tag.add(test_tag)
        test_Article.author.add(test_Author)
        test_Article_2 = Article(
                                 title="test title 2",
                                 body='This is also a test'
                                 )
        test_Article_2.save()
        test_Article_2.tag.add(test_tag)
        test_Article_2.author.add(test_Author)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def testTag(self):

        _tag = Tag.objects.filter(name__iexact='test tag')
        self.assertTrue(len(_tag) == 1)

        self.assertIsNotNone(_tag[0].slug)

    def testAuthor(self):

        test_Auth = Author.objects.filter(name__iexact='test auth')
        self.assertTrue(len(test_Auth) == 1)

        self.assertIsNotNone(test_Auth[0].slug)

        test_name = 'test auth'

        self.assertTrue(test_Auth[0].__str__() == test_name,
                        'Error: .__str__ did not return expected value')

    def testArticle(self):

        test_Art = Article.objects.filter(title__iexact="test title")
        self.assertTrue(len(test_Art) == 1)

        self.assertIsNotNone(test_Art[0])

        self.assertIsNotNone(test_Art[0].teaser)
        self.assertIsNotNone(test_Art[0].id)
        self.assertIsNotNone(test_Art[0].slug)
        self.assertIsNotNone(test_Art[0])

        self.assertIsInstance(test_Art[0].tag.all()[0], Tag)
        self.assertIsInstance(test_Art[0].author.all()[0], Author)

    def testComment(self):
        test_Art = Article.objects.filter(title__iexact="test title")[0]

        self.assertEqual(test_Art.comment_count, 0)

        test_CommentForm = CommentForm({'article': test_Art,
                                        'body': 'This is a test comment',
                                        'user': self.user})

        self.assertTrue(test_CommentForm.is_valid())
        comment = test_CommentForm.save()

        test_Art_comment = Comment.objects.filter(article=test_Art)[0]

        self.assertEqual(test_Art.comment_count, 1, f'Error: comment_count returns: {test_Art.comment_count}. Expected: 1')

        self.assertEqual(test_Art_comment.body,
                         'This is a test comment',
                         'Error: test_Art.comment.body returned: {test_Art.comment.body}')

        self.assertEqual(comment.article.id,
                         test_Art.id,
                         f'Error: Comment.article.id: {comment.article.id}, article.id: {test_Art.id}. Expected: Values are equal')

    def testCommentChild(self):

        test_Art = Article.objects.filter(title__iexact="test title")[0]

        self.assertEqual(test_Art.comment_count, 0)

        test_CommentForm = CommentForm({'article': test_Art,
                                        'body': 'This is a test comment',
                                        'user': self.user})

        self.assertTrue(test_CommentForm.is_valid())

        parent_comment = test_CommentForm.save()

        self.assertEqual(test_Art.comment_count, 1)
        
        self.assertIsNotNone(parent_comment.id)
        self.assertEqual(parent_comment.article.id,
                         test_Art.id,
                         f'Error: Comment.article.id: {parent_comment.article.id}, article.id: {test_Art.id}. Expected: Values are equal')
        test_ChildComment = CommentForm(
                                        {
                                            'article': test_Art,
                                            'body': 'This is a child comment',
                                            'user': self.user2,
                                            'parent': parent_comment
                                        }
                                        )
        self.assertTrue(test_ChildComment.is_valid())
        child_comment = test_ChildComment.save()

        self.assertEqual(test_Art.comment_count, 2)
        self.assertEqual(parent_comment.id, int(child_comment.get_parent))

        self.assertEqual(child_comment.comment_body, 'This is a child comment')

    def testLikes(self):

        test_Art = Article.objects.filter(title__exact="test title")[0]
        test_Art_2 = Article.objects.filter(title__exact="test title 2")[0]

        self.assertEqual(test_Art.likes_count, 0)
        self.assertEqual(test_Art_2.likes_count, 0)

        like_1 = Likes(article=test_Art, user=self.user).save()
        self.assertEqual(test_Art.likes_count, 1)

        like_2 = Likes(article=test_Art, user=self.user2).save()

        self.assertEqual(test_Art.likes_count, 2)

        self.assertEqual(test_Art_2.likes_count, 0)

