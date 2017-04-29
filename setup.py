from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import ecen_330
import os

setup(
    name = "ecen_330_pynq",
    version = ecen_330.__version__,
    url = 'https://github.com/TimWhiting/ecen_330_pynq',
    license = 'All rights reserved.',
    author = "Tim Whiting",
    author_email = "tim@whitings.org",
    include_package_data = True,
    packages = ['ecen_330'],
    package_data = {
    'ecen_330' : ['*/*.bit','*/*.tcl','*/*.so','*/*.bin','*/*.txt', '*/*.cpp', '*/*.h', '*/*.sh','*/*.elf'],
    },
    data_files = [(os.path.join('/home/xilinx/jupyter_notebooks/ecen_330',root.replace('notebook/','')), [os.path.join(root, f) for f in files]) for root, dirs, files in os.walk('notebook/')],
    description = "New custom overlay for PYNQ-Z1"
)