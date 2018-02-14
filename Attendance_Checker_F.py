##GUI.py authored by Jeremy Micah Choa

#This is a course requirement for CS 192 Software Engineering under the
#supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of
#Computer Science, College of Engineering, University of the Philippines,
#Diliman for the AY 2016-2017.

#Version 1.3 (May 8, 2017) by Jeremy Micah Choa
# - jumpTo no longer accepts session number 0 or below
# - "Indefinite" class session length is now represented as 
# ---- Ellipsis instead of -1
# - prevSession now checks if currentSession is not negative 
# ---- instead of not equal to 0
# - doUpload now returns an error if the class's name is already
# ---- in use

#Version 1.2 (Mar. 24, 2017) by Jeremy Micah Choa
# - added file checking to doUpload, should now check if file follows
# ---- proper format
# - added instructions on how to upload the class record files in the
# ---- upMenu window
# - added icons for View Class, Next/Prev Session, Present and Absent
# - added error messages for going out of bounds when pressing
# ---- Present!, Absent!, and Jump to Session

#Version 1.1.8 (Mar. 13, 2017) by Jeremy Micah Choa
# - added a "Jump to Session" entry that allows user to jump
# ---- to a particular session
# - finally reenabled the viewMenu function, displays the class data in a
# ---- separate window
# - added viewTrigger to make viewMenu display class data properly
# - toggleButton adjusted, it only works on the main menu now

#Version 1.1.7 (Feb. 17, 2017) by Jeremy Micah Choa
# - fixed setPresent to refer to the objects themselves rather than
#   the strings being displayed in the GUI
# - fixed setPresent to change the attendance in the currently viewed session
#   rather than the lastest session
# - added read_on_startup and setAbsent and checkAbsent

#Version 1.1.5 (Feb. 17, 2017) by Faneallrich Li Yao
# - fixed the error prompt when user enters 0 in class sessions when uploading
#   classes

#Version 1.1 (Feb. 6, 2017) by Jeremy Micah Choa
# - added nextSession and previousSession buttons
# - made widget alignments more uniform
# - enabled file reading

#Version 1.0 (Jan. 28, 2017) by Jeremy Micah Choa

#File created on Jan. 28, 2017
#Developed by Team 6 Absences
#Developed for teachers and instructors everywhere (we hope)
#This is the file that represents the GUI that Attendance Checker will use.

#Version 2.0 (Feb 13, 2017) by Robelle Silverio
# - remove some intructions in "up" subwindow under def upMenu
# - added "See .csv file's content format" button in "up" subwindow under def upMenu
# - added "See .csv file's content format" button's functionality (viewquemark)
# - edited "view" subwindow

from appJar import gui
from AttendanceChecker import *
from random import randint
import os.path
import Tkinter
Tkinter.wantobjects = False

#pressUpload
#created Jan. 28, 2017
# - adds a class to the list of classes, then calls updateClassNames
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Upload Class, no return values
# - needs the following to work:
# ----- the appJar library
# ----- updateClassNames and its requirements
# ----- the file AttendanceChecker.py
def pressUpload(btn):
     print(btn)
     main.showSubWindow("up")

#setI
#created Jan. 31, 2017
# - disables entry for "Number of Sessions:" in the Upload Class subwindow
#   when the "Indefinite" option is checked
# - needs the following to work:
# ----- the appJar library
def setI(btn):
    global signal
    main.disableEntry("Number of sessions:")
    signal += 1
    if signal == 2:
        signal = 0
        main.enableEntry("Number of sessions:")

#Cancel
#created Jan. 31, 2017
# - hides the Upload Class subwindow
# - initialize every entry and the tick box to empty before closing the window
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Cancel, no return values
# - needs the following to work:
# ----- the appJar library
def Cancel(btn):
     print(btn)
     #clear everything for next use
     main.clearAllEntries()
     #untick check box for next use
     main.setCheckBox("Indefinite",False)
     main.hideSubWindow("up")

