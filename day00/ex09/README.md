# ft_package

A simple test package for demonstration purposes.

## Installation

You can install the package using either of these commands:

```bash
pip install build
```

```bash	
python -m build
```

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```
or
```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

To use the package, you can import the functions as follows:
```python
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

```bash
pip list
pip show -v ft_package
```
