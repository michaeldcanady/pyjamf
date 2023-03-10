# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pyjamf'
copyright = '2023, dmcanady'
author = 'dmcanady'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'autoapi.extension',
    'sphinx.ext.napoleon',
    'sphinxcontrib.confluencebuilder',
    'sphinx_autodoc_typehints',
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoapi_type = 'python'

autoapi_dirs = ['../pyjamf']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Confluence settings
# https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/configuration/
confluence_page_generation_notice = True
confluence_space_key = 'IEDM'
confluence_parent_page = 'PyJAMF'
confluence_server_url = 'https://wiki.os.liberty.edu/'
# Confluence publishing configurations
confluence_publish = True
confluence_publish_token = "OTQ0MzI2MTM1MTA1OuNPRV1AM3mHWPN9mLkW23ecAk6y"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
