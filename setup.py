from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="sp_mysql",
    version="1.0.1",
    description="A Python package to work with mysql database.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/suryaprakash0831/sp_mysql",
    author="Suryaprakash S",
    author_email="suryaprakash0831@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sp_mysql"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "sp-msql=sp_mysql.cli:main",
        ]
    },
)