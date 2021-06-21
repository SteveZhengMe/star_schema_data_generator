from baseclass import ERObject

class Drop_Off_Reason(ERObject):
    reason = None
    remoteRelavent = False
    
    def __init__(self, id, reason, remoteRelavent):
        super().__init__(id)
        self.reason = reason
        self.remoteRelavent = remoteRelavent
    
    def exportHead(self):
        return "id,remoteRelavent,reason"

    def exportData(self):
        return "%d,%s,%s" % (self.id, self.remoteRelavent,self.reason)
    

class Drop_Off_Fact(ERObject):
    student_id = None
    drop_off_date = None
    drop_off_reason_id = None
    
    def __init__(self, id,student_id, drop_off_date, drop_off_reason_id):
        super().__init__(id)
        self.student_id = student_id
        self.drop_off_date = drop_off_date
        self.drop_off_reason_id = drop_off_reason_id
        
    def print(self):
        result = super().print()
        result.update({
            "student_id":self.student_id,
            "drop_off_date":self.drop_off_date,
            "drop_off_reason_id":self.drop_off_reason_id
        })
        return result
    
    def exportHead(self):
        return "id,student_id,drop_off_date,drop_off_reason_id"

    def exportData(self):
        return "%d,%d,%s,%d" % (self.id, self.student_id,self.drop_off_date,self.drop_off_reason_id)