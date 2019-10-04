from os import path, getcwd
from ppm import prompt, helpers, init
import pkg_resources

package_name = path.basename(getcwd())

class Install:
  def __init__(self, data, dev_mode):
    self.install_data = data
    self.dependencies = None
    self.dev_mode = dev_mode
    helpers.init_venv() 

  def install_from_package(self):
    package_init = init.Init()
    self.dependencies = package_init.get_dependencies()
    package_list = self.build_install_list()

    self.install_package(package_list)
  
  def install_specific_package(self):
    package_init = init.Init()
    self.install_package(self.install_data)
    for package in self.install_data:
      package = package.split("==")
      name = '',
      version = ''
      if len(package) == 2:
        name, version = package
      else:
        name = package[0]
        version = self.get_package_version(name)
        
    package_init.add_dependencies(name, version, self.dev_mode)
    package_init.write_package_json()

  
  def build_install_list(self):
    return [(lambda n, v: n + "==" + v)(depName, depVersion) for depType, depList in self.dependencies.items() for depName, depVersion in depList.items() ]
  
  def install_package(self, package):
    return helpers.run_pip_install(package)
  
  def get_package_version(self, package):
    return pkg_resources.get_distribution(package).version

  def run_install(self):
    if len(self.install_data):
      self.install_specific_package()
    else:
      return self.install_from_package()

