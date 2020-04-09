"""

For this problem, the goal is to write code for finding all files 
under a directory (and all directories beneath it) that end with ".c"

./testdir
./testdir/subdir1
./testdir/subdir1/a.c  <----------
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c  <-----------------
./testdir/t1.h

"""

import os


def file_recursion(suffix, path, files=[]):
	# get full path: suffix/path/file
	if path:
		suffix = os.path.join(suffix, path)
	for item in os.listdir(suffix):
		full_path = os.path.join(suffix, item)
		if os.path.isfile(full_path) and full_path.endswith(".c"):
			files.append(full_path)
		elif os.path.isdir(full_path):
			# recurse into next directory
			files = file_recursion(suffix, item, files)

	return files


files = file_recursion(".", "testdir")
print([x for x in files])