from ppm import arguments, init, helpers

class PPM:  
  def __init__(self, *args, **kwargs):
    self.__cli_arguments = arguments.get_cli_arguments()

  @property
  def cli_arguments(self):
    return self.__cli_arguments
  
  def init(self):
    package_init = init.Init()
    package_config = package_init.generate_package_json()
    if not package_config: return

    helpers.init_venv()
    package_config = package_init.add_requirements_to_dependencies()
    helpers.write_json(package_config)

  def executeCommand(self):
    command_handler = self.__getattribute__(self.cli_arguments.command)
    command_handler()
