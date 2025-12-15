"""Configuration file for the Sphinx documentation builder."""

# -- Project information

project = "Platform Connectors"
copyright = "2025, Gallagher Middle East"
author = "Rami Mousleh"

release = "0.1"
version = "0.1.0"

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

# -- Options for EPUB output
