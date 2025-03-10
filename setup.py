#!/usr/bin/env python
# coding: utf-8
import os.path as osp
from setuptools import setup, find_packages


def get_version():
    # From: https://github.com/facebookresearch/iopath/blob/master/setup.py
    # Author: Facebook Research
    init_py_path = osp.join(
        osp.abspath(osp.dirname(__file__)), "graphgallery", "version.py"
    )
    init_py = open(init_py_path, "r").readlines()
    version_line = [line.strip() for line in init_py if line.startswith("__version__")][
        0
    ]
    version = version_line.split("=")[-1].strip().strip("'\"")

    return version


VERSION = get_version()
url = 'https://github.com/EdisonLeeeee/GraphGallery'


install_requires = [
    # Do not add pytorch here. Users should install
    # pytorch themselves, preferrably by OS's package manager, or by
    # choosing the proper pypi package name at
    # pytorch: https://pytorch.org/
    'tqdm',
    'yacs',
    'scipy',
    'numpy',
    'tabulate',
    'pandas',
    'scikit_learn>=0.21.0',
    'networkx>=2.3',
    'gensim>=3.8.0',
    'numba>=0.46.0',
]

setup_requires = ['pytest-runner']
tests_require = ['pytest', 'pytest-cov']

setup(
    name='graphgallery',
    version=VERSION,
    description='A Graph-based Model Gallery for Benchmarking Graph Neural Networks.',
    author='Jintang Li',
    author_email='lijt55@mail2.sysu.edu.cn',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, VERSION),
    keywords=[
        'pytorch',
        'benchmark',
        'model-gallery',
        'geometric-deep-learning',
        'graph-neural-networks',
    ],
    python_requires='>=3.6',
    license="MIT LICENSE",
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    packages=find_packages(exclude=("examples", "imgs", "benchmark", "test")),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
