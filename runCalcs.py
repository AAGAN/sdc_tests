from os import listdir, mkdir, startfile
from os.path import isfile, join
import re
import shutil

mypath = r'C:\SoftwareDevelopment\GSI'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
try:
    shutil.rmtree('C:\\SoftwareDevelopment\\GSI\\folders')
except:
    print('no folders directory')

mkdir('C:\\SoftwareDevelopment\\GSI\\folders')
for file in onlyfiles:
    # print(file)
    folderName = str(file).split(sep='.')[0]
    mkdir('C:\\SoftwareDevelopment\\GSI\\folders\\'+folderName)
    shutil.copy('C:\\SoftwareDevelopment\\GSI\\'+str(file),'C:\\SoftwareDevelopment\\GSI\\folders\\'+folderName+'\\TempInput.tmp')
    shutil.copy('C:\\SoftwareDevelopment\\GSI\\70bar\\PipeSapphire.flo','C:\\SoftwareDevelopment\\GSI\\folders\\'+folderName+'\\PipeSapphire.flo')
    shutil.copy('C:\\SoftwareDevelopment\\GSI\\70bar\\Sapphire70bar.exe','C:\\SoftwareDevelopment\\GSI\\folders\\'+folderName+'\\Sapphire70bar.exe')
    try:
        startfile('C:\\SoftwareDevelopment\\GSI\\folders\\'+folderName+'\\Sapphire70bar.exe')
    except:
        print('Issue running C:\\SoftwareDevelopment\\GSI\\folders\\'+folderName)

onlyfolders = [f for f in listdir(mypath+'\\folders\\')]
for folder in onlyfolders:
    if ('ResultsOut.tmp' not in listdir(mypath+'\\folders\\'+folder)):
        print(folder)