Flask-BlogTheme
===============

.. image:: https://travis-ci.org/frostming/Flask-BlogTheme.svg?branch=master
    :target: https://travis-ci.org/frostming/Flask-BlogTheme

*Flask extension to switch blog theme easily*

Features
~~~~~~~~

* Clone theme repository to theme folder and set name in config file
* YAML ``_config.yml`` files like Jekyll
* Easily porting theme from Jekyll or Hexo

Installation
~~~~~~~~~~~~

From PyPI
^^^^^^^^^
::

    $ pip install Flask-BlogTheme

All are ready for you, prefix the command with ``sudo`` if necessary.

From GitHub
^^^^^^^^^^^
::

    $ git clone git@github.com:frostming/Flask-BlogTheme.git
    $ cd Flask-BlogTheme
    $ python setup.py develop

Usage
~~~~~

.. code-block:: python

from Flask-BlogTheme import BlogTheme
from flask import Flask

app = Flask(__name__)
BlogTheme(app)

Create a ``theme`` folder under your app root, clone some theme repository to it. You can pass an extra ``theme_folder`` parameter to ``BlogTheme()`` to change the default folder.

Config the theme just as the guide tells, in ``_config.yml``. The theme repository should obey following restrictions:

* static files under ``assets`` folder
* All layout / templates directly under the theme folder
* Templates are in jinja2-readable format

Set ``app.config['BLOG_THEME_NAME']`` to the theme name. Then, in you ``app.py``:
Then ``{{theme}}`` is accessible throughout your app. You can put some settings in the ``_config.yml`` under app root path to override the theme config.

Config
~~~~~~

======================  ===========================================================
Config                        Description
======================  ===========================================================
BLOG_THEME_NAME         The theme name
BLOG_THEME_PROCESSOR    the context processor for the config, defaults to ``theme``
BLOG_THEME_CONFIG_NAME  the config file name, defaults to ``_config.yml``
======================  ===========================================================

License
~~~~~~~

MIT. See the LICENSE file
