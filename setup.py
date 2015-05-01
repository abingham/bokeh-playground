import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'bokeh',
    'gitpython',
    'ipython',
    'jsonschema',
    'pyzmq',
    ]

setup(name='bokeh-playground',
      version='0.0',
      description='Bokeh playground',
      long_description=README,
      license="MIT License",
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Austin Bingham',
      author_email='austin.bingham@gmail.com',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
