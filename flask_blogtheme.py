"""
    Flask-BlogTheme
    ~~~~~~~~~~~~~~~
    Flask extension to switch blog theme easily

    :author: Frost Ming
    :email: mianghong@gmail.com
    :license: MIT
"""
import yaml
import io
import os.path as op

from flask import Blueprint

__version__ = '0.2.1'
__all__ = ['BlogTheme']


class BlogTheme(object):
    """Main class of Flask-YmlConf"""
    def __init__(self, app=None, processor=None, config_name=None,
                 theme_folder='theme'):
        """Create a YmlConf instance

        :param app: the app object
        :param processor: give it a value to override ``BLOG_THEME_PROCESSOR``
        :param config_name: give it a value to override ``BLOG_THEME_CONFIG_NAME``
        :param theme_folder: the folder path to store themes
        """
        self.config_name = config_name
        self.processor = processor
        self.theme_folder = theme_folder
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not self.config_name:
            self.config_name = app.config.get('BLOG_THEME_CONFIG_NAME',
                                              '_config.yml')
        if not self.processor:
            self.processor = app.config.get('BLOG_THEME_PROCESSOR', 'theme')

        template_folder = app.config['BLOG_THEME_NAME']
        static_folder = op.join(template_folder, 'assets')
        # Create a blueprint to handle themes
        theme = Blueprint('theme', __name__,
                          template_folder=template_folder,
                          static_folder=static_folder,
                          root_path=op.join(app.root_path, self.theme_folder))
        app_config = self._get_config(app.root_path)
        theme_config = self._get_config(op.join(theme.root_path,
                                                theme.template_folder))
        # Override settings in config
        theme_config.update(app_config)

        @theme.app_context_processor
        def _get_theme_config():
            return {self.processor: theme_config}

        app.register_blueprint(theme)
        if not app.extensions:
            app.extensions = {}
        app.extensions['blogtheme'] = self
        self.app = app

    def _get_config(self, root_path):
        filename = self.config_name
        filepath = op.join(root_path, filename)
        rv = {}
        if op.isfile(filepath):
            with io.open(filepath, encoding='utf-8') as fp:
                rv = yaml.load(fp)
        return rv
