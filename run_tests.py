import os
rootdir = 'C:/Users/aahma/Desktop/SDC_Tests'



def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())


    with open(File2,'r') as f:
        e=set(f.readlines())

    open('file3.txt','w').close() #Create the file

    with open('file3.txt','a') as f:
        for line in list(d-e):
           f.write(line)

for subdir, dirs, files in os.walk(rootdir):
    for directory in dirs:
        print(directory)
        
