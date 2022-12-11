try:
    from setuptools import setup
except ImportError:
    from distutile.core import setup

config = {
    'description': 'My Project',
    'author': 'Wang Hongyu',
    'url': '',
    'download_url': '',
    'author_email': 'wang_al@qq.com',
    'version': '0.1',
    'install_requires': ['none'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
