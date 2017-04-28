from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import ecen_330

setup(
    name = "ecen_330",
    version = ecen_330.__version__,
    url = 'https://github.com/TimWhiting/ecen_330_pynq',
    license = 'All rights reserved.',
    author = "Tim Whiting",
    author_email = "tim@whitings.com",
    packages = ['ecen_330'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so','*.elf'],
    },
    description = "New custom overlay for PYNQ-Z1"
)