import os
import sys
import argparse

def cFlag(fileName):
    
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

def lFlag(fileName):
    
    class LAction(argparse.Action):

        def __call__(self, parser, namespace, values, option_string=None):
            
            if os.path.exists(fileName):
        
                count = 0
                with open(f'{fileName}', "rb") as f:
                    for i, _ in enumerate(f):
                        count += 1
                print(count, end=" ")
                print(f'{values[0]}') 
            
            else:
                return "File Not found. Please provide the correct file path"
        
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', action=LAction, nargs=1)
    parser.parse_args(["-l", sys.argv[2]])

def wFlag(fileName):
    
    class WAction(argparse.Action):

        def __call__(self, parser, namespace, values, option_string=None):
            
            if os.path.exists(fileName):
        
                wordCount = 0
                wordList = []
                with open(f'{fileName}', 'r') as f:
                    for i in f:
                        wordList.append(i.split())
                for i in wordList:
                    wordCount += len(i)
                print(wordCount, end=" ")
                print(f'{values[0]}') 
            
            else:
                return "File Not found. Please provide the correct file path"
        
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', action=WAction, nargs=1)
    parser.parse_args(["-w", sys.argv[2]])    

if sys.argv[1] == '-c':
    cFlag(sys.argv[2])
elif sys.argv[1] == "-l":
    lFlag(sys.argv[2])
elif sys.argv[1] == "-w":
    wFlag(sys.argv[2])

    

