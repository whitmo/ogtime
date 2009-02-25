from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='OGTime',
      version=version,
      description="Time tracking app for OpenGeo",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='time',
      author='whit',
      author_email='whit@opengeo.org',
      url='http://www.opengeo.org',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'PasteDeploy',
          'jsonstore'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = ogtime.wsgiapp:make_app
      """,
      )
