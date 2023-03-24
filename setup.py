import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piti",
    version="0.0.1",
    author="meraklibaykus",
    author_email="eseryologlu@gmail.com",
    description="A simple calculator using ANTLR and Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meraklibaykus/piti",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'antlr4-python3-runtime>=4.9.2',
    ],
    entry_points={
        'console_scripts': [
            'piti = piti.__main__:main'
        ]
    }
)
