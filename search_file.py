import os
import sys
import fnmatch
search_string=str(sys.argv[2])   #take string to search from command line
print('Searching word....',search_string)
filetypes = ['*.py','*.txt','*.c','*.cpp','*.m']            #specify file type to search
this_file=os.path.realpath(__file__).split('/')[-1]
path = sys.argv[1]

def found_in_file(root,filename, search_string):
	with open(root+filename) as search_file:
		for line in search_file:
			if search_string in line:
				return True
		return False

for root,dirs,files in os.walk(path):
	print('------------------------------------------------------------------------')
	print('Location:',root)
	print('Directories present inside:',dirs)
	print('Files are :',files)
	for extension in tuple(filetypes):
		for filename in fnmatch.filter(files, extension): #allow only files with extension mentioned above
			if(filename==this_file):
				break
			print(filename)
			root+='/'
			if found_in_file(root,filename, search_string):
				print('%s STRING FOUND IN: %s'%(search_string,filename))
			else:
				print('NOT FOUND')
			print('------------------------------------------------------------------------')

