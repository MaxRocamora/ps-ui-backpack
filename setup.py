from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyside-ui-backpack',
    version='0.1.0',
    description='Helper functions for PySide2 UI development',
    url='https://github.com/MaxRocamora/ps-ui-backpack',
    author='Maximiliano Rocamora',
    author_email='maxirocamora@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU GENERAL PUBLIC LICENSE',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: PySide2 :: UI :: Development"
    ],
    python_requires='>=3.7',
    package_data={
        '': ['README.md'],
    },
    include_package_data=True,
    test_suite='tests',
    project_urls={
        'Source': 'https://github.com/MaxRocamora/ps-ui-backpack',
    },
)
