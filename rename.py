#! python3
# Renames files and directories

import os, sys, shutil, shelve, re

# test case directory - temporary! Remove from finished program!
os.chdir('!testCases')

print('The current Directory is :\n' + str(os.getcwd()))
itemsToRename = os.listdir(os.getcwd())
print('\nThe current list is :\n' + str(itemsToRename))

# Regex for files and directories
docform = re.compile(r'''
	(\w+)		# text items
	([-_.]+)	# separators
	(\w+)		# text items
	''', re.VERBOSE)
dirform = re.compile(r'''
	(\w+)		# text items
	([-_.]+)	# separators
	''', re.VERBOSE)
	
# Rename files and directores 
for items in itemsToRename:
	# Checks if item is file or directory
	if os.path.isfile(items) == True:
		# Removes file extension so Regex will work
		items = os.path.splitext(items)[0]
		print('----')
		print(items)
		print(docform.findall(items))
		#~ os.rename(items, a)
	elif os.path.isdir(items) == True:
		continue
		print('----')
		print(items)
		print(dirform.findall(items))
	else:
		continue
