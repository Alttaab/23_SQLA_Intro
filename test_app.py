from parameterized import parameterized_class
from app import app
from seed import reset_to_seed
from unittest import TestCase


@parameterized_class(
    ('route', 'expected_html_contents'), [
        ('/users', '<h1>Users</h1>'),
        ('/users/new', '<h1>Create a New User</h1>'),
        ('/users/3', '<h1>Winslow Catering</h1>'),
        ('/users/3/edit', '<h1>Edit Winslow Catering</h1>'),
        ('/posts', '<h1>Posts</h1>'),
        ('/users/3/posts/new', '<h1>Create a Post for Winslow Catering</h1>'),
        ('/posts/1/edit', '<h1>Edit My First Post</h1>'),
        ('/tags', '<h1>Tags</h1>'),
        ('/tags/1', '<h1>Posts Tagged with greeting</h1>'),
        ('/tags/new', '<h1>Create a New Tag</h1>'),
        ('/tags/1/edit', "<h1>Edit 'greeting' Tag</h1>"),
        ('/posts/1', '<h1>My First Post</h1>')
    ]
)
class UserViewsTestCase(TestCase):

    def test_user_route_views_parameterized(self):
        with app.test_client() as client:

            response = client.get(self.route)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(self.expected_html_contents, html)


@parameterized_class(
    ('first_name', 'last_name', 'image_url'), [
        ('Samuel', 'Smith', ''),
        ('Bob', 'Dylan', ''),
        ('arstnasrtastshtnsrtahsrtdasnertdhaenrsdt', 'Smith', '')
    ])
class UserFormsTestCase(TestCase):

    @classmethod
    def tearDownClass(cls) -> None:
        reset_to_seed()
        return super().tearDownClass()

    def test_new_user_submit_parameterized(self):
        with app.test_client() as client:

            response = client.post('/users/new', follow_redirects=True,
                                   data={
                                       'first_name': self.first_name,
                                       'last_name': self.last_name,
                                       'image_url': self.image_url})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(self.first_name, html)


@parameterized_class(
    ('user_id', 'user_name', 'post_title', 'post_content', 'edited_title', 'edited_content', 'post_id'), [
        ('1', 'Alexandretta Tau', 'Lorem ipsum',
         'Lorem ipsum dolor sit amet, consectetuer.'),
        ('2', 'Kong Zhu', 'Epsum', 'Epsum factorial non deposit quid pro quo.'),
        ('3', 'Winslow Catering', 'Li Europan',
         'Li Europan lingues es membres del sam.'),
        ('4', 'Elisa Whitoak', 'Ma quande',
         'Ma quande lingues coalesce, li grammatica del.')
    ]
)
class PostTestCase(TestCase):

    @classmethod
    def tearDownClass(cls) -> None:
        reset_to_seed()
        return super().tearDownClass()

    def test_new_post_submit_parameterized(self):
        with app.test_client() as client:

            response = client.post(f'/users/{self.user_id}/posts/new', follow_redirects=True,
                                   data={
                                       'title': self.post_title,
                                       'content': self.post_content})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(self.user_name, html)
            self.assertIn(self.post_title, html)
            self.assertIn(self.post_content, html)

    def test_delete_post_parameterized(self):
        with app.test_client() as client:

            response = client.post(
                f'/posts/{self.user_id}/delete', follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Post', html)
            self.assertIn('removed.', html)

    def test_alter_post_submit_parameterized(self):
        with app.test_client() as client:

            response = client.post(f'/posts/{self.user_id}/edit', follow_redirects=True,
                                   data={
                                       'title': self.post_title,
                                       'content': self.post_content})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(self.post_title, html)
            self.assertIn(self.post_content, html)


@parameterized_class(
    ('tag_name', 'tag_id', 'edited_tag_name'), [
        ('news', '1', 'lorem'),
        ('test tag', '2', 'ipsum'),
        ('this is a very long tag', '3', 'dolor')
    ]
)
class TagTestCase(TestCase):

    @classmethod
    def tearDownClass(cls) -> None:
        reset_to_seed()
        return super().tearDownClass()

    def test1_new_tag_parameterized(self):
        with app.test_client() as client:

            response = client.post('/tags/new', follow_redirects=True,
                                   data={
                                       'name': self.tag_name})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(self.tag_name, html)

    def test2_edit_tag_parameterized(self):
        with app.test_client() as client:

            response = client.post(f'/tags/{self.tag_id}/edit', follow_redirects=True,
                                   data={
                                       'name': self.edited_tag_name})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(self.edited_tag_name, html)

    def test3_delete_tag_parameterized(self):
        with app.test_client() as client:

            response = client.post(
                f'/tags/{self.tag_id}/delete', follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(f"removed.", html)
