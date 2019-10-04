from os import path, getcwd
from ppm import prompt, helpers

package_name = path.basename(getcwd())

questions = [
    {"question": "package name", "key": "package_name", "default": package_name },
    {"question": "version", "key": "version", "default": "1.0.0" },
    {"question": "description", "key": "description", "default": "" },
    {"question": "entry_point", "key": "entry", "default": "app.py" },
    {"question": "git repository", "key": "git_repository", "default": "" },
    {"question": "author", "key": "author", "default": "" },
    {"question": "license", "key": "license", "default": "ISC" },
  ]

class Init:
  def __init__(self):
    self.__package_config = None
    self.dep_name = "dependencies"
    self.dev_dep_name = "devDependencies"
  
  @property
  def package_config(self):
    return self.__package_config

  @package_config.setter
  def package_config(self, value):
    self.__package_config = value

  def generate_package_json(self):
    package_config = {}
    for question in questions:
      question_title = question.get('question')
      ans = prompt.cli_prompt(question_title, question.get('answer'), question.get('required'), question.get('default'))
      package_config[question.get('key', question_title)] = ans

    package_config['scripts'] = {}
    
    ans = prompt.cli_prompt("Is this ok", ["yes", "no"], True) 

    if ans == 'yes': 
      self.package_config = package_config
      return self.package_config

  def add_dependencies(self, name, version, dev=False):
    print(name, version)
    depType = self.dev_dep_name if dev else self.dep_name
    self.package_config = self.package_config or helpers.read_json()
    self.package_config[depType] = self.package_config.get(depType) or {}
    self.package_config[depType][name] = version 

    self.package_config = self.package_config

    return self.package_config

  def get_dependencies(self):
    self.package_config = self.package_config or helpers.read_json()

    return { self.dep_name: self.package_config.get(self.dep_name, {}), self.dev_dep_name: self.package_config.get(self.dev_dep_name, {}) }

  def add_requirements_to_dependencies(self):
    requirements = self.read_requirement_txt()
    for package in requirements:
      if package != '':
        name, version = package.split('==')
        self.add_dependencies(name, version)
    return self.package_config
  
  def write_package_json(self):
    return helpers.write_json(self.package_config)

  def read_requirement_txt(self):
    return helpers.read_file('requirements.txt').split('\n')
