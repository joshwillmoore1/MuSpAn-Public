import os
import sys
from datetime import date
import toml

sys.path.insert(0, os.path.abspath('/Users/joshuamoore/Dropbox/Ox_PostDoc/Code/MuSpAn'))
# Load the version from pyproject.toml
pyproject_path = os.path.abspath(os.path.join('/Users/joshuamoore/Dropbox/Ox_PostDoc/Code/MuSpAn', 'pyproject.toml'))
with open(pyproject_path, 'r') as f:
    pyproject_data = toml.load(f)


project = 'MuSpAn'
copyright = f'2024-{date.today().year}, Joshua A. Bull, Joshua W. Moore  & Helen M. Byrne'
author = 'Joshua A. Bull, Joshua W. Moore & Helen M. Byrne'
release = pyproject_data['project']['version']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_favicon",
    "sphinx_copybutton",
    "sphinx_reredirects",
    "texext",
    "numpydoc",
    "matplotlib.sphinxext.plot_directive",
    "nbsphinx",
    "sphinxcontrib.collections",
    "sphinx_gallery.load_style",
    "sphinx_rtd_theme",
    "sphinx_tabs.tabs",
    "sphinx-prompt",
    "sphinx_design",
    "sphinxcontrib.bibtex",
    'sphinx-jsonschema'
]

# added layout.html in templates which adds the schema json to the header of specific pages - helps search engines
templates_path = ["_templates"]
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
language = 'en'

github_username = 'JABull1066'
github_repository = 'MuSpAn'

bibtex_bibfiles = ['muspan_citations.bib']

html_theme = 'pydata_sphinx_theme'
html_title = 'Multiscale Spatial Analysis'
html_short_title = 'MuSpAn'

autodoc_inherit_docstrings = True
inheritance_graph_attrs = dict(rankdir="TB", size='""', fontsize=14, ratio='compress')
add_module_names = False

# The suffix of source filenames.
source_suffix = ".rst"
default_role = "autolink"
add_function_parentheses = False

autosummary_generate = True
numpydoc_show_class_members = False


autodoc_default_options = {
    'inherited-members': None,
}
autodoc_typehints = 'none'
copybutton_only_copy_prompt_lines = False
html_show_sourcelink = False
html_copy_source = False

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

# Redirect index to Documentation.html
redirects = {
    "index": "Documentation.html",
}

html_context = {
    "default_mode": "auto",
    
    "schema_jsonld": {
        "tutorials": {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": "Spatial Analysis Tutorials",
            "description": "Step-by-step tutorials on using MuSpAn for spatial data analysis.",
            "url": "https://docs.muspan.co.uk/latest/tutorials.html"
        }
    }

}

# Drop out the sidebar on specific pages
html_sidebars = {
    "Installation": [],
    "glossary": [],
    "references": [],
}

html_theme_options = {
    "primary_sidebar_end": ["indices.html"],
    "logo": {
        "link": "https://www.muspan.co.uk",
        "image_light": "images/muspan_logo_lightmode.png",
        "image_dark": "images/muspan_logo_darkmode.png",
    },
    "navbar_end": ["navbar-icon-links", "theme-switcher"],
    "navbar_start": ["navbar-logo", "version-switcher"],
    "collapse_navigation": True,
    "navigation_depth": 2,
    "show_prev_next": False,
    "footer_start": ["copyright"],
    "footer_end": ["last-updated"],
    "header_links_before_dropdown": 7,
    "icon_links": [
        {
            "name": "Gitter",
            "url": "https://app.gitter.im/#/room/#muspan-community:gitter.im",
            "icon": "fab fa-gitter",
            "type": "fontawesome",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/joshwillmoore1/MuSpAn-Public",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
    ],
    "icon_links_label": "Quick Links",
    "analytics": {"google_analytics_id": "G-NYJKGWRYPR"},
    "switcher": {
        "json_url": 'https://docs.muspan.co.uk/version_switcher.json',
        "version_match": release,
    },
    "announcement": "https://raw.githubusercontent.com/joshwillmoore1/MuSpAn-Public/refs/heads/main/announcements/muspan_announce.html",
}

collections = {
    'basic_tutorials': {
        'driver': 'copy_folder',
        'source': '../tutorials/getting_started',
        'target': 'getting_started/',
        'ignore': ['*.py', '.sh'],
    },
    'import_io': {
        'driver': 'copy_folder',
        'source': '../tutorials/importing_data',
        'target': 'importing_data/',
        'ignore': ['*.py', '.sh'],
    },
    'query_tutorials': {
        'driver': 'copy_folder',
        'source': '../tutorials/queries',
        'target': 'queries/',
        'ignore': ['*.py', '.sh'],
    },
    'objects_tutorials': {
        'driver': 'copy_folder',
        'source': '../tutorials/working_with_objects',
        'target': 'working_with_objects/',
        'ignore': ['*.py', '.sh'],
    },
    'spatial_analysis': {
        'driver': 'copy_folder',
        'source': '../tutorials/spatial_analysis_methods',
        'target': 'spatial_analysis_methods/',
        'ignore': ['*.py', '.sh'],
    },
    'net_tutorials': {
        'driver': 'copy_folder',
        'source': '../tutorials/spatial_networks',
        'target': 'spatial_networks/',
        'ignore': ['*.py', '.sh'],
    },
    'paper_tutorials': {
        'driver': 'copy_folder',
        'source': '../tutorials/paper_tutorials',
        'target': 'paper_tutorials/',
        'ignore': ['*.py', '.sh'],
    },
    'net_analysis': {
        'driver': 'copy_folder',
        'source': '../tutorials/network_analysis',
        'target': 'network_analysis/',
        'ignore': ['*.py', '.sh'],
    },
    'region_analysis': {
        'driver': 'copy_folder',
        'source': '../tutorials/region_based_analysis',
        'target': 'region_based_analysis/',
        'ignore': ['*.py', '.sh'],
    },
    'dist_analysis': {
        'driver': 'copy_folder',
        'source': '../tutorials/distribution_analysis',
        'target': 'distribution_analysis/',
        'ignore': ['*.py', '.sh'],
    },
    'tda': {
        'driver': 'copy_folder',
        'source': '../tutorials/topology',
        'target': 'topology/',
        'ignore': ['*.py', '.sh'],
    },
    'geo': {
        'driver': 'copy_folder',
        'source': '../tutorials/geometry',
        'target': 'geometry/',
        'ignore': ['*.py', '.sh'],
    },
    'release_notes': {
        'driver': 'copy_folder',
        'source': '../release_notes/generated_release_notes',
        'target': 'release_notes/',
        'ignore': ['*.py', '.sh'],
    },
    'misc': {
        'driver': 'copy_folder',
        'source': '../tutorials/misc',
        'target': 'misc/',
        'ignore': ['*.py', '.sh'],
    },
    
    'wf': {
        'driver': 'copy_folder',
        'source': '../tutorials/workflows',
        'target': 'workflows/',
        'ignore': ['*.py', '.sh'],
    },
}
