import os
import difflib

#list of all the directories with input file in them
dirs = ['','','','','','','','']
dirs[0] = r'.\tests\01_pre_wit_test_1_r'
dirs[1] = r'.\tests\02_pre_wit_test_3_r'
dirs[2] = r'.\tests\03_pre_wit_test_7_r'
dirs[3] = r'.\tests\04_wit_1_as_built'
dirs[4] = r'.\tests\05_wit_2_as_built'
dirs[5] = r'.\tests\06_wit_3_design_rev_4'
dirs[6] = r'.\tests\07_wit_4_unbalanced_as_built'
dirs[7] = r'.\tests\08_complex_system'

exeFile = '70barSapphire.exe'
newCalcEngineFolder = r'.\tests\new_calc_engine\\'
oldCalcEngineFolder = r'.\tests\old_calc_engine\\'

def compare(newResults,oldResults,comparison):
    with open(newResults,'r') as f:
        #newR=set(f.readlines())
        newR = f.readlines()

    with open(oldResults,'r') as f:
        #oldR=set(f.readlines())
        oldR = f.readlines()

    with open(comparison,'a') as f:
        f.write('\n\n\n=====================================================\n\n')
        f.write(newResults+'\n')
        f.write(oldResults+'\n')
        f.write(comparison+'\n\n')
        #for line in list(newR-oldR):
        #       f.write(line)
        for line in difflib.unified_diff(newR, oldR, fromfile=newResults, tofile=oldResults, lineterm=''):
                f.write(line+'\n')           

#Copies the input file from test_dir to the folders containing old and new calculation engines
#then runs the calculation engines and moves the results back the directory where the input file was
#then cleans up the directories containing calculation engines.
def runCalcs(test_dir):
        copyCommandNew = 'xcopy /Y /f ' + test_dir + r'\TEMPINPUT.TMP ' + newCalcEngineFolder
        copyCommandOld = 'xcopy /Y /f ' + test_dir + r'\TEMPINPUT.TMP ' + oldCalcEngineFolder
        execCommandNew = newCalcEngineFolder + exeFile
        execCommandOld = oldCalcEngineFolder + exeFile
        moveCommandNew = r'move /Y ' + newCalcEngineFolder +'ResultsOut.tmp ' + test_dir + r'\ResultsOut_new.tmp'
        moveCommandOld = r'move /Y ' + oldCalcEngineFolder +'ResultsOut.tmp ' + test_dir + r'\ResultsOut_old.tmp'
        deleteCommandNew = r'del '+ newCalcEngineFolder + 'TEMPINPUT.TMP'
        deleteCommandOld = r'del '+ oldCalcEngineFolder + 'TEMPINPUT.TMP'
        os.system(copyCommandNew)
        os.system(copyCommandOld)
        os.system(execCommandNew)
        os.system(execCommandOld)
        os.system(moveCommandNew)
        os.system(moveCommandOld)
        os.system(deleteCommandNew)
        os.system(deleteCommandOld)

#main part of the program, first create a file to store the differences between files. we
#only create the file here and in the loop we append the results for each input file to the
#same comparison file.
comp = r'.\tests\comparison.txt'
open(comp,'w').close() #Create the file
allOlds = 'allOldResults.txt' 
allNews = 'allNewResults.txt'

#loop through all the directories, run the calcs and compare the results.
for directory in dirs:
        runCalcs(directory)
        newResult = directory+r'\ResultsOut_new.tmp'
        oldResult = directory+r'\ResultsOut_old.tmp'
        compare(newResult,oldResult,comp)
        pass

#create a file including all the old results
with open(allOlds, 'w') as outfile:
        for directory in dirs:
                fname = directory+r'\ResultsOut_old.tmp'
                outfile.write('\n\n============================================\n')
                outfile.write('\n'+fname+'\n')
                with open(fname) as infile:
                        for line in infile:
                                outfile.write(line)

#create a file containing all the new results
with open(allNews, 'w') as outfile:
        for directory in dirs:
                fname = directory+r'\ResultsOut_new.tmp'
                outfile.write('\n\n============================================\n')
                outfile.write('\n'+fname+'\n')
                with open(fname) as infile:
                        for line in infile:
                                outfile.write(line)


#comparison between allNewResults.txt and allOldResults.txt can be done using this website:
#http://gerhobbelt.github.io/google-diff-match-patch/demos/demo_diff.html