from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests', 'pandas' , 'os', 'datetime']

# some more details
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    ]

# calling the setup function 
setup(name='CorrelAPI',
      version='1.0.3',
      description='Test of packaging python code as a REST API',
      long_description=long_description,
      url='https://github.com/lunabre/CorrelAPI',
      author='BRENDA',
      author_email='balunapardo@gmail.com',
      license='MIT',
      packages=['correl_pkg'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='correl api'
      )