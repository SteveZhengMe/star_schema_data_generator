from random import randint
from datetime import datetime
from datetime import timedelta

from baseclass import ERObject

class Person(ERObject):
    name = None
    gender = None
    dob = None
    parameters = None

    def __init__(self, id, parameters):
        super().__init__(id)
        self.name = self.names[randint(0,len(self.names)-1)]
        if randint(0,10) > 5:
            self.gender ="M"
        else:
            self.gender ="F"
        self.parameters = parameters

    def getRandDate(self, startYear, endYear=2000, month=0):
        year = randint(startYear,endYear)
        if month == 0:
            month = randint(1,12)
        return"%d-%d-%d" % (year,month,randint(1,28))
    
    def print(self):
        result = super().print()
        result.update({"name":self.name,"gender":self.gender,"dob":self.dob})
        return result

class Prof(Person):
    onboarding_date = None

    def __init__(self, id, parameters):
        super().__init__(id, parameters)
        self.dob = self.getRandDate(parameters.professor_dob_year)
        self.onboarding_date = self.getRandDate(parameters.professor_start_working_year)
    
    def print(self):
        result = super().print()
        result.update({"onboarding_date":self.onboarding_date})
        return result
    
    def exportHead(self):
        return "id,name,gender,dob,onboarding_date"

    def exportData(self):
        return "%d,%s,%s,%s,%s" % (self.id, self.name,self.gender,self.dob,self.onboarding_date)
    

class Student(Person):
    ori_continent = None
    register_date = None
    enroll_date = None
    program = None
    drop_off_date = None
    drop_off_reason = None
    dropOffReasonList = None

    def __init__(self, id, reasonList, parameters):
        super().__init__(id, parameters)
        self.ori_continent = self.continent[randint(0,len(self.continent)-1)]
        self.dob = self.getRandDate(parameters.student_dob_year)
        self.dropOffReasonList = reasonList
        
    def register(self, reg_year):
        reg_month = [1,2,3,4,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,10,10,10,11,11,11,11,11,11,12,12,12,12,12,12,12]
        self.register_date ="%d-%d-%d" % (reg_year, reg_month[randint(0,len(reg_month)-1)], randint(1,28))
        # Assumption: from parameters.remote_learning_start_year, Algonquin started remote class
        year = int(self.register_date.split("-")[0])
        if year < self.parameters.remote_learning_start_year:
            if randint(0,10) < 7:
                self.enroll()
        else:
            if randint(0,10) < 9:
                self.enroll()
                
    def enroll(self):
        year, month, date = self.register_date.split("-")
        if int(month) < 8:
            self.enroll_date ="%s-%d-%d" % (year,9,min(randint(1,30),int(date)))
        else:
            self.enroll_date ="%d-%d-%d" % (int(year)+1,1,min(randint(1,31),int(date)))

        self.dropOff()
        
    def dropOff(self):
        becauseRemote = None
        if int(self.enroll_date.split("-")[0]) < self.parameters.remote_learning_start_year:
            if randint(0,100) < self.parameters.before_remote_learning_drop_off["rate"]:
                # 10% Drop off and 20% because of remoting
                becauseRemote = randint(0,100) < self.parameters.before_remote_learning_drop_off["remote"]+10
                theTime = datetime.strptime(self.enroll_date,'%Y-%m-%d')
                dropOffTime = theTime + timedelta(days=randint(1,100))
                self.drop_off_date = datetime.strftime(dropOffTime,'%Y-%m-%d')
        else:
            if randint(0,100) < self.parameters.after_remote_learning_drop_off["rate"]:
                # 30% Not Drop off and 50% because of remoting
                becauseRemote = randint(0,100) < self.parameters.after_remote_learning_drop_off["remote"]+10
                self.drop_off_date = datetime.strftime(datetime.strptime(self.enroll_date,'%Y-%m-%d') + timedelta(days=randint(0,40)),'%Y-%m-%d')
                
        if becauseRemote is not None:
            reasonList = [item for item in self.dropOffReasonList if item.remoteRelavent==becauseRemote]
            self.drop_off_reason = reasonList[randint(0, len(reasonList)-1)]                  
    
    def getDropOffReason(self):
        reason_id = None
        reason_desc = None
        if self.drop_off_reason is not None:
            reason_id = self.drop_off_reason.id
            reason_desc = self.drop_off_reason.reason
        return reason_id, reason_desc
            

    def print(self):
        result = super().print()
        result.update({
            "ori_continent":self.ori_continent,
            "program":self.program,
            "register_date":self.register_date,
            "enroll_date":self.enroll_date,
            "drop_off_reason_id":self.getDropOffReason()[0],
            "drop_off_reason_desc":self.getDropOffReason()[1]
        })
        return result

    def exportHead(self):
        return "id,name,gender,dob,ori_continent,register_date,enroll_date,program,drop_off_date,drop_off_reason_id"

    def exportData(self):
        return "%d,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id, self.name,self.gender,self.dob,self.ori_continent,self.register_date,self.enroll_date,self.program,self.drop_off_date,str(self.getDropOffReason()[0]))
