from ConfigParser import RawConfigParser
import os
import subprocess

class _InstallModules:
    def __init__(self):
        _config = RawConfigParser()
        _config.read(os.path.join(os.path.dirname(__file__), '../silpa.conf'))

        self.modules = {}
        for module, status in _config.items('modules'):
            self.modules[module] = status if status else "no"

        self.modules_gitnames = {}
        for module, name in _config.items('module_gitnames'):
	    if self.modules[module] == "yes":
            	self.modules_gitnames[module] = name

_config = _InstallModules()

def _writeRequirements():
	FILE = 'modules.txt'
	modules = open(FILE, "w")
	FLAG = '-e'
	BASE_URL = 'git+git://github.com/Project-SILPA/'
	for values in _config.modules_gitnames.values():
		modulename = FLAG+' '+BASE_URL+values+'.git'+'#egg='+values+'\n'
		modulename.encode('utf-8')
		modules.write("%s"%modulename)
	modules.close()

_writeRequirements()

def _install():
	    subprocess.call(['pip', 'install','-r', 'modules.txt'])
_install()





