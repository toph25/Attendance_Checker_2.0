import unittest
from AttendanceChecker import *

# Define global variables for the tests
stud1 = MakeStudent("Baekhyun", 4)
stud2 = MakeStudent("Chanyeol", 61)
stud3 = MakeStudent("Suho", 1)
stud4 = MakeStudent("Jongin", 88)
class1 = Classes()
class1.name = "EXO"
class1.students = [stud1, stud2, stud3, stud4]
class1.number = 1



# Functions to test
# -- setattendance()
# -- setabsence()
# -- setexcused()
# -- setlate()
class TestAPEL(unittest.TestCase):
	def test_set_attendance(self):
		att = AttendanceR()
		att.record = [[0,0,0,0]]
		class1.attendance = att

		stu = class1.findstudent("Baekhyun")
		self.assertEqual(stu.ID, 4)
		
		temp = class1.students.index(stu)
		self.assertEqual(temp, 0)
		
		self.assertEqual(class1.attendance.record, [[0,0,0,0]])

		class1.setattendance(stu, 0)
		self.assertEqual(class1.attendance.record, [[1,0,0,0]])

	def test_set_excused(self):
		att = AttendanceR()
		att.record = [[0,0,0,0]]
		class1.attendance = att

		stu = class1.findstudent("Chanyeol")
		self.assertEqual(stu.ID, 61)
		
		temp = class1.students.index(stu)
		self.assertEqual(temp, 1)
		
		self.assertEqual(class1.attendance.record, [[0,0,0,0]])

		class1.setexcused(stu, 0)
		self.assertEqual(class1.attendance.record, [[0,2,0,0]])

	def test_set_late(self):
		att = AttendanceR()
		att.record = [[0,0,0,0]]
		class1.attendance = att

		stu = class1.findstudent("Suho")
		self.assertEqual(stu.ID, 1)
		
		temp = class1.students.index(stu)
		self.assertEqual(temp, 2)
		
		self.assertEqual(class1.attendance.record, [[0,0,0,0]])

		class1.setlate(stu, 0)
		self.assertEqual(class1.attendance.record, [[0,0,3,0]])

	def test_set_absence(self):
		att = AttendanceR()
		att.record = [[0,0,0,0]]
		class1.attendance = att

		stu = class1.findstudent("Jongin")
		self.assertEqual(stu.ID, 88)
		
		temp = class1.students.index(stu)
		self.assertEqual(temp, 3)
		
		self.assertEqual(class1.attendance.record, [[0,0,0,0]])

		class1.setabsence(stu, 0)
		self.assertEqual(class1.attendance.record, [[0,0,0,4]])
		


if __name__ == "__main__":
	unittest.main()