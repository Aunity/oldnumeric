from setuptools import setup, find_packages

setup(name='oldnumeric',
      description='The oldnumeric numpy package',
      author='xoviat',
      author_email='xoviat@noreply.users.github.com',
      packages=find_packages(),
      install_requires=[
            'numpy',
      ],
      setup_requires=[
            'setuptools',
      ],
      version='1.0.5',
      #use_scm_version=True,
     )