#doUpload
#created Jan. 31, 2017
# - retrieves the user-inputted data from the Upload Class subwindow,
#   then passes it to the AddClass function
# - indefinite number of sessions is -1
# - lots of error checking involved
# - upon successful uploading of class or cancellation, the entry fields are
#   cleared and the Upload Class subwindow is closed
# - also upon successful uploading of class, updateClassNames is called
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Upload Class, no return values
# - needs the following to work:
# ----- the appJar library
# ----- the file AttendanceChecker.py for function AddClass
def doUpload(btn):
     err_check = 0
     tempN = main.getEntry("Name of class:")
     tempS = main.getCheckBox("Indefinite")
     tempF = main.getEntry("Class record file:")
     if tempN == "":
          main.errorBox("Error","Please enter a name for your class.")
     else:
          if tempS == False:
               tempS = main.getEntry("Number of sessions:")
               if (tempS == "" or tempS.isdigit() == False):
                    main.errorBox("Error","Please enter how many sessions your\nclass will run for.")
               elif int(tempS) < 1:
                    main.errorBox("Error","Please enter a positive value for your sessions.")
               else:
                    if tempF == "":
                         main.errorBox("Error","Please enter a file of your class record.")
                    else:
                         if os.path.isfile(tempF) == False:
                              main.errorBox("Error","That file doesn't exist.")
                         elif (tempF[-4:] != ".csv"):
                              main.errorBox("Error","The file must be a .csv file.")
                         else:
                              errcheck = AddClass(classes,tempN,tempS,tempF)
                              #success
                              if errcheck == 0:
                                   main.infoBox("success","Your class has been uploaded!")
                                   main.clearAllEntries()
                                   main.hideSubWindow("up")
                                   main.showButton("View Class")
                                   updateClassNames()
                                   main.updateListItems("classData",[])
                              elif errcheck == 1:
                                   main.errorBox("Error","Your file contains a student with a blank ID.")
                              elif errcheck == 2:
                                   main.errorBox("Error","Your file has more than 3 columns in it.")
                              elif errcheck == 3:
                                   main.errorBox("Error","Your file contains students with duplicate IDs.")
                              elif errcheck == 4:
                                   main.errorBox("Error","There is already a class with the same name as this one.\nPlease choose a different name.")
          #they chose indefinite
          else:
               tempS = Ellipsis
               if tempF == "":
                    main.errorBox("Error","Please enter a valid file of your class record.")
               else:
                    if os.path.isfile(tempF) == False:
                         main.errorBox("Error","That file doesn't exist.")
                    elif (tempF[-4:] != ".csv"):
                         main.errorBox("Error","The file must be a .csv file.")
                    else:
                         errcheck = AddClass(classes,tempN,tempS,tempF)
                         #success
                         if errcheck == 0:
                              main.infoBox("success","Your class has been uploaded!")
                              main.clearAllEntries()
                              main.hideSubWindow("up")
                              main.showButton("View Class")
                              updateClassNames()
                              main.updateListItems("classData",[])
                         elif errcheck == 1:
                              main.errorBox("Error","Your file contains an entry with a blank ID.")
                         elif errcheck == 2:
                              main.errorBox("Error","Your file has more than 3 columns in it.")
                         elif errcheck == 3:
                              main.errorBox("Error","Your file contains students with duplicate IDs.")
                         elif errcheck == 4:
                              main.errorBox("Error","There is already a class with the same name as this one.\nPlease choose a different name.")

#pressDelete
#created Jan. 30, 2017
# - deletes the user-selected class from the list of classes,
#   then calls updateClassNames
# - only callable/button only appears when a class exists
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Delete Class, no return values
# - needs the following to work:
# ----- the appJar library
# ----- updateClassNames and its requirements
# ----- the file AttendanceChecker.py
def pressDelete(btn):
     print(btn)
     print("deleting class " + str(main.getListItems("classes")))
     temp = classesName.index(main.getListItems("classes")[0])
     DeleteClass(classes,classes[temp])
     updateClassNames()
     print("done deleting")
     print("classes -> " + str(main.getListItems("classData")))
     main.updateListItems("classData", main.getListItems("classData"))

