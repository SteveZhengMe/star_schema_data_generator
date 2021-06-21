from random import randint

from people import Prof
from courses import Course
from courses import Curriculum_Fact
from people import Student
from dropoff import Drop_Off_Reason
from dropoff import Drop_Off_Fact
from parameters import Parameters

#  program_number, course_number_per_program, professor_number

class Main:
    parameters = None

    def __init__(self, parameters):
        self.parameters = parameters

    def professorFactory(self):
        profArray = []
        
        for seq in range(1, self.parameters.professor_number + 1):
            profArray.append(Prof(seq, self.parameters))
        
        # for item in profArray:
        #     print(item.print())
        
        return profArray

    def studentFactory(self, drop_off_reasons):
        studentArray = []
        seq = 0
        student_base_number = int(self.parameters.student_number * 0.8)
        random_student_number = int(self.parameters.student_number * 0.2)

        for year in range(self.parameters.student_enrollment_year["start"],self.parameters.student_enrollment_year["end"]):
            for i in range(student_base_number + randint(0,random_student_number)):
                seq += 1
                student = Student(seq, drop_off_reasons, self.parameters)
                student.register(year)

                if student.enroll_date:
                    student.program = Student.programs[randint(0,len(Student.programs)-1)]    

                studentArray.append(student)
        
        
        # print("%d/%d" % (len([item for item in studentArray if item.drop_off_reason is not None]), len(studentArray)))
        # for item in studentArray:
        #     if item.id < 30:
        #         print(item.print())    
                
        return studentArray

    def courseFactory(self):
        courseArray = []
        seq = 0
        for programName in Course.programs:
            durrationRand = randint(0,10)
            course_duration_year = 2
            if durrationRand < 4:
                # 1 years
                course_duration_year = 1
            elif durrationRand > 8:
                # 3 years
                course_duration_year = 3
            
            # Create courses in a program
            for courseCount in range(0,randint(self.parameters.course_number_per_program["min"],self.parameters.course_number_per_program["max"])):
                seq += 1
                courseArray.append(Course(seq, programName,course_duration_year,self.parameters))
        
        # for item in courseArray:
        #     print(item.print())
        return courseArray

    def currFactory(self, studentList, coursesList):
        # curr_fact
        seq = 0
        currList = []
        dropOffList = []
        drop_off_seq = 0
        
        for student in studentList:
            if student.enroll_date:
                for course in coursesList:
                    if student.program == course.program:
                        seq += 1
                        curr = Curriculum_Fact(seq, self.parameters)
                        curr.student_id = student.id
                        curr.course_id = course.id
                        curr.professor_id = course.prof.id
                        curr.setStartDate(student, course)
                        
                        curr.generateScores(student, course)
                        curr.generateRemoteLearning(student, course)
                        currList.append(curr)
                        #print(seq)
                
                if student.drop_off_reason is not None:
                    drop_off_seq += 1
                    dropOffList.append(Drop_Off_Fact(drop_off_seq, student.id, student.drop_off_date, student.drop_off_reason.id))
        
        return currList, dropOffList

    def generateDropOffReason(self):
        reasonsArray = []
        seq = 0
        for reason in Drop_Off_Reason.normalReasons:
            seq += 1
            reasonsArray.append(Drop_Off_Reason(seq, reason,False))
        
        for reason in Drop_Off_Reason.remoteReasons:
            seq += 1
            reasonsArray.append(Drop_Off_Reason(seq, reason,True))
        return reasonsArray
    