from setuptools import setup, find_packages

setup(
    name="abacus",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'abacus=abacus.main:main',
        ],
    },
    author="Harry Iraku",
    description="A command line calculator for a wide range of mathematical problems.",
    long_description=open('docs/README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
