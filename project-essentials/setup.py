from setuptools import setup, find_packages

requirements = [
]

test_requirements = [
    "coverage",
    "pytest",
    "pytest-asyncio",
    "tox"
]

setup(
    name='project_name',
    version='0.1.0',
    description="",
    author="toolbox",
    author_email='toolbox-devs@tesla.com',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require={
        'dev': requirements,
        'test': test_requirements
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': ['project_name=projectname.cli:main']
    },
)
