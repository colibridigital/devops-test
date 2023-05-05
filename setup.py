from setuptools import setup
setup(
    name = 'news_search',
    version = '0.1.0',
    packages = ['news_search'],
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'news_search = news_search.__main__:main'
        ]
    })