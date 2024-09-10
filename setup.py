from setuptools import find_packages, setup

setup(
    name="log_abstractor",
    version="1.1.2",
    packages=find_packages(),
    install_requires=[
        "structlog>=24.4.0", "scrubadub>=2.0.1",
    ],
    description="Optimized anonymizer with pre-scrubbing.",
    author="Dipanjan Mazumder",
    author_email="dmazumder@hhaexchange.com",
    url="https://github.com/HHAeXchange/platform-logger",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
