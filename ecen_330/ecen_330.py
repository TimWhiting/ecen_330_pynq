
from pynq import Overlay, PL
import os
import tempfile
import subprocess

ECEN330_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
ECEN330_EXE_DIR = os.path.join(ECEN330_ROOT_DIR, 'executables')
ECEN330_BIT_DIR = os.path.join(ECEN330_ROOT_DIR, 'bitstream')

class ecen_330:
    
    def __init__(self):
		self.bitstream_name="top.bit"
		self.bitstream_path=os.path.join(ECEN330_BIT_DIR, self.bitstream_name)
		if PL.bitfile_name != self.bitstream_path:
			if load_overlay:
				Overlay(self.bitstream_path).download()
			else:
				raise RuntimeError("Incorrect Overlay loaded")
        
    def __del__(self):
        
        
    def getExecutables(self):
		names = ""
		for root, dirs, files in os.walk(ECEN330_EXE_DIR):
			for name in files:
				names += name + " "
		return names
        
    def execute(self,name):
		fullName = ECEN330_EXE_DIR + name
		process = subprocess.Popen([fullName],stdin=None,stdout=subprocess.PIPE,stderr=None,shell=False)
		if process.stderr:
			print process.stderr.readlines()
    

