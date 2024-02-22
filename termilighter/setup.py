from setuptools import setup, find_packages
import os

with open("README.md", "r") as f:
    readme = f.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()


setup(
    name="termilighter",
    package_dir={"": "src"},
    packages=find_packages(where="src", include=["*"]),
    include_package_data=True,
    version="0.0.2",
    author="Abdullah Amjad",
    author_email=os.environ.get("EMAIL"),
    url="https://github.com/createwithabd/termilighter/tree/master/termilighter",
    description="Package for customizing terminal output display.",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    keywords=[
        "color output",
        "highlighter",
        "color converter",
        "converter",
        "termilighter",
    ],
    python_requires=">=3",
    install_requires=[""],
    test_suite="tests",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.0",
    ],
    license="License :: OSI Approved :: MIT License",
    zip_safe=False,
)
