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

def main():
    for subdir, dirs, files in os.walk(rootdir):
        for directory in dirs:
            print(subdir, files, directory)

dirs = ['','','','','','','']
dirs[0] = r'.\tests\01_pre_wit_test_1_r'
dirs[1] = r'.\tests\02_pre_wit_test_3_r'
dirs[2] = r'.\tests\03_pre_wit_test_7_r'
dirs[3] = r'.\tests\04_wit_1_as_built'
dirs[4] = r'.\tests\05_wit_2_as_built'
dirs[5] = r'.\tests\06_wit_3_design_rev_4'
dirs[6] = r'.\tests\07_wit_4_unbalanced_as_built'

def runCalcs(test_dir):
        copyCommandNew = 'xcopy /Y ' + test_dir + r'\TEMPINPUT.TMP' + r' .\tests\new_calc_engine'
        copyCommandOld = 'xcopy /Y ' + test_dir + r'\TEMPINPUT.TMP' + r' .\tests\old_calc_engine'
        execCommandNew = r'.\tests\new_calc_engine\70barSapphire.exe'
        execCommandOld = r'.\tests\old_calc_engine\70barSapphire.exe'
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


for directory in dirs:
        runCalcs(directory)