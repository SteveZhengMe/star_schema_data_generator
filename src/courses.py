from random import randint
from datetime import datetime
from datetime import timedelta
import hashlib

from baseclass import ERObject

class Course(ERObject):
    name = None
    program = None
    course_duration_year = None
    remote_learning_start_year = 2018
    prof = None
    onlineDaysMap = {}
    
    def __init__(self, id, programName, year, parameter):
        super().__init__(id)
        randStr = hashlib.md5(str(randint(0,99999)).encode()).hexdigest()
        fistPos = randint(0,15)
        self.name = "c_" + randStr[fistPos:3+fistPos+randint(0,10)]
        self.program = programName
        self.course_duration_year = year
        self.remote_learning_start_year = parameter.remote_learning_start_year
        
    def setProf(self, prof):
        self.prof = prof
        
    def print(self):
        result = super().print()
        result.update({"name":self.name,"program":self.program,"course_duration_days":self.course_duration_year})
        return result
    
    def getOnlineRates(self, currYear):
        if currYear not in self.onlineDaysMap:
            if int(currYear) < self.remote_learning_start_year:
                self.onlineDaysMap[currYear] = 5 + randint(0,10)
            else:
                self.onlineDaysMap[currYear] = 40 + randint(0,60)
                
        return self.onlineDaysMap[currYear]

    def exportHead(self):
        return "id,name,program,course_duration_year"

    def exportData(self):
        return "%d,%s,%s,%d" % (self.id, self.name,self.program,self.course_duration_year)



class Curriculum_Fact(ERObject):
    student_id = None
    course_id = None
    professor_id = None
    start_date = None
    end_date = None
    participate_score = None
    lab_score = None
    theory_score = None
    final_score = None
    online_days = None
    classroom_days = None
    remote_learning_start_year = None
    
    def __init__(self, id, parameter):
        super().__init__(id)
        self.remote_learning_start_year = parameter.remote_learning_start_year
        
    def setStartDate(self, student, course):
        self.start_date = "%s-%d-%d" % (student.enroll_date.split("-")[0],int(student.enroll_date.split("-")[1])+1,1)
        theTime = datetime.strptime(self.start_date,'%Y-%m-%d')
        theEndTime = theTime + timedelta(days=course.course_duration_year*365)
        self.end_date = datetime.strftime(theEndTime,'%Y-%m-%d')

    def generateScores(self, student, course):
        startPoint = 40
        if int(student.enroll_date.split("-")[0]) < self.remote_learning_start_year:
            startPoint = 60
        
        self.participate_score = startPoint + randint(0,100 - startPoint)
        self.lab_score = startPoint + randint(0,100 - startPoint)
        self.theory_score = 50 + randint(0,50)
        self.final_score = (self.participate_score+self.lab_score+self.theory_score+self.theory_score)/4
    
    def generateRemoteLearning(self, student, course):
        totalLearningDate = 365*course.course_duration_year*3/7
        
        self.online_days = int(course.getOnlineRates(self.start_date.split("-")[0]) * totalLearningDate/100)
        self.classroom_days = int(totalLearningDate - self.online_days)
    
    def print(self):
        result = super().print()
        result.update({
            "student_id":self.student_id,
            "course_id":self.course_id,
            "professor_id":self.professor_id,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "participate_score":self.participate_score,
            "lab_score":self.lab_score,
            "theory_score":self.theory_score,
            "final_score":self.final_score,
            "online_days":self.online_days,
            "classroom_days":self.classroom_days
        })
        return result
    
    def exportHead(self):
        return "id,student_id,course_id,professor_id,start_date,end_date,participate_score,lab_score,theory_score,final_score,online_days,classroom_days"

    def exportData(self):
        return "%d,%d,%d,%d,%s,%s,%d,%d,%d,%d,%d,%d" % (self.id,self.student_id,self.course_id,self.professor_id,self.start_date,self.end_date,self.participate_score,self.lab_score,self.theory_score,self.final_score,self.online_days,self.classroom_days)
