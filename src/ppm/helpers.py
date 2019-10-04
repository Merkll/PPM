
from os import path, getcwd, mkdir, chmod, environ
import subprocess
import json
from ppm import config

import pkg_resources

root = getcwd()

def write_json(data):
  with open('{}/package.json'.format(root), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

def read_json():
  with open('{}/package.json'.format(root), 'r', encoding='utf-8') as f:
    return json.load(f)

def init_venv():
  subprocess.Popen(["virtualenv", config.package_dir_name]).wait()
  venv_file = "{}/{}/bin/activate_this.py".format(root, config.package_dir_name)
  exec(open(venv_file).read(), {'__file__': venv_file})

def read_file(filename):
  with open('{}/{}'.format(root, filename), 'r', encoding='utf-8') as f:
    return f.read()

def run_pip_install(package):
  return subprocess.Popen(["pip", "install"] + package).wait()
