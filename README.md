# Aman Tiwari

> aman.tiwari2015@vit.ac.in

## How To Run

Use Pycharm or IDLE (Python > 3 with tkinter installed) & Run file “GUI.py”.


## Special Features:

 - •	Undo Feature 
•	Exception Handling in GUI as well as in backend
•	Custom Directory Selection For organizing any directory as required 	 (Option)
•	Platform Independence (Linux, Windows)
•	Graphical User Interface


# Description & Screenshots:

## •	Finding Top 10 System Files - 

There were various methods of finding 10 biggest files on system but for obvious reasons we want to reduce the time delay as it will already take time for traversing all directories and files. Thus, I used “Min Heap” as Data Structure with capacity of 10. Every time a file is chosen, its size is compared with the minimum size in Heap, if min(heap) < current file size then replaces the minimum value with current file size. Similarly, the heap property is maintained and at the end of full system traversal we get only the top 10 largest values and all the small size values are popped out.
Exception Handling has been taken care of for system files that are read only protected in case the script is not run as administrator. 
This process will take some time depending upon the processor (As Full system Scan is in process)
windows 10 takes less time than linux (because linux have highly scattered small size system files in root directory)
Time Complexity: **O(Log(N))**
![System Scan](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/d.PNG)

![Results](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/2.png)

## •	Organize Desktop chunk of Files In Documents (Excluding Special Files)-
This feature doesn't allow UNDO feature, while the organizing property remains same and the files are moved to "Documents" folder
![enter image description here](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/desktop.PNG)
![enter image description here](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/documents.PNG)

## •	Organize Desktop chunk of Files On Same Location (Excluding Special Files)-

For chunk of files placed on Desktop, the given script organize them in respective folders based on their extensions, however the files like shortcut icons should not be touched.
Also, there are some file that doesn’t have any extension and are considered as “File” type, similarly such files are grouped together and organized in a “Misc” folder.
![Unorganized Desktop](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/g.JPG)
![Organized Desktop](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/h.JPG)

## •	Organize any Given Custom Directory –

This Features works as previous one but with an option of organizing any custom directory instead of desktop only.
![enter image description here](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/customM.JPG)
![enter image description here](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/a.PNG)
![enter image description here](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/b.PNG)
## •	Organize Pictures/Images with Date Modified for Easier Access –

We all know that images or pictures in the system or not well organized they have some defined file name like “DSC-0001” etc. we find it difficult when we want to search or access a particular picture we want in a directory full of thousands of images.
My proposed idea is to organize the whole directory with “Date Created Or Date modified”, for just sample I have taken “Date modified” as the separating factor. So all the image/pictures are organized with “Year-Month” folder name. Thus it becomes easy for use now to navigate to that particular Year & month folder and get the corresponding file that we want.

**NOTE:**  This feature also works with all file types. Not necessarily for only Images. Only because the such organizing mechanism helps in case of pictures, I have given it name of Organize Pictures.

![Images Folder](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/5.png)

![With Date Modified Organize](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/7.png)
## •	Undo Feature

This Feature is one of the most important & helpful feature in any software where user has control of the software. If the user finds that software script has done something that is not as desired that he or she can revert all the action that has been taken by the script.

![Before Organize](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/8.png)

![After Organize](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/9.png)

![After Undo Action](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/10.png)
## •	GUI

A simple GUI has been built on top of the backend for ease of the naïve user. UI is not having any out of the box features, but it is having basic UI features like:
•	“Undo” Button is By Default “Disabled”.
•	“Undo” Button is enabled when any action is taken like organize.
•	Radio Button to choose between “Desktop” or “Custom” directory.
•	When any one option between “organize everything” & “organize by date modified” is selected the other one will be disabled, (obviously) other will be of no use now. However, both can be enabled back if “Undo” is clicked.

![Undo Disabled](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/d.PNG)![Organize option Disabled](https://raw.githubusercontent.com/tiwari85aman/AssignmentOrganizer/master/Images/f.JPG)
