##AttendanceChecker.py authored by Faneallrich Li Yao

#This is a course requirement for CS 192 Software Engineering under the
#supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of
#Computer Science, College of Engineering, University of the Philippines,
#Diliman for the AY 2016-2017.

#Version 1.5.5 (May 8, 2017) by Jeremy Micah Choa
# - addClass no longer adds a blank-name student after reading a file
# - addClass now checks if the class's name is not already being used

#Version 1.5 (Mar. 24, 2017) by Jeremy Micah Choa
# - addClass now returns an integer whose value depends
# ---- on errors found in reading the class record file

#Version 1.4.5 (Mar. 23, 2017) by Jeremy Micah Choa
# - adjust class Attendance and all other functions that use class Classes's
# ---- list "attendance"

#Version 1.4 (Feb 27, 2017) by Kenneth Velasquez
# - made a new class for Attendance records

#Version 1.3.5 (Feb. 17, 2017) by Jeremy Micah Choa
# - fixed findstudent to search by name instead of ID
# - fixed AddClass to extract comma-separated names
# - fixed AddClass to sort students alphabetically

#Version 1.3 (Feb. 10, 2017) by Jeremy Micah Choa
# - fixed AddStudent, AddClass to actually read student record file
# - disabled createClass, it was redundant

#Version 1.2 (Feb. 2, 2017) by Kenneth Velasquez
# - added functions AddStudent, createClass, AddClass

#Version 1.1 (Jan. 28, 2017) by Jeremy Micah Choa
# - fixed the formatting of this file
# - added function getname() to class Classes
# - disabled delete_student(), don't need it anyway
# - changed 1st calling argument of AddClass() to be more obvious

#Version 1.0 (Jan. 18, 2017) by Faneallrich Li Yao

#File created on Jan. 18, 2017
#Developed by Team 6 Absences
#Developed for teachers and instructors everywhere (we hope)
#This is the file of the classes and methods that will be used in the
#database of Attendance Checker.

#represent each Attendance record as an object of index and attendances
class AttendanceR:
#the Attendance initialization function
#created Feb. 27, 2017
# - set current session number to 0
# ---- and initialize the array that stores the data
# - no input, no output
     def __init__(self):
          self.number = 0
          self.record = []

#set_sessionNum
#created Feb. 27, 2017
# - set current session number
# - 1 integer input, no output
     def set_sessionNum(self, num):
          self.number = num

#get_sessionNum
#created Feb. 27, 2017
# - get current session number
# - no input, 1 integer output
     def get_sessionNum(self):
          return self.number

#get_recordLength
#created Mar. 23, 2017
# - returns the length of the Attendance record list
# - no input, 1 integer output
     def get_recordLength(self):
          return len(self.record)

#add_record
#created Mar. 23, 2017
# - adds an object rec to the Attendance record
# - 1 list input, no output
     def add_record(self,rec):
          self.record.append(rec)

#add_newStudent
#created Mar. 23, 2017
# - adds a new record entry on all records
# - no input, no output
     def add_newStudent(self):
          for i in self.record:
               i.append(0)

#retrieve
#created Mar. 23, 2017
# - returns the attendance record of a given student b in a given session a
# - requires 2 integer input, gives 1 integer output
     def retrieve(self, a, b):
          return self.record[a][b]

#retrieve_everything
#created Mar. 23, 2017
# - returns the whole attendance record as a single list
# - no input, no output
     def retrieve_everything(self):
          return self.record

#set_att
#created Mar. 23, 2017
# - sets the attendance of student b in session a to be num
# - requires 3 integer input, gives no output
     def set_att(self,a,b,num):
          self.record[a][b] = num

#---------------------------------

#represent each Student as an object of name and ID
class Student:
# the Student initialization function
# created Jan. 25, 2017
# - sets Student name and ID to blank
# - no input, no output
     def __init__(self):
          self.name = ""
          self.ID = ""

