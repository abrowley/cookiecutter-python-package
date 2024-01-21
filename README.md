# COOKIECUTTER-PYTHON-PACKAGE

A Cookie Cutter Template [https://cookiecutter.readthedocs.io/] for a Python Package
using setuptools with a pyproject.toml and automatic source control version generation.

Adds pytest.

To use

In a python venv:

```
pip install cookiecutter
cookiecutter gh:abrowley/cookiecutter-python-package
```

Follow the prompts, setting the name of the package (project_name). The package name will follow the project name but ensure it is a valid packasge name, this is the project_slug.

When complete

```
cd project_slug
git init
python -m venv .venv
pip install -r requirements.txt
python -m build
python -m pytest tests
```

Alex Rowley
21 Jan 2023