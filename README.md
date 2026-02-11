# Welcome

This is the Python package types-ibapi. This adds type stubs for the `ibapi` package for more reliable type checking.

## Usage

You can use this package in your project by adding the following to your pre-commit hooks or `mypy.ini` file:

```yaml
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.15.0
    hooks:
      - id: mypy
        args: []
        additional_dependencies:
          - pytest
          - numpy
          - types-ibapi  # <---------
```