#toggleButtons
#created Jan. 31, 2017
# - hides the View Class and Delete Class button whenever there are
#   0 classes and the active menu is the Classes menu
# - 1 arg of type string (lb) automatically supplied by the list box,
#   no return values
# - needs the following to work:
# ----- the appJar library
# ----- the View Class and Delete Class buttons
def toggleButtons(lb):
     global currentSession
     global maxSession
     print(lb)
     #if (lb == "classData" and len(main.getAllListItems("classData")) > 0):
          #main.hideButton("Delete")
          #main.hideButton("View Class")
          #main.showButton("Present!")
          #main.showButton("Absent!")
          #main.showButton("Jump to Session")
          #if currentSession > 0:
               #main.showButton("Previous Session")
          #if currentSession < maxSession:
               #main.showButton("Next Session")
     if (lb == "classes" and len(classes) > 0):
          main.showButton("View Class")
          main.showButton("Delete")
          #main.hideButton("Present!")
          #main.hideButton("Absent!")
          #main.hideButton("Previous Session")
          #main.hideButton("Next Session")
          #main.hideButton("Jump to Session")
     elif (lb == "classes" and len(classes) == 0):
          main.hideButton("Delete")
          main.hideButton("View Class")
     #elif lb == "classes":
          #main.hideButton("Present!")
          #main.hideButton("Absent!")
          #main.hideButton("Previous Session")
          #main.hideButton("Next Session")
          #main.hideButton("Jump to Session")

#viewTrigger
#created Mar. 15, 2017
# - calls pressView to update the viewing window for class data
# ---- before displaying the viewing window itself
# - 1 input arg automatically supplied by button, no output
# - needs the following to work:
# ---- the appJar library
# ---- whatever requirements pressView needs
def viewTrigger(btn):
     print(btn)
     pressView()
     main.showSubWindow("view")

#pressView
#created Jan. 30, 2017
# - displays the user-selected class's details, including students and their
#   current attendance status in the latest class session
# - hides the Delete and View Class buttons, shows the Present! button
# - no input args, no return values
# - needs the following to work:
# ----- the appJar library
# ----- the file AttendanceChecker.py
#edited Feb. 13, 2018
# - removed if and else condition for class_dur label
# - replaced class_dur with curr_session
def pressView():
     global classesName
     global classDataDisplay
     global studentsNames
     global currentSession
     global maxSession
     global currentView
     global currentMax
     print("selected " + str(main.getListItems("classes")))
     if len(classes) > 0:
          # temp is the list of things to be displayed
          # tempS is the list of students to be displayed, and is needed to make
          #    setPresent() easier
          temp = []
          tempS = []
          # get the index of the class being viewed
          index = classesName.index(main.getListItems("classes")[0])
          # save it to global variable
          classDataDisplay = index
          print("classes index -> " + str(classDataDisplay))
          # get class name
          #temp.append(classes[index].getname())
          # make it the currently viewed class
          main.setLabel("class_name",classes[index].getname())

          # set # of current session (i.e. the latest one)
          #    being viewed, zero-indexing already
          #make it currently viewed session
          currentSession = classes[index].getsessionnum()
          main.setLabel("curr_session","Session " + str(currentSession + 1))
          

     
          # get max number of sessions for the class being viewed, 0-indexing
          try:
               maxSession = int(classes[index].getmaxsessionnum()) - 1
          except TypeError:
               maxSession = Ellipsis
          print("max sessions for this class -> " + str(maxSession))
          temp.append("Session " + str(currentSession + 1))
          temp.append("")
          # get list of present and absent students in latest session
          temp.append("Present:")
          for stud in classes[index].getstudents():
               if classes[index].getattendance(stud,-1) == 1:
                    temp.append(stud.getname())
                    tempS.append(stud.getname())

          temp.append("")
          temp.append("Absent:")
          for stud in classes[index].getstudents():
               if classes[index].getattendance(stud,-1) == 0:
                    temp.append(stud.getname())
                    tempS.append(stud.getname())
          # display the class details
          main.updateListItems("classData",temp)
          print("current session -> " + str(currentSession))
          # set list of students in the class being viewed
          studentsNames = tempS

