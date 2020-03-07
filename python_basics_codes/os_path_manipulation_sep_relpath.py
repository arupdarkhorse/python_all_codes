import os, sys
curpath = os.path.dirname(__file__)
#head_tail_path = os.path.split(curpath)     # splitting path
#os.path.relpath(curpath, os.environ['HOME'])    # finding relative path
#print(os.path.pardir(curpath))
#sys.executable    # print the location of python installed
#print(os.__builtins__)
#print(os.__doc__)
#print(os.pardir)
# moving back to parent directory and navigating other path
print(os.path.join(os.path.abspath(os.path.join(curpath,os.pardir))),"dir2/subdir2/file2.txt")