import os
import time
import random
 
FILES_FOLDER = 'files/'
ITERATIONS = 100000
LINES = 1000
 
SIZE = 100*1024*1024
 
 
def init_file():
        with open(FILES_FOLDER + 'file.txt', 'w') as f:
                f.write("x"*SIZE)
               
def write_file():
        with open(FILES_FOLDER + 'file.txt', 'w') as f:
                offset = random.randint(0, SIZE-10)
                f.seek(offset, 0)
                f.write('qwert')
 
def read_file():
        with open(FILES_FOLDER + 'file.txt', 'r') as f:
                offset = random.randint(0, SIZE-10)
                f.seek(offset, 0)
                f.read(5)
 
def test():
        start = time.time()
        init_file()
        for i in range(0, ITERATIONS):
                write_file()
                read_file()
        print('Process time: {} seconds'.format(time.time() - start))
 
test()