#refreshView
#created Jan. 31, 2017
# - functionally identical to pressView, to be called before ending
#   a successful setPresent, prevSession, nextSession, and jumpTo
# - also called after switching between class sessions
# - no calling arguments, no return values
# - needs the following to work:
# ----- the appJar library
# ----- the file AttendanceChecker.py
#edited Feb. 13, 2018
# - removed if and else condition for class_dur label
# - replaced class_dur with curr_session
def refreshView():
     global classDataDisplay
     global studentsNames
     global currentSession
     print("refreshing")
     if len(classes) > 0:
          temp = []
          tempS = []
          print("classes index -> " + str(classDataDisplay))

          main.setLabel("curr_session","Session " + str(currentSession + 1))
          
          temp.append("Session " + str(currentSession + 1))
          temp.append("")
          temp.append("Present:")
          for stud in classes[classDataDisplay].getstudents():
               if classes[classDataDisplay].getattendance(stud,currentSession) == 1:
                    temp.append(stud.getname())
                    tempS.append(stud.getname())
          temp.append("")
          temp.append("Absent:")
          for stud in classes[classDataDisplay].getstudents():
               if classes[classDataDisplay].getattendance(stud,currentSession) == 0:
                    temp.append(stud.getname())
                    tempS.append(stud.getname())
          main.updateListItems("classData",temp)
          studentsNames = tempS

#setPresent
#created Jan. 31, 2017
# - sets the selected student's attendance to present, then updates
#   the class data being displayed
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Present!, no return values
# - assume all student names are unique
# - needs the following to work:
# ----- the appJar library
# ----- the file AttendanceChecker.py
def setPresent(btn):
     global classDataDisplay
     #global studentsNames
     global currentSession
     print(btn)
     print("selected " + str(main.getListItems("classData")))
     if main.getListItems("classData")[0] in studentsNames:
          tempSN = main.getListItems("classData")[0]
          print("student's name -> " + str(tempSN))
          #tempI = studentsNames.index(tempSN)
          #print("student's ID -> " + str(tempI))
          tempS = classes[classDataDisplay].findstudent(tempSN)
          classes[classDataDisplay].setattendance(tempS,currentSession)
          refreshView()

#setAbsent
#created Feb. 26, 2017
# - sets the selected student's attendance to absent, then updates
#   the class data being displayed
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Absent!, no return values
# - assume all student names are unique
# - needs the following to work:
# ----- the appJar library
# ----- the file AttendanceChecker.py
def setAbsent(btn):
     global classDataDisplay
     #global studentsNames
     global currentSession
     print(btn)
     print("selected " + str(main.getListItems("classData")))
     if main.getListItems("classData")[0] in studentsNames:
          tempSN = main.getListItems("classData")[0]
          print("student's name -> " + str(tempSN))
          #tempI = studentsNames.index(tempSN)
          #print("student's ID -> " + str(tempI))
          tempS = classes[classDataDisplay].findstudent(tempSN)
          classes[classDataDisplay].setabsence(tempS,currentSession)
          refreshView()

#prevSession
#created Feb. 7, 2017
# - displays the session before the one being viewed
# - will refresh the view after adjusting the # of the session being viewed
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Prev Session, no return values
# - needs the following to work:
# ----- the appJar library
def prevSession(btn):
     global currentSession
     print(btn)
     #make sure negative doesn't slip through
     if currentSession > 0:
          currentSession -= 1
          refreshView()
     else:
          print("can't go any further back")
          main.errorBox("Error","You can't go further back for this class.")
          

