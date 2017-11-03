
# create a folder for py files
# create setup.py

from distutils.core import setup
setup(
    name = "python_programming",
    version="1.0", # depend on you
    py_modules=['a11_function', 'a12_unittest'],

    # metadata
    author = "me",
    author_email="gmail",
    description="what does your lib do",
    license="Public",
    keywords="deep learning",
)

# create an virtual env to install this module
python setup.py install
# go elsewhere, in python check __file__ location

# package all dependencies into a zip file
python setup.py sdist --format zip
# it will create a zip file
unzip ...zip

python setup.py sdist --help-formats
