import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = "django-hitcount-lite",
    version = "0.2.1",
    packages=['hitcount'],
    license = 'BSD',
    description = "Django hit counter application that tracks the number of hits/views for chosen objects",
    long_description = README,
    author = 'Damon Timm',
    author_email = 'damontimm@gmail.com',
    maintainer='Basil Shubin',
    maintainer_email='basil.shubin@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
)
