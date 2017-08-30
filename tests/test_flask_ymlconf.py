import unittest
from flask import Flask, render_template_string
from flask_ymlconf import YmlConf
from blueprint import sub


app = Flask(__name__)
conf = YmlConf(app)
app.register_blueprint(sub, url_prefix='/sub')


class TestFlaskYmlConf(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_app_config(self):
        self.assertEqual(app.site, {'name': 'main', 'alist': [1, 2],
                                    'anested': {'A': 'a', 'B': 'b'}})

    def test_app_processor(self):
        with app.test_request_context('/sub/'):
            rv = render_template_string('{{site|safe}}')
        self.assert_(rv)

    def test_blueprint_processor(self):
        with app.test_request_context('/sub/'):
            rv = render_template_string('{{blueprint|safe}}')
        self.assert_(rv)

    def test_blueprint_processor_outof_blueprint(self):
        with app.test_request_context('/other'):
            rv = render_template_string('{{blueprint|safe}}')
        self.assertEqual(rv, '')


if __name__ == '__main__':
    unittest.main()
