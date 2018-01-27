from setuptools import setup

setup(name='python_randomUser',
      version='0.1',
      description='Wrapper module for the randomuser.me api',
      url='https://github.com/fuzzylimes/pyRandomUser',
      author='fuzzylimes',
      license='MIT',
      packages=['randomUser'],
      install_requires=[
          'requests==2.18.4'
      ],
      zip_safe=False)