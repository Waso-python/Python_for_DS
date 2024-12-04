from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="sdarr",
    author_email="sdarr@student.42.fr",
    url="https://github.com/sdarr/ft_package",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
