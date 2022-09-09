from setuptools import setup

setup(
    name="docket",
    version="0.1.0",
    description="Backscatter scraping tables",
    url="https://github.com/bipsen/docket",
    author="Bertil Johannes Ipsen",
    author_email="ipsen.bertli@gmail.com",
    license="MIT",
    packages=["docket"],
    install_requires=[
        "pyairtable",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
