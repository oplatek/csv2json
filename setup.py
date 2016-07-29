from setuptools import setup

setup(
  name='csv2json',
  packages=['csv2json'],  # this must be the same as the name above
  version='0.2',
  description='A command-line tools and module to convert csv to json',
  author='Ondrej Platek',
  license='Apache 2.0',
  author_email='ondrej.platek.cz',
  url='https://github.com/oplatek/csv2json',  # use the URL to the github repo
  download_url='https://github.com/oplatek/csv2json/tarball/0.2',  # I'll explain this in a second
  keywords=['csv', 'json', 'conversion'],
  scripts=['csv-to-json'],
  classifiers=[],
)