# set_ID
# created Jan. 25, 2017
# - sets the ID of the Student with supplied string
# - needs 1 string input, no output
     def set_ID(self,n):
          self.ID = n

# set_name
# created Jan. 25, 2017
# - sets the name of the Student with supplied string
# - needs 1 string input, no output
     def set_name(self,n):
          self.name = n

# get_name
# created Jan. 27, 2017
# - gets the name of the Student
# - no input, returns a string
     def getname(self):
          return self.name

# getID
# created Jan. 27, 2017
# - gets the ID of the Student
# - no input, returns a string
     def getID(self):
          return self.ID

#-------------------------------------

class Classes:
# the Classes initialization function
# created Jan. 25, 2017
# - sets the following to blank:
# ---- list of Students in the Class
# ---- the name of the Class
# ---- the length of list "attendance"
# ---- the maximum sessions allowed in the Class
# ---- the Attendance of each Student in each session
# - no input, no output
     def __init__(self):
          self.students = []
          self.name = ""
          self.maxnumber = 0
          self.attDate = []
          self.attendance = AttendanceR()

# changename
# created Jan. 25, 2017
# - sets the name of the Class
# - needs 1 string input, no output
     def changename(self,n):
          self.name = n

# numofsessions
# created Jan. 25, 2017
# - sets the maximum number of sessions in the Class
# - needs 1 integer input, no output
     def numofsessions(self,n):
          self.maxnumber = n

# getname
# created Jan. 27, 2017
# - gets the name of the Class
# - no input, returns a string
     def getname(self):
          return self.name

# getsessionnum
# created Jan. 27, 2017
# - gets the number of sessions that the Class has completed
# - no input, returns an integer
     def getsessionnum(self):
          return self.attendance.get_sessionNum()

# getmaxsessionnum
# created Jan. 30, 2017
# - gets the maximum number of sessions that the Class can have
# - no input, returns an integer
     def getmaxsessionnum(self):
          return self.maxnumber

# getstudents
# created Jan. 30, 2017
# - gets the list of Students in the Class
# - no input, returns a list
     def getstudents(self):
          return self.students

# findstudent
# created Jan. 31, 2017
# - gets the particular Student in the Class by looking for the matching string
# - used specifically for the setPresent function in GUI.py
# - needs 1 string input, returns a Student
     def findstudent(self,i):
          for stu in self.students:
               if stu.getname() == i:
                    return stu
                    
# add_student
# created Jan. 27, 2017
# - adds a Student to the Class's list of Students
# - only called by AddClass
# - if the attendance list is empty, it appends an array with 1 element (0)
# - if not, it appends a 0 to the presumably existing initial session
# - needs 1 Student input, no output
     def add_student(self,stu):
          self.students.append(stu)
          if self.attendance.get_recordLength() == 0:
               self.attendance.add_record([0])
          elif self.attendance.get_recordLength() > 0:
               self.attendance.add_newStudent()

# getattendance
# created Jan. 30, 2017
# - gets the attendance status of a particular student in a particular
#   session in the Class
# - returns 1 if the Student is present, 0 if absent
# - needs 2 integer inputs, returns an integer
     def getattendance(self,stu,ses):
          temp = self.students.index(stu)
          #return self.attendance.record[ses][temp]
          return self.attendance.retrieve(ses,temp)

# getallattendance
# created Jan. 31, 2017
# - gets the entire attendance list of the Class
# - no input, returns a 2-dimensional list
     def getallattendance(self):
          temp = self.attendance.retrieve_everything()
          return temp

# setattendance

# created Jan. 31, 2017
# - sets the specified student in the specified session to present
# - needs 2 integer inputs, no output
     def setattendance(self,stu,ses):
          temp = self.students.index(stu)
          #self.attendance[ses][temp] = 1
          self.attendance.set_att(ses,temp,1)

# setabsence
# created Feb. 26, 2017
# - sets the specified student in the specified session to absent
# - needs 2 integer inputs, no output
     def setabsence(self,stu,ses):
          temp = self.students.index(stu)
          #self.attendance[ses][temp] = 0
          self.attendance.set_att(ses,temp,0)

# extendattendance
# created Feb. 13, 2017
# - appends a new list to the attendance record
# - needs 1 list input, no output
     def extendattendance(self,new):
          #self.attendance.append(new)
          self.attendance.add_record(new)
          # append date of function execution to self.attDate

# stringify
# created Feb. 13, 2017
# - converts given list into a string by concatenating each element in it
# - needs 1 list input, returns a string
def stringify(li):
     b = ''
     for i in li:
          b = b + str(i)
     return(b)

# AddClass
# created Feb. 1, 2017
# - generates a Class with supplied name, number of sessions, and a student
#   record file; then adds it to the supplied list
# - Students are generated with ID and name taken from the student record
#   file
# - needs 1 list of Classes, 2 strings, and 1 integer; returns 1 integer output

# csv fields must be arranged like this: ID, Lastname, Firstname
# all IDs must be unique
def AddClass(aList,name,sessions,studentfile):
     sfile = open(studentfile, "r")
     x = Classes()
	#set name and number of sessions
     x.changename(name)
     x.numofsessions(sessions)
     errcheck_ID = []
     for line in sfile:
          Id = []
          name = []
          tok = []
          order = 0
          for i in line:
               if (i == "," and order == 0):
                    print("Found the first comma")
                    Id = stringify(tok)
                    #error checking for blank ID
                    if Id == "":
                         return 1
                    #error checking for duplicate ID
                    errcheck_ID.append(Id)
                    print("Got ID#" + str(Id)) 
                    tok = []
                    order = 1
               elif (i == "," and order == 1):
                    print("Found the second comma")
                    tok.append(i)
                    order = 2
               elif (i == "\n" or i == ""):
                    print("Found the end of the line")
                    name = stringify(tok)
                    x.add_student(MakeStudent(name, Id))
                    print("Added student " + name)
                    tok = []
                    order = 0
               #check for errors
               #more than 3 columns
               elif (i == "," and order == 2):
                    return 2
               else:
                    print("Found a character")
                    tok.append(i)
     #reached the end of the file
     print("Found the end of the file")
     sfile.close()
     #name = stringify(tok)
     #x.add_student(MakeStudent(name, Id))
     #print("Added student " + name)
     #tok = []

     #check for errors
     #are all IDs unique?
     temp = set(errcheck_ID)
     if len(temp) != len(errcheck_ID):
          return 3
     
     #sort students by last name first
     x.students.sort(key=lambda x: x.name, reverse=False)
     print("Sorted class")
     for y in x.students:
          print(y.name)
	
     #then add the class to the list of classes
	#check first for duplicates
     errcheck_ID = []
     for i in aList:
	  errcheck_ID.append(i.getname())
	#error checking: not unique name
     if x.getname() in errcheck_ID:
	  return 4
	#success
     else:
          aList.append(x)
          return 0
     

# MakeStudent
# created Feb. 1, 2017
# - generates a Student given a name and ID
# - needs 2 strings, returns a Student
def MakeStudent(name, ID):
     x = Student()
     x.set_name(name)
     x.set_ID(ID)
     return x

#def createClass(filename, classname, session):
     #info = open(filename)
     #classdata = classname+".csv"
     #defaultloc = open(classdata, 'r+')
     #for i in info.readlines():
         #defaultloc.write(i)
     #info.close()
     #AddClass(ClassesList, classname, session, defaultloc)

# DeleteClass
# created Jan. 27, 2017
# - deletes a given Class from the given list
# - needs 1 list and 1 Class, no output
def DeleteClass(aList,cl):
     aList.remove(cl)

#test = []
#S1 = MakeStudent("A", "1")
#S2 = MakeStudent("B", "2")
#AddClass(test,"test",3)
#test[0].add_student(S1)
#test[0].add_student(S2)
#ou = test[0].getallattendance()
#print(ou)
