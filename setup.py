import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='anybase32',
    version='1.1.0',
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/alanblevins/anybase32',
    download_url='https://github.com/alanblevins/anybase32/tarball/1.1.0',
    license='MIT',
    author='Alan Blevins',
    author_email='alan.blevins@gmail.com',
    description='Encode and decode base32 data using arbitrary alphabets',
    keywords=['base32', 'encode', 'decode'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
