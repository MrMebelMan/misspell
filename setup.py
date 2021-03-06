import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='misspell',
    version='0.6',
    scripts=['misspell/__init__.py'],
    author='Vladyslav Burzakovskyy',
    author_email='mutex-lock@protonmail.com',
    description='Some functions that introduce random typographical errors in provided text.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MrMebelMan/misspell',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

