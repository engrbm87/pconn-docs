"""Configuration file for the Sphinx documentation builder."""

# -- Project information

import os
import sys

sys.path.insert(0, os.path.abspath("."))

from __version__ import VERSION

project = "Platform Connectors"
copyright = "2025-2026, Gallagher Middle East"
author = "Rami Mousleh"

release = VERSION
version = VERSION
download_link = f"https://github.com/engrbm87/pconn-docs/releases/download/{VERSION}/PconnInstaller-{VERSION}-x64.msi"

# -- General configuration

extensions = ["sphinx.ext.duration", "sphinx.ext.doctest", "sphinx.ext.intersphinx"]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

epub_show_urls = "footnote"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

# Include static assets (images, css, etc.) from _static
html_static_path = ["_static"]

html_logo = "_static/pconn_logo.jpg"

rst_prolog = f"""
.. |download_link| replace:: `this link <{download_link}>`__
"""
