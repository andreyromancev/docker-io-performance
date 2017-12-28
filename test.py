import os
import time

FILES_FOLDER = 'files/'
ITERATIONS = 50000
LINES = 1000

def write_file(index):
	with open(FILES_FOLDER + 'file{}.txt'.format(index), 'w') as f:
		for i in range(0, LINES):
			f.write('I am the test file!')

def read_file(index):
	with open(FILES_FOLDER + 'file{}.txt'.format(index), 'r') as f:
		f.read()

def delete_file(index):
	os.remove(FILES_FOLDER + 'file{}.txt'.format(index))


def test():
	start = time.time()
	for i in range(0, ITERATIONS):
		write_file(i)
		read_file(i)
		delete_file(i)

	print('Process time: {} seconds'.format(time.time() - start))


test()
