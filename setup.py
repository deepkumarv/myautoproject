from setuptools import find_packages, setup
setup(
    name='pradeepkumarlibs',
    packages=find_packages(include=['pradeepkumarlibs']),
    version='0.1.0',
    description='my first python library',
    readme='README.md',
    auther='V Pradeep Kumar',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest==7.2.1'],
    test_suite='tests',
    long_description="long_description",

)