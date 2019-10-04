import argparse
from ppm import commands

def get_cli_arguments():
  parser = argparse.ArgumentParser(description='This is PPM')

  parser.add_argument("command", choices=commands.choices, help="Type of Command to execute",  nargs='?', default="init")
  parser.add_argument('-D', action="store_true", dest='dev_mode',
                    help='Save as a development dependency', default=False)

  return parser.parse_known_args()
