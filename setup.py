from setuptools import setup

setup_requires = [
    'pytest-runner',
]

install_requires = [
    'requests',
    'lxml',
    'bs4',
    'attrs',
]

tests_requires = [
    'pytest'
]

setup(
    name='cibus_cli',
    description='cibus_cli',
    version='0.0.2',
    packages=['cibus'],
    author='Nadav Yutal',
    author_mail='nyutal@gmai.com',
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_requires,
)
