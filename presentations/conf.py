# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Open-Needs Introduction'
copyright = '2022, Open-Needs community'
author = 'Open-Needs community'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.plantuml',
    'sphinxcontrib.needs',
    'sphinx_revealjs',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.inheritance_diagram',
    'sphinxcontrib.programoutput',
    'sphinxcontrib.sadisp'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'slides']


revealjs_style_theme = "moon"
revealjs_static_path = ['_static']
revealjs_css_files = ['custom.css']

revealjs_script_conf = """
{
    controls: true,
    transition: 'slide',
    progress: true,
    history: true,
    keyboard: true,
    preloadIframes: true,
}
"""

revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs4/plugin/notes/notes.js",
    },
    # {
    #     "name": "RevealHighlight",
    #     "src": "revealjs4/plugin/highlight/highlight.js",
    # },
]

# plantuml_output_format = 'png'
plantuml_output_format = 'svg_img'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']