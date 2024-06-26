from setuptools import setup

setup(
    name='pydrc',
    version='0.1.0',
    description='Python module for fitting, analysis and visualization of dose-response data',
    license='MIT'
    authors='Mathias Fon, Hallvard Wæhler',
    url='https://github.com/Mr-Mathias-F/pydrc',
    packages=['pydrc'],
    install_requires=['numpy', 'scipy', 'pandas'],
    tests_require='pytest',
    python_requires='>=3.8',
    zip_safe=True,
)
