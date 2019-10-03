from ppm.ppm import PPM

def ppm():
  package_manager = PPM()
  print(package_manager.cli_arguments)
  package_manager.executeCommand()

if __name__ == "__main__":
  ppm()