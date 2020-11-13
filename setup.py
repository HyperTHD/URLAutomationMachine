from setuptools import setup 

setup(
name = 'urlChecker',
version = '1', 
install_requires = ['urllib3', 'colorama', 'black', 'pylint'], 
py_modules = ['urlChecker'],

entry_points={
'console_scripts':
['url_checker = url_checker : main']} 
)