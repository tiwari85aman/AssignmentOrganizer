#author: aman tiwari
#contact: 8428941096, tiwari.aman85@gmail.com, aman.tiwari2015@vit.ac.in


import os,datetime,shutil
import platform
from tkinter import filedialog

directory="NULL"
if(platform.system()=='Windows'):
    directory = os.path.abspath('C://Users//Aman Tiwari//Desktop//')
else:
    directory = os.path.abspath('//home//aman//Desktop//')

def setChoice(choice):
    global directory
    if(choice==1):
        directory=directoryDialog()
    else:
        print("Default Directory Selected (Desktop)")



#Keep track of changes done on the Directory
prevState={}
folderCreated={}

#Directory Selection Dialog Box
def directoryDialog():
    directoryGiven = filedialog.askdirectory(initialdir='.')    
    return directoryGiven

#Move the file to assigned Folder & Keeps track of created Folder
def movFileToFolder(filename,folder,source,directorySeparator):
    global folderCreated
    folderCreated[folder]='new'
    if not os.path.exists(folder):
        os.makedirs(folder)
    destination=folder+directorySeparator+filename
    
    os.rename(source,destination)

#Organize Desktop Based on Extension Names
def organiseDesktop(everythingButton,byDateButton,undoButton):
    print(directory)
    # Disable the Buttons Pressed In GUI
    everythingButton.config(state='disabled')
    byDateButton.config(state='disabled')
    # Enable the Undo Button
    undoButton.config(state='normal')

    #save the current State of the directory to use this info if in case UNDO is required
    global prevState
    prevState=currentState()

    #iterate through each file in the current directory
    for filename in os.listdir(directory):
            fileSource=os.path.join(directory,filename)
            if(os.path.isdir(fileSource)):
                continue
            #getting current file extension
            currFileExt=os.path.splitext(filename)[1][1:]
            if(platform.system()=='Windows'):
                directorySeparator='\\'
            else:
                directorySeparator='//'

            #Exclude shortcut icons in the given directory
            if(currFileExt!='lnk'):
                if(currFileExt==''):
                    assignedFolder=directory+directorySeparator+'File(Misc)'
                else:
                    assignedFolder=directory+directorySeparator+currFileExt
                movFileToFolder(filename,assignedFolder,fileSource,directorySeparator)
                #print (fileSource)
            
    

#Organize Directories with Date Modified (e.g. IMAGES / Pictures)
def organiseDesktopByDate(everythingButton,byDateButton,undoButton):
    #Disable the Buttons Pressed In GUI
    everythingButton.config(state='disabled')
    byDateButton.config(state='disabled')
    # Enable the Undo Button
    undoButton.config(state='normal')

    #saving current state
    global prevState
    prevState = currentState()
    #organize by Date Modified
    for filename in os.listdir(directory):
            fileSource=os.path.join(directory,filename)
            if(os.path.isdir(fileSource)):
                continue
            currFileExt=os.path.splitext(filename)[1][1:]
            if(platform.system()=='Windows'):
                directorySeparator='\\'
            else:
                directorySeparator='//'
                
            if(currFileExt!='lnk'):
                date = datetime.datetime.fromtimestamp(os.path.getmtime(fileSource))
                assignedFolder = directory + directorySeparator + str(date.year)+'-'+str(date.month)
                #print(filename)
                movFileToFolder(filename,assignedFolder,fileSource,directorySeparator)


#Fetch current State of the Directory
def currentState():
    files={}
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            fileSource=os.path.join(root,filename)
            files[filename]=fileSource
    return (files)

#Undo Changes Made by the program by using the track record(Or History).
def undoChanges(undoButton,everythingButton,byDateButton):
    #Disable the Undo Button Pressed In GUI
    undoButton.config(state='disabled')
    # Enable the other two Button In GUI
    everythingButton.config(state='normal')
    byDateButton.config(state='normal')

    newState=currentState()
    for key, prevLocation in prevState.items():
        os.rename(newState[key],prevLocation)
    global folderCreated
    #delete all newly created folder
    for key in folderCreated.keys():
        shutil.rmtree(key)
    folderCreated={}

#author: aman tiwari
#contact: 8428941096, tiwari.aman85@gmail.com, aman.tiwari2015@vit.ac.in


