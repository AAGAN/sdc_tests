import os
import difflib

rootdir = 'C:/Users/aahma/Desktop/SDC_Tests'

dirs = ['','','','','','','']
dirs[0] = r'.\tests\01_pre_wit_test_1_r'
dirs[1] = r'.\tests\02_pre_wit_test_3_r'
dirs[2] = r'.\tests\03_pre_wit_test_7_r'
dirs[3] = r'.\tests\04_wit_1_as_built'
dirs[4] = r'.\tests\05_wit_2_as_built'
dirs[5] = r'.\tests\06_wit_3_design_rev_4'
dirs[6] = r'.\tests\07_wit_4_unbalanced_as_built'

exeFile = '70barSapphire.exe'

def compare(newResults,oldResults,comparison):
    with open(newResults,'r') as f:
        #newR=set(f.readlines())
        newR = f.readlines()

    with open(oldResults,'r') as f:
        #oldR=set(f.readlines())
        oldR = f.readlines()

    #open(comparison,'w').close() #Create the file

    with open(comparison,'a') as f:
        f.write('\n\n\n=====================================================\n\n')
        f.write(newResults+'\n')
        f.write(oldResults+'\n')
        f.write(comparison+'\n\n')
        #for line in list(newR-oldR):
        #       f.write(line)
        for line in difflib.unified_diff(newR, oldR, fromfile=newResults, tofile=oldResults, lineterm=''):
                #print(line)
                f.write(line+'\n')
                pass
           

def main():
    for subdir, dirs, files in os.walk(rootdir):
        for directory in dirs:
            print(subdir, files, directory)

def runCalcs(test_dir):
        copyCommandNew = 'xcopy /Y ' + test_dir + r'\TEMPINPUT.TMP' + r' .\tests\new_calc_engine'
        copyCommandOld = 'xcopy /Y ' + test_dir + r'\TEMPINPUT.TMP' + r' .\tests\old_calc_engine'
        execCommandNew = '.\\tests\\new_calc_engine\\' + exeFile
        execCommandOld = '.\\tests\\old_calc_engine\\' + exeFile
        moveCommandNew = r'move /Y .\tests\new_calc_engine\ResultsOut.tmp ' + test_dir + r'\ResultsOut_new.tmp'
        moveCommandOld = r'move /Y .\tests\old_calc_engine\ResultsOut.tmp ' + test_dir + r'\ResultsOut_old.tmp'
        deleteCommandNew = r'del .\tests\new_calc_engine\TEMPINPUT.TMP'
        deleteCommandOld = r'del .\tests\old_calc_engine\TEMPINPUT.TMP'
        os.system(copyCommandNew)
        os.system(copyCommandOld)
        os.system(execCommandNew)
        os.system(execCommandOld)
        os.system(moveCommandNew)
        os.system(moveCommandOld)
        os.system(deleteCommandNew)
        os.system(deleteCommandOld)

comp = r'.\tests\comparison.txt'
open(comp,'w').close() #Create the file
for directory in dirs:
        runCalcs(directory)
        newResult = directory+r'\ResultsOut_new.tmp'
        oldResult = directory+r'\ResultsOut_old.tmp'
        compare(newResult,oldResult,comp)
        pass
