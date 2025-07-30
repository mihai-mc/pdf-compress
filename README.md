# Neural Geometric Parametrisation (NGP)

Research MSc project at The University of Edinburgh

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/github/license/mihai-mc/pdf-compress)

[//]: # (![CI]&#40;https://github.com/mihai-mc/ngp/actions/workflows/main.yml/badge.svg&#41;)

# Requirements

* Python 3.12
* pip3
* virtualenv

## Set up Virtual environment

``` python
    virtualenv --python=python3.12 env
    . env/bin/activate
```

## Install Dependencies

``` python
    pip install -r requirements.txt
    pip install "git+https://github.com/facebookresearch/pytorch3d.git@V0.7.8" --no-build-isolation
```

## Convention

All scripts assume that they are being run from the root of the repo. Please adjust paths accordingly.
