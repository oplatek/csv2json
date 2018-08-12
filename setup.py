from setuptools import setup
version = '0.2.2'
name = 'csv2json'

setup(
  name=name,
  packages=[name],  # this must be the same as the name above
  version=version,
  description='A command-line tools and module to convert csv to json',
  long_description="""
    See https://github.com/oplatek/csv2json/blob/master/README.md
  """,
  author='Ondrej Platek',
  license='Apache 2.0',
  author_email='ondrej.platek@seznam.cz',
  url='https://github.com/oplatek/csv2json',  # use the URL to the github repo
  download_url='https://github.com/oplatek/csv2json/tarball/%s' % version,
  keywords=['csv', 'json', 'conversion'],
  scripts=['csv-to-json'],
  classifiers=[],
)
