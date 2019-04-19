from setuptools import setup

setup_params = {
    # standard setup configuration
    "name": "flask-helpers",
    "version": "0.1",
    "description": "Generic tools for Flask applications",
    "author": "Marcus Rickert",
    "author_email": "marcus.rickert@web.de",
    "url": "https://github.com/marcus67/flask_helpers",

    "install_requires": [
        'flask==0.12.1'
    ],

    "packages": ['flask_helpers'],
    "include_package_data": True,

    "long_description": """Really long text here.""",

    # additional setup configuration used by CI stages
    "id": "flask-helpers",
    "revision": "1"
}

if __name__ == '__main__':
    setup(**setup_params)
