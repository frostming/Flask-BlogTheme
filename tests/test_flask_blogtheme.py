import unittest
from flask import Flask, render_template_string, render_template
from flask_blogtheme import BlogTheme


app = Flask(__name__)
app.config['BLOG_THEME_NAME'] = 'mytheme'
conf = BlogTheme(app)


class TestBlogTheme(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_theme_processor(self):
        with app.test_request_context('/'):
            self.assertEqual(render_template_string('{{theme.name|safe}}'),
                             'main')
            self.assertEqual(render_template_string('{{theme.blist|safe}}'),
                             '[3, 4]')

    def test_render_theme(self):
        with app.test_request_context('/'):
            rv = render_template('index.txt')
            self.assertEqual(rv, '/assets/plain.txt')

    def test_static_file(self):
        c = app.test_client()
        r = c.get('/assets/plain.txt')
        self.assertEqual(r.data, b'hello world\n')


if __name__ == '__main__':
    unittest.main()
