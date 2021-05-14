from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]


setup(
    name='simple_calculator',
    version='0.0.1',
    description='Simple calculator package example.',
    long_description=open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Ayush6459/Simple_Calculator_package.git',
    author='Ayush Ranjan',
    author_email='ayushranjan6459@gmail.com',
    Licence='MIT',
    classifiers=classifiers,
    keyword='calculator',
    #packages=find_packages(),
    install_requires=[''],
    py_modules=["Calculator"],
    package_dir={'': 'src'},
    extras_require={
        "dev":[
            "pytest>=3.7",
        ],
    },
)
