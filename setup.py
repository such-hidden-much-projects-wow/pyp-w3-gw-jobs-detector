import os
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ["tests/"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import sys, pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def extract_requirements_from_file(req_file_name):
    with open(req_file_name, 'r') as fp:
        return [line.strip() for line in fp
                if line.strip() and not line.startswith('-r')]

requirements = extract_requirements_from_file('requirements.txt')
dev_requirements = (requirements +
                    extract_requirements_from_file('dev-requirements.txt'))


setup(
    name='rmotr.com | Jobs Detector',
    version='0.0.1',
    description="rmotr.com Group Project | Jobs Detector",
    # url=project_url,
    # download_url="{url}/tarball/{version}".format(
    #     url=project_url, version=version),
    author='rmotr.com',
    author_email='questions@rmotr.com',
    license='CC BY-SA 4.0 License',
    scripts=['jobs_detector/main.py'],
    packages=['jobs_detector'],
    maintainer='rmotr.com',
    install_requires=requirements,
    tests_require=dev_requirements,
    entry_points={
        'console_scripts': [
            'jobs_detector = main:jobs_detector'
        ]
    },
    zip_safe=True,
    cmdclass={'test': PyTest},
)
