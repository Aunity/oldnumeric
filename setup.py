from setuptools import setup, find_packages

setup(name='oldnumeric',
      version='1.1',
      description='The oldnumeric numpy package',
      author='xoviat',
      author_email='xoviat@noreply.users.github.com',
      packages=find_packages(),
      install_requires=[
            'numpy',
      ],
     )
