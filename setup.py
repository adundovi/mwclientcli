from setuptools import find_packages, setup

setup(name="mwclientcli",
      version="0.1",
      description="A set of tools to read and edit MediaWiki site from a command line intefrace",
      author="Andrej Dundovic",
      author_email='andrej@dundovic.com.hr',
      platforms=["linux"],
      license="BSD",
      url="",
      keywords="mediawiki mwclient",
      packages=find_packages(),
      install_requires=["mwclient>=0.8.1"],
      entry_points={
          'console_scripts': [
              'wiki = mwclientcli.__main__:main'
          ]
      },
     )
