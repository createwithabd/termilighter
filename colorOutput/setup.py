from setuptools import setup, find_packages
import os

# Reading README and converting it to long description.
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="colorOutput",
    version="0.0.1",
    author="Abdullah Amjad",
    author_email=os.environ.get("EMAIL"),
    description="Package for highlighting output text on terminal, and converting hex and rgb colors to xterm colors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/createwithabd/highlighter/tree/master/colorOutput",
    keywords=[
        "terminal-highlight",
        "print-terminal",
        "color-terminal",
        "xterm-colors",
        "conversion",
        "rgb_to_hex",
        "hex_to_rgb development",
        "highlight",
        "highlighter",
    ],
    py_modules=["textHighlight"],
    package_dir={"": "src"},
    python_requires=">=3",
    install_requires=[""],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
    license="License :: OSI Approved :: MIT License",
)
