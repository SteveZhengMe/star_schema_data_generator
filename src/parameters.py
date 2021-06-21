class Parameters:
    course_number_per_program = {"min":3,"max":6}
    remote_learning_start_year = 2018
    professor_number = 3000
    student_enrollment_year = {"start":2015,"end":2016}
    student_number = 20000
    before_remote_learning_drop_off = {"rate":10,"remote":20}
    after_remote_learning_drop_off = {"rate":30,"remote":50}

    # Set the number yourself
    student_dob_year = 1980
    professor_dob_year = 1960
    professor_start_working_year = 1990

    def setCourseNumberPerProgram(self, min, max):
        self.course_number_per_program["min"] = int(min)
        self.course_number_per_program["max"] = int(max)
    
    def setRemoteLearningStartYear(self, year):
        self.remote_learning_start_year = int(year)

    def setProfessorNumber(self, number):
        self.professor_number = int(number)

    def setStudentEnrollmentYear(self, start, end):
        self.student_enrollment_year["start"] = int(start)
        self.student_enrollment_year["end"] = int(end)

    def setStudentNumber(self, number):
        self.student_number = int(number)
    
    def setBeforeRemoteLearningDropOffAndReasonRate(self,drop_off_rate, remote_reason_rate):
        self.before_remote_learning_drop_off["rate"] = int(drop_off_rate)
        self.before_remote_learning_drop_off["remote"] = int(remote_reason_rate)
    
    def setAfterRemoteLearningDropOffAndReasonRate(self,drop_off_rate, remote_reason_rate):
        self.after_remote_learning_drop_off["rate"] = int(drop_off_rate)
        self.after_remote_learning_drop_off["remote"] = int(remote_reason_rate)
