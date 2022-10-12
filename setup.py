from setuptools import setup

setup(
    name='input_output',
    version='0.1.0',
    author='Fawdy',
    py_modules=['input_output'],
    install_requires=[
      'numpy==1.23.0',
      'pandas==1.4.3',
      'openpyxl==3.0.10'
    ],
    entry_points='''
        [console_scripts]
        input_output=input_output:input_output
    ''',
)