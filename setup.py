from setuptools import setup, find_packages
import sys, os

version = '0.8'

setup(name='WebError',
      version=version,
      description="Web Error handling and exception catching",
      long_description="""\
""",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
      ],
      keywords='wsgi',
      author='Ben Bangert, Ian Bicking, Mark Ramm',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.filter_app_factory]
      error_catcher = weberror.exceptions.errormiddleware:make_error_middleware
      cgitb = weberror.cgitb_catcher:make_cgitb_middleware
      evalerror = weberror.evalexception.middleware:make_eval_exception
      """,
      )
