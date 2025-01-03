import os

fileName = "test.txt"

fileStats = os.stat(fileName)

print(f'File size in Bytes: {fileStats.st_size}')