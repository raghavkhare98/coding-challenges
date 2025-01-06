import os
import sys
import argparse

def cFlag(fileName=None):
            
    try:
        if fileName:
            
            fileStats = os.stat(fileName)
            print(f'{fileStats.st_size}', end=" ")
            
        else:
            data = sys.stdin.read()
            lineCount = data.count("\n")
            print(f'{lineCount}')
            
    except Exception as e:
        
        print("Please provide the correct file path")

    

def lFlag(fileName=None):
    
    try:        
        count = 0

        if fileName:
            
            with open(f'{fileName}', "rb") as f:
                for i, _ in enumerate(f):
                    count += 1
            print(count, end=" ")

        else:

            data = sys.stdin.read()
            for i, _ in enumerate(data):
                count += 1
            print(count)
            
            
    
    except Exception as e:
        
        return "File Not found. Please provide the correct file path"

def wFlag(fileName=None):
    
            
    try:
        
        if fileName:

            with open(f'{fileName}', 'r') as f:
                for i in f:
                    wordCount = len(i.split())
            print(wordCount, end=" ")
            

        else:

            data = sys.stdin.read()
            wordCount = len(data.split())
            print(wordCount) 
    
    except Exception as e:
        
        return "File Not found. Please provide the correct file path"

def mFlag(fileName=None):

    charCount = 0

    try:
        
        if fileName:
            
            with open(f'{fileName}', 'r', encoding="UTF-8") as f:
                for i in f:
                    charCount += len(i)

            print(charCount, end=" ")

        else:
            
            data = sys.stdin.read()
            for i in data:
                charCount += len(i)
            
            print(charCount, end=" ")
                
    except Exception as e:
        return "File Not found. Please provide the correct file path"


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action="store_true")
    parser.add_argument('-l', action="store_true")
    parser.add_argument('-w', action="store_true")
    parser.add_argument('-m', action="store_true")

    parser.add_argument("files", nargs="*")

    args = parser.parse_args()

    if not(args.c or args.l or args.w or args.m):

        args.m = args.l = args.c = True
        

    if not args.files:
        
        fileName = None
    
    else:

        fileName = args.files

    for file in fileName:

        if args.c:
            cFlag(file)
            print(file)
        if args.l:
            lFlag(file)
            print(file)
        if args.m:
            mFlag(file)
            print(file)
        if args.w:
            wFlag(file)
            print(file)

if __name__ == "__main__":
    main()