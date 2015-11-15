from distutils.core import setup
setup(
  name = 'silver',
  packages = ['silver'], # this must be the same as the name above
  version = '0.2',
  description = 'SilverCore API python wrapper',
  author = 'Alejandro Saucedo',
  author_email = 'alejandro@hackpartners.com.com',
  url = 'https://github.com/HackTrain/silver',
  download_url = 'https://github.com/HackTrain/silver/tarball/0.2', 
  keywords = ['silvercore', 'silver', 'hackpartners', 'hacktrain', 'hack', 'partners'], 
  include_package_data=True,
  install_requires=[
        "pyxb",
        "suds"
    ],
  classifiers = [],
)