#nextSession
#created Feb. 7, 2017
# - displays the session after the one being viewed
# - creates a new record of attendance for the next session if the current
#   one being viewed is the latest session
# - will refresh the view after adjusting the # of the session being viewed
# - 1 arg of type string (btn) automatically supplied by the Button for
#   Next Session, no return values
# - needs the following to work:
# ----- the appJar library
def nextSession(btn):
     global currentSession
     global classDataDisplay
     global maxSession
     print(btn)
     if (currentSession < maxSession) or (maxSession == Ellipsis):
          print("currentSession was " + str(currentSession))
          print("gonna add 1 to currentSession")
          currentSession += 1
          print("currentSession is " + str(currentSession))
          #making a new session
          if len(classes[classDataDisplay].getallattendance()) == currentSession and len(classes[classDataDisplay].getallattendance()) <= maxSession:
               print("add another list to the attendance record")
               b = []
               #make a blank session
               for i in range(len(classes[classDataDisplay].getallattendance()[-1])):
                    b.append(0)
               classes[classDataDisplay].extendattendance(b)
          #refresh the window
          refreshView()
     else:
          print("can't go further forward")
          main.errorBox("Error","You can't go further forward in this class.")

#jumpTo
#created March 13, 2017
# - set currently displayed session to supplied session number
# - refreshes the Classes Data window with the supplied session number attendance records
# - no input, no output
# - needs the following to work:
# ---- the appJar library
# ---- see the other function's details for its requirements
def jumpTo(btn):
     global currentSession
     ses = main.getEntry("Session Number")
     try:
          ses = int(ses)
     except ValueError:
          main.errorBox("Error","Enter a number please!")
          return
     #zero-indexing
     currentSession = ses - 1
     try:
               #this is python, can't allow user to view negative sessions or it will wrap around
               if currentSession < 0:
                    main.errorBox("Error","You can't view that session!")
               else:
                    refreshView()
     except IndexError:
          main.errorBox("Error","You haven't started that session yet!")
     main.clearAllEntries()
         
#uploadBtn
#created Jan. 28, 2017
# - generates the button for "Upload Class"
# - see pressUpload for the effect of pressing the button
# - no args, no return values
# - needs the following to work:
# ----- upload.gif, the icon for Upload Class
# ----- the appJar library
def uploadBtn():
     main.setSticky("nw")
     main.setPadding([10,5])
     main.addButton("Upload",pressUpload,0,0)
     main.setButtonImage("Upload","upload.gif")
     main.setSticky("")
     main.setPadding([0,0])

#viewBtn
#created Jan. 30, 2017
# - generates the button for "View Class"
# - see pressView for the effect of pressing the button
# - no args, no return values
# - needs the following to work:
# ----- view.gif, the icon for View Class
# ----- the appJar library
def viewBtn():
     main.setSticky("nw")
     main.setPadding([10,5])
     main.addButton("View Class",viewTrigger,0,1)
     main.setButtonImage("View Class","view.gif")
     main.setSticky("")
     main.hideButton("View Class")
     main.setPadding([0,0])

#deleteBtn
#created Jan. 30, 2017
# - generates the button for "Delete Class"
# - see pressDelete for the effect of pressing the button
# - no args, no return values
# - needs the following to work:
# ----- delete.gif, the icon for Delete Class
# ----- the appJar library
def deleteBtn():
     main.setPadding([10,5])
     main.setSticky("nw")
     main.addButton("Delete",pressDelete,0,2)
     main.setButtonImage("Delete","delete.gif")
     main.setSticky("")
     main.hideButton("Delete")
     main.setPadding([0,0])

#checkPresent
#created Jan. 31, 2017
# - generates the button for "Present!"
# - see setPresent for the effect of pressing the button
# - no args, no return values
# - needs the following to work:
# ----- the appJar library
def checkPresent():
     main.setPadding([5,00])
     main.addButton("Present!",setPresent,3,2)
     main.setButtonImage("Present!","present.gif")
     #main.hideButton("Present!")
     main.setPadding([0,0])

