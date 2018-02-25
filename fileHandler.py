import os,datetime,shutil
import platform
from tkinter import filedialog
from os.path import expanduser


directory="NULL"
home = expanduser("~")

if(platform.system()=='Windows'):
    directory = os.path.abspath(home+'\\Desktop\\')
else:
    directory = os.path.abspath(home+'/Desktop/')

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
    print(destination)
    os.rename(source,destination)

inDocument=0
def organiseDesktopInDocuments(everythingButton,everythingInDocumentButton,byDateButton,undoButton):
    global inDocument
    inDocument=1
    organiseDesktop(everythingButton,everythingInDocumentButton,byDateButton,undoButton)

#Organize Desktop Based on Extension Names
def organiseDesktop(everythingButton,everythingInDocumentButton,byDateButton,undoButton):
    print(directory)
    # Disable the Buttons Pressed In GUI
    everythingInDocumentButton.config(state='disabled')
    everythingButton.config(state='disabled')
    byDateButton.config(state='disabled')


    #save the current State of the directory to use this info if in case UNDO is required
    global prevState
    global inDocument
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
                directorySeparator='/'

            #Exclude shortcut icons in the given directory
            if(inDocument==1):
                if(platform.system()=='Windows'):
                    finalDirectory=home+"\\Documents"
                else:
                    finalDirectory=home+"/Documents"
            else:
                finalDirectory=directory
                # Enable the Undo Button
                undoButton.config(state='normal')

            if(currFileExt!='lnk'):
                if(currFileExt==''):
                    assignedFolder=finalDirectory+directorySeparator+'File(Misc)'
                else:
                    assignedFolder=finalDirectory+directorySeparator+currFileExt
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
    print(prevState)
    #organize by Date Modified
    for filename in os.listdir(directory):
            fileSource=os.path.join(directory,filename)
            if(os.path.isdir(fileSource)):
                continue
            currFileExt=os.path.splitext(filename)[1][1:]
            if(platform.system()=='Windows'):
                directorySeparator='\\'
            else:
                directorySeparator='/'
                
            if(currFileExt!='lnk'):
                date = datetime.datetime.fromtimestamp(os.path.getmtime(fileSource))
                assignedFolder = directory + directorySeparator + str(date.year)+'-'+str(date.month)
                #print(filename)
                movFileToFolder(filename,assignedFolder,fileSource,directorySeparator)


#Fetch current State of the Directory
def currentState():
    files={}
    print(directory)
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            fileSource=os.path.join(root,filename)
            if(os.path.isdir(fileSource)):
                continue
            files[filename]=fileSource
    return (files)

#Undo Changes Made by the program by using the track record(Or History).
def undoChanges(undoButton,everythingButton,everythingInDocumentButton,byDateButton):
    #Disable the Undo Button Pressed In GUI
    undoButton.config(state='disabled')
    # Enable the other two Button In GUI
    everythingInDocumentButton.config(state='normal')
    everythingButton.config(state='normal')
    byDateButton.config(state='normal')

 
    newState=currentState()
    print(newState)
    for key, prevLocation in prevState.items():
        print(newState[key])
        os.rename(newState[key],prevLocation)
    global folderCreated
    #delete all newly created folder
    for key in folderCreated.keys():
        shutil.rmtree(key)
    folderCreated={}
