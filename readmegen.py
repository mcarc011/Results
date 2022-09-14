#%%
import os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

L = [i.split('\\')[-2]+'/'+i.split('\\')[-1] for i in getListOfFiles(os.getcwd()+'\\figs')]
f = open("read.txt",'w')
model = ''
for i in L:
    m = i.split('/')[0]
    if model !=m:
        f.write('\n\n##Model '+m[-1]+'##\n')
        model = m
        f.write('\nUnique Toric Phases:\n')
    if 'Tweb' in i and 'A' in i:
        tdata = i.split('_')
        d1,d2 = i.index('('),i.index(')')
        data = i[d1:d2+1]
        try:
            data = '('+str(int(data[1])+1)+','+str(int(data[-2])+1)+')'
        except:
            pass
        direction = 'Triality: '
        if '-' in tdata[0]:
            direction = 'Inverse Triality: '
        f.write('\n\n Phases: '+data + direction + str(int(tdata[-1][-5])+1)+'\n')
    f.write('\n<img src="./figs/'+i+'" width="100" height="100">')
        
f.close()


# %%
