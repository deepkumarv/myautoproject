> python3 -m venv myautoproject_venv
> source myautoproject_venv/bin/activate
> pip install wheel
> pip install setuptools
> pip install twine
> 
> setup.py file structure is as below
> 
> from setuptools import find_packages, setup
setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
> 
> pip install pytest
> 
> To run the tests:
> python setup.py pytest
> 
> To build the python library:
> python setup.py bdist_wheel
> Then python library gets created in dist folder.
> 
> 