#checkAbsent
#created Feb. 26, 2017
# - generates the button for "Absent!"
# - see setAbsent for the effect of pressing the button
# - no args, no return values
# - needs the following to work:
# ----- the appJar library
def checkAbsent():
     main.setPadding([5,00])
     main.addButton("Absent!",setAbsent,3,1)
     main.setButtonImage("Absent!","absent.gif")
     #main.hideButton("Absent!")
     main.setPadding([0,0])

#sessionButton
#created Feb. 7, 2017
# - generates the button for "Next Session" and "Previous Session"
# - see  for the effect of pressing the button
# - no args, no return values
# - needs the following to work:
# ----- the appJar library
def sessionButton():
     main.setPadding([10,00])
     main.addButton("Previous Session",prevSession,3,0)
     main.setButtonImage("Previous Session","prev.gif")
     #main.hideButton("Previous Session")
     main.setPadding([0,0])

     main.setPadding([10,00])
     main.addButton("Next Session",nextSession,3,3)
     main.setButtonImage("Next Session","next.gif")
     #main.hideButton("Next Session")
     main.setPadding([0,0])

#menu0_display
#created Jan. 28, 2017
# - generates the subcontents of the main page
# - no args, no return values
# - needs the following to work:
# ----- the appJar library
def menu0_display():
     main.setPadding([0,10])
     main.setSticky("nw")
     main.addLabel("label00","You don't have any classes!\nMake a class by clicking the Upload Class button!",0,1)
     main.setSticky("")

     main.startLabelFrame("Your Classes",1,0,3)
     main.setSticky("nw")
     main.addListBox("classes",classesName)
     main.setListBoxHeight("classes",25)
     main.setSticky("")
     main.stopLabelFrame()

     #main.startLabelFrame("Class Data",1,1,4)
     #main.setSticky("news")
     #main.addListBox("classData",classesName,1,1,4)
     #main.setListBoxHeight("classData",25)
     #main.setListBoxWidth("classData",40)
     #main.setSticky("")
     #main.stopLabelFrame()

     main.addLabel("label01","Attendance Checker v1.3.7",2,0,3)

     #main.setSticky("n")
     #main.startLabelFrame("Jump to Session",1,2)
     #main.setSticky("news")
     #main.addLabelEntry("Session Number",0,1)
     #main.addButton("Go!",jumpTo,0,2)
     #main.setSticky("")
     #main.stopLabelFrame()
     #main.setSticky("")

     #main.setListBoxFunction("classData",toggleButtons)
     #main.setListBoxFunction("classes",toggleButtons)
     
     if len(classes) > 0:
          main.hideLabel("label00")
          main.showButton("Delete")
          main.showButton("View Class")

#menu0
#created Jan. 28, 2017
# - generates the main page in the correct position relative to
#   the background image
# - no args, no return values
# - see uploadBtn and menu0_display for this function's requirements
def menu0():
     #main.startLabelFrame("",0,0)
     uploadBtn()
     deleteBtn()
     viewBtn()
     #main.stopLabelFrame()
     #checkPresent()
     #checkAbsent()
     #sessionButton()
     menu0_display()
     updateClassNames()

#created Feb. 13, 2017
# - functionality for "See .csv file's content format" button whcih will load the subwindow "qm" from def vqm
def viewquemark(btn):
     print(btn)
     main.showSubWindow("qm")

#created Feb. 13 2017
# - creates subwindow and will show .csv file content's format
def vqm():
     main.startSubWindow("qm","",True)
     main.setSticky("news")
     main.setStretch("both")

     main.setPadding([10,5])
     main.addImage("qm","format.gif")
     
     main.stopSubWindow()

#upMenu
#created Jan. 31, 2017
# - generates the Upload Class subwindow, initially hidden
# - no args, no return values
# - needs the following to work:
# ----- the appJar library
# ----- functions setI, doUpload, and Cancel
#edited Feb. 13, 2018 by Robelle Silverio
# -remove some instructionsadded 
# - added "See .csv file's content format" button and has a functionality called viewquemark
def upMenu():
     main.startSubWindow("up","",True)
     main.setSticky("news")
     main.setStretch("both")
     
     main.setPadding([10,5])
     main.addLabelEntry("Name of class:",0,0,1)
     
     main.addLabelEntry("Number of sessions:",1,0,1)
     main.setPadding([0,0])
     
     main.setPadding([50,0])
     main.addCheckBox("Indefinite",2,0,1)
     main.setPadding([0,0])
     main.setCheckBoxFunction("Indefinite",setI)
     
     main.setPadding([10,5])
     main.addLabelEntry("Class record file:",3,0,1)
     main.setEntryDefault("Class record file:", "file.csv")

     
     main.addButton("Upload Class",doUpload,4,0)
     main.addButton("Cancel",Cancel,4,1)

     main.addLabel("instructions","Please place your class record file in the same\n folder as this program.\n\nThe class record file must be a .csv file",5,0)

     main.addButton("See .csv file's content format",viewquemark,6,0)
     #main.hideButton("Absent!")
     main.stopSubWindow()


#viewMenu
#created Feb. 7, 2017
# - generates the View Class subwindow, initially hidden
# - contains the viewing window for class data, the present, absent, next session,
# ---- and previous session buttons
# - also has jump to session button
# - no args, no return values
# - needs the following to work:
# ----- the appJar library
# ----- functions 
#edited Feb. 13, 2017
# - removed if and else condition for class_dur label
# - replaced class_dur with curr_session
def viewMenu():
     global currentView
     main.startSubWindow("view","",True)
     main.setSticky("news")
     main.addLabel("class_name",str(currentView),0,0,4)
     main.addLabel("curr_session",str(currentMax),1,0,4)
     main.setSticky("")
     
     main.startLabelFrame("Class Data",2,0,4)
     main.setSticky("news")
     main.addListBox("classData",classesName)
     main.setListBoxHeight("classData",15)
     main.setListBoxWidth("classData",40)
     main.setSticky("")
     main.stopLabelFrame()

     #main.startLabelFrame("Actions",1,0)
     checkPresent()
     checkAbsent()
     sessionButton()
     #main.stopLabelFrame()

     main.setSticky("n")
     main.startLabelFrame("Jump to Session",4,0,4)
     main.setSticky("news")
     main.addLabelEntry("Session Number",0,0)
     main.addButton("Go!",jumpTo,0,1)
     main.setSticky("")
     main.stopLabelFrame()
     main.setSticky("")
     main.stopSubWindow()
    
#updateClassNames
#created Jan. 28, 2017
# - flush the list of classes' names, then fill with the names of all classes
#   and then update the GUI
# - to be used as argument for registerEvent()
# - no calling args, no return values
# - needs the following:
# ----- the file AttendanceChecker.py
# ----- the appJar library
# ----- the list of classes and a list for their names
def updateClassNames():
     global classes
     global classesName
     del classesName[:]
     if len(classes) > 0:
          for name in classes:
               classesName.append(name.getname())
     main.updateListItems("classes",classesName)
     print("names of existing classes -> " + str(classesName))
     if len(classes) == 0:
          main.hideButton("Delete")
          main.hideButton("View Class")
          main.showLabel("label00")
     else:
          main.hideLabel("label00")
          main.showButton("Delete")
          main.showButton("View Class")

#read_on_startup
#created Feb. 26, 2017
# - read from savefile.txt if it exists
# - load in existing class data from savefile.txt
# - no input, no output
# - needs the following:
# ---- savefile.txt (optional)
# ---- AttendanceChecker.py

