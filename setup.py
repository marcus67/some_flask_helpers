from setuptools import setup

setup_params = {
    # standard setup configuration
    "name": "some-flask-helpers",
    "version": "0.1",
    "description": "Generic tools for Flask applications",
    "author": "Marcus Rickert",
    "author_email": "marcus.rickert@web.de",
    "url": "https://github.com/marcus67/flask_helpers",

    "install_requires": [
        'flask'
    ],

    "packages": ['some_flask_helpers'],
    "include_package_data": True,

    "long_description": """Really long text here.""",
}

extended_setup_params = {
    # additional setup configuration used by CI stages
    "id": "some-flask-helpers",
}

extended_setup_params.update(setup_params)

if __name__ == '__main__':
    setup(**setup_params)
