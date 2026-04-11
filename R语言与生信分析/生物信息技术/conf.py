project = '生物信息技术教程'
copyright = '2025, Medical Student Rescue Plan'
author = 'Medical Student Rescue Plan'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

pygments_style = 'sphinx'

master_doc = 'index'

language = 'zh_CN'

html_theme_options = {
    'description': '生物信息技术基础教程',
    'fixed_sidebar': True,
    'sidebar_width': '260px',
}

html_context = {
    'display_github': False,
}
