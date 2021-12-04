import os
import sys

sys.path.insert(0, os.path.abspath("../"))

project = "PyjamasAPI"
copyright = "2021, Harsh"
author = "Harsh"

# The full version, including alpha/beta/rc tags
release = "0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_theme = "alabaster"
pygments_style = "sphinx"

html_static_path = ["_static"]
