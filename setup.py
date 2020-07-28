import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="semantic_nutrition_joshuadrc", # Replace with your own username
    version="0.0.2",
    author="Joshua D'Arcy",
    author_email="joshuadrc@gmail.com",
    description="Tools for semantic nutrition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)