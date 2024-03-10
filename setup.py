"""
pydrc: Python module for fitting, analysis and visualization of dose-response data
"""

from setuptools import setup


setup(
    name='pydrc',
    version='0.0.1',
    description='Python module for fitting, analysis and visualization of dose-response data',
    author='Mathias Fon, Hallvard Wæhler',
    url='https://github.com/Mr-Mathias-F/pydrc',
    packages=['pydrc'],
    install_requires=read_requirements(),
    tests_require='pytest',
    python_requires='>=3.8',
    zip_safe=True,
)

