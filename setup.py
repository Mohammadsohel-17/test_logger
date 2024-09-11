import os
from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
 
class CustomInstallCommand(install):
    """Custom handler for the 'install' command to remove unwanted packages."""
    def run(self):
        print("######################## starting install.run")
        install.run(self)
        print("######################## starting post install.run")
        # Run the post-install script
        subprocess.call(['python', 'post_install.py'])

setup(
    name="log_caller",  # Replace with your project's name
    version="0.1.0",  # Replace with your project's version
    packages=find_packages(),  # Automatically find and include packages
    #package_data={'': ['deps/*']},
    install_requires=[
        "structlog>=24.4.0","scrubadub[base]",
# List your project dependencies here, or use a requirements.txt file
    ],
    cmdclass={
        'install': CustomInstallCommand,  # Use the custom install command
    },
    author="dipanjan",  # Replace with your name
    python_requires='>=3.6',
    zip_safe=False,
    # entry_points={
    #     'console_scripts': [
    #         'my_project=my_package.your_code:main',
    #     ],
    # },
)
