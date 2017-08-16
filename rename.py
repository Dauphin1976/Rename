#! python3
# Renames files and directories

import os, sys, shutil, shelve, re

# test case directory - temporary! Remove from finished program!
os.chdir('!testCases')

print('The current Directory is :\n' + str(os.getcwd()))
itemsToRename = os.listdir(os.getcwd())
print('\nThe current list is :\n' + str(itemsToRename))

regex = re.compile('[-_.]+')

# Rename files and directores 
for items in itemsToRename:
	# Checks if item is file or directory
	if os.path.isfile(items) == True:
		# Removes file extension so Regex will work
		items = os.path.splitext(items)[0]
		if '[-_.]+'.test(items) == False:
			continue
		else:
			regexSplit = re.split('[-_.]+', items)
			newName = ' '.join(regexSplit)
			print(newName)
			os.rename(items, newName)
	elif os.path.isdir(items) == True:
		continue
		print('----')
		print(items)
		print(dirform.findall(items))
	else:
		continue
