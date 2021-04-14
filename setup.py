from setuptools import find_namespace_packages, setup
from codecs import open


with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()


with open('VERSION', 'r', 'utf-8') as f:
    version = f.read()


setup(
    name='prodinf-dbspy',
    version=version,
    description='Web application for monitoring MySQL database statistics',
    long_description=readme,
    author="Luca Da Rin Fioretto",
    author_email="ldrf@ebi.ac.uk",
    maintainer="Ensembl Production Team",
    maintainer_email="ensembl-production@ebi.ac.uk",
    packages=find_namespace_packages(include=['ensembl.*']),
    license='Apache 2.0',
    package_data={'': ['LICENSE', 'NOTICE']},
    zip_safe=False,
    install_requires=[
        'fastapi',
        'uvicorn[standard]',
        'gunicorn',
        'sqlalchemy',
        'mysqlclient'
    ],
    python_requires='>=3.7, <4',
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
