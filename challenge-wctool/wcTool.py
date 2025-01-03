import os
import sys
import argparse

class CAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        
        if os.path.exists(values[0]):
            fileStats = os.stat(values[0])
            print(f'{fileStats.st_size}', end=" ")
            print(f'{values[0]}')
            # setattr(namespace, self.dest, fileStats.st_size, values[0])
        else:
            print("Please provide the correct file path")
            
parser = argparse.ArgumentParser() #this will help us in commandline flags

parser.add_argument('-c', action=CAction, nargs=1)
args = parser.parse_args(["-c", sys.argv[2]])