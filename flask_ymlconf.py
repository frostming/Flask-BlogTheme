"""
    Flask-YmlConf
    ~~~~~~~~~~~~~
    Flask extension to read ``_config.yml`` files like Jekyll

    :author: Frost Ming
    :email: mianghong@gmail.com
    :license: MIT
"""
import yaml
import io
import os.path as op

from flask.config import Config

__version__ = '0.1.1'
__all__ = ['YmlConf']


class YmlConf(object):
    """Main class of Flask-YmlConf

    Provide following config variables:

    YML_CONF_NAME: the file name of the config, defaults to ``_config.yml``
    YML_CONF_PROCESSOR: the context processor for the config, defaults to ``site``
    YML_CONF_BLUEPRINT_PROCESSOR: the context processor for the blueprint config,
        defaults to ``blueprint``
    """
    def __init__(self, app=None, name=None, processor=None,
                 blueprint_processor=None):
        """Create a YmlConf instance

        :param app: the app object
        :param name: give it a value to override ``YML_CONF_NAME``
        :param processor: give it a value to override ``YML_CONF_PROCESSOR``
        :param blueprint_processor: give it a value to override
            ``YML_CONF_BLUEPRINT_PROCESSOR``
        """
        self.name = name
        self.processor = processor
        self.blueprint_processor = processor
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not self.name:
            self.name = app.config.get('YML_CONF_NAME', '_config.yml')
        if not self.processor:
            self.processor = app.config.get('YML_CONF_PROCESSOR', 'site')
        if not self.blueprint_processor:
            self.blueprint_processor = app.config.get('YML_CONF_BLUEPRINT_PROCESSOR',
                                                      'blueprint')

        config = Config(app.root_path, self._get_config(app))
        setattr(app, self.processor, config)

        @app.context_processor
        def app_config():
            return {self.processor: config}

        app.register_blueprint = self._wrapper(app.register_blueprint)

        if not app.extensions:
            app.extensions = {}
        app.extensions['ymlconf'] = self

    def _get_config(self, blueprint):
        filename = self.name
        filepath = op.join(blueprint.root_path, filename)
        rv = None
        if op.isfile(filepath):
            with io.open(filepath, encoding='utf-8') as fp:
                rv = yaml.load(fp)
        return rv

    def _wrapper(self, func):
        def _register(blueprint, **options):
            @blueprint.context_processor
            def _context_processor():
                rv = Config(blueprint.root_path, self._get_config(blueprint))
                return {self.blueprint_processor: rv}

            func(blueprint, **options)
        return _register
