from os import path
import sys

modulePath = path.abspath(path.join(path.dirname(__file__), '../src'))
sys.path.append(modulePath)
sys.path.append(path.abspath(path.dirname(__file__)))