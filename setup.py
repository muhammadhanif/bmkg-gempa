import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bmkg-gempa",
    version="1.0.1",
    author="Muhammad Hanif",
    author_email="moehammadhanif@gmail.com",
    description="Konversi data gempa bumi BMKG dari XML ke JSON.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muhammadhanif/bmkg-gempa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