#format of savefile
# -----
# numberofclasses
# nameofclass
# max#ofsessions currentsession
# #ofstudents
# studentname studentID
# ...
# attendance record
# ...
# nameofclass
# ...
# -----
def read_on_startup():
     global classes
     if os.path.isfile("savefile.txt") == True:
          print("savefile.txt exists, reading it now")
          f = open("savefile.txt","r")
          #get the number of classes
          i = f.readline()
          i = i.strip('\n')
          i = int(i)
          print("there are " + str(i) + " classes")
          for times in range(i):
               #make a blank class
               x = Classes()
               
               #get the name of the class
               nameC = f.readline()
               nameC = nameC.strip("\n")
               nameC = nameC.strip("\r")
               print("got class " + nameC)
               #set name 
               x.changename(nameC)
               
               #get max# of sessions and current session#
               temp = f.readline() #string
               temp = temp.split() #list
               try:
                    maxS = int(temp[0])
               except ValueError:
                    maxS = Ellipsis
               currS = int(temp[1])
               print("max sessions is " + str(maxS))
               print("current session is " + str(currS))
               #set max and current sessions
               x.numofsessions(maxS)
               #x.number = currS - 1 #zero-indexing
               
               #get the number of students in the class
               num_students = f.readline()
               num_students = num_students.strip('\n')
               num_students = int(num_students)
               print("there are " + str(num_students) + " in this class")

               #get the students and their ID
               stu = []
               for j in range(num_students):
                    student = f.readline()
                    student = student.strip('\n')
                    student = student.split()
                    print("found student " + str(student))
                    temp = MakeStudent(student[0],student[1])
                    stu.append(temp)
               print("length of student list is " + str(len(stu)))
               x.students = stu

               #get attendance record of the class
               att = []
               for j in range(currS): #not zero-indexed
                    entry = f.readline()
                    entry = entry.split()
                    for k in range(len(entry)):
                         entry[k] = int(entry[k])
                    print("got attendance entry " + str(entry))
                    att.append(entry)
               print("length of attendance record is " + str(len(att)))
               #set attendance
               x.attendance = AttendanceR()
               x.attendance.number = currS -1
               x.attendance.record = att
                    
               #get attendance record start dates

               #add to classes
               classes.append(x)
          f.close()

#checkStop
#created Jan. 31, 2017
# - displays a prompt when the user tries to quit the application
# - no calling args, returns True if Yes was answered, otherwise False
# - needs the following:
# ----- the appJar library
def checkStop():
     global classes
     temp = main.yesNoBox("quit", "Are you sure you want to quit?")
     if temp == True:
          f = open("savefile.txt","w")
          f.write(str(len(classes)))
          f.write("\n")
          for item in classes:
               f.write(item.getname())
               f.write("\n")
               f.write(str(item.getmaxsessionnum()))
               f.write(" ")
               f.write(str(len(item.getallattendance())))
               f.write("\n")
               f.write(str(len(item.getstudents())))
               f.write("\n")
               for stud in item.getstudents():
                    f.write(stud.getname())
                    f.write(" ")
                    f.write(stud.getID())
                    f.write("\n")
               for record in item.getallattendance():
                    for entry in range(len(record)):
                         f.write(str(record[entry]))
                         f.write(" ")
                    f.write("\n")
          f.close()
     return temp
         
#--------------------------------------------------------------#
#"indefinite"/class length entry
signal = 0
#zero-indexed
currentSession = 0
#not zero-indexed
maxSession = 0
#index of the class being viewed
classDataDisplay = 0
#list of classes
classes = []
#AddClass(classes,"Test",1)
#list of the names of classes
classesName = []
#currently-viewed class's name
currentView = ""
#currently-viewed class's max sessions
currentMax = ""
#list of students' names in the class being viewed
studentsNames = []
read_on_startup()

#main = gui("Attendance Checker","800x600")
main = gui("Attendance Checker")
main.setLocation(0,0)
main.setFont(14,"Berlin Sans FB")
main.setBgImage("background.gif")

menu0()
upMenu()
viewMenu()
vqm()
main.setStopFunction(checkStop)

    
main.go()
