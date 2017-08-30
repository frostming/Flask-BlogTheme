Flask-YmlConf
=============

.. image:: https://travis-ci.org/frostming/Flask-YmlConf.svg?branch=master
    :target: https://travis-ci.org/frostming/Flask-YmlConf

*Flask extension to read _config.yml files like Jekyll*

When we are using static blogging framework such as Jekyll and Hexo, we benefit from brief syntax and elegant looking of YAML config files.

Installation
~~~~~~~~~~~~

From PyPI
^^^^^^^^^
::

    $ pip install Flask-YmlConf

All are ready for you, prefix the command with ``sudo`` if necessary.

From GitHub
^^^^^^^^^^^
::

    $ git clone git@github.com:frostming/Flask-YmlConf.git
    $ cd Flask-YmlConf
    $ python setup.py develop

Usage
~~~~~
Put a ``_config.yml`` under main app directory as well as blueprint root, like below::

    myproject
     ├─blueprint
     │    ├─__init__.py
     │    └─_config.yml
     ├─app.py
     └─_config.yml

Then, in you ``app.py``::

    from flask-ymlconf import YmlConf
    from flask import Flask
    from blueprints import sub

    app = Flask(__name__)
    conf = YmlConf(app)
    # Alternatively, you can instantiate with YmlConf() and call conf.init_app() later in your app factory function.

    # Register any blueprint after Flask-YmlConf is initialized
    app.register_blueprint(sub, url_prefix='/sub/')

An extra attribute ``app.site`` is available for the app config. The name is taken from Jekyll config conventions, you can change it by ``app.config['YML_CONF_NAME']``.

``{{site}}`` is also added as app context processor and is accessible in templates., ``{{blueprint}}`` is added as context processor for each blueprint. The processor names are also customizable.

Config
~~~~~~

============================  =========================================================================
Config                        Description
============================  =========================================================================
YML_CONF_NAME                 the file name of the config, defaults to ``_config.yml``
YML_CONF_PROCESSOR            the context processor for the config, defaults to ``site``
YML_CONF_BLUEPRINT_PROCESSOR  the context processor for the blueprint config, defaults to ``blueprint``
============================  =========================================================================

In addition, you can pass ``name``, ``processor``, ``blueprint_processor`` to ``YmlConf()`` to override corresponding config values.

License
~~~~~~~

MIT. See the LICENSE file