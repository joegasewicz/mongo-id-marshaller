from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mongo-id-marshaller",
    version="0.0.1",
    description="A small library that marshals Mongo ObjectIds",
    packages=["mongo_id_marshaller"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/mongo-id-marshaller",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com",
    extras_require={
        "dev": [
            "pytest",
            "bson",
            "mongomock",
        ]
    }
)
