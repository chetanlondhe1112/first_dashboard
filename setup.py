from setuptools import setup, find_packages

def readme():
  with open('README.md') as f:
    README = f.read()
    return README

NAME='First dashboard(upgraded)'
AUTHOR='Chetan Arvind Londhe'
MAIL='chetanlondhe1112@gmail.com'
VERSION = '0.0.0'
DESCRIPTION = 'Environment study dashboard'
LONG_DESCRIPTION = ''
KEYWORD=['python', 'plotly','pandas','style','charts','streamlit']
LICENSE='MIT'
# Setting up
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=MAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=KEYWORD,
    license=LICENSE,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
)