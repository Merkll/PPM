import argparse
from ppm import commands

def get_cli_arguments():
  parser = argparse.ArgumentParser(description='This is PPM')

  parser.add_argument("command", choices=commands.choices, help="Type of Command to execute",  nargs='?', default="init")
  return parser.parse_args()
