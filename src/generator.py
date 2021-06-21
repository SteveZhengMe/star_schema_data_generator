from random import randint

import tkinter as tk

from main import Main
from parameters import Parameters
from guibaseclass import LabelInputCombo, LabelTwoInputCombo

class AppWindow(tk.Frame):
    summaryFrame = None
    activitiesDataTableFrame = None

    def __init__(self,parent):
        self.parent = parent
        self.parent.resizable(False, False)
        self.windowSelfConfig()
        self.createWidgets()

    def windowSelfConfig(self):
        self.parent.geometry('640x380+20+20')
        self.parent.title("Star Schema Data Generator")
    
    def createWidgets(self):
        first_label_size = 36
        conn_Str_size = 25
        first_input_size = 12
        second_input_size = 12
        self.professor_numbers = LabelInputCombo(self.parent,"Professors Number: ","300", size=(first_label_size,first_input_size), margin=(2,2))
        self.professor_numbers.pack(side="top", pady=(10,0), fill="both")

        self.studentEnrollmentYear = LabelTwoInputCombo(self.parent,"Student Enroll(Year): ", ("2015","2021"), " To ", size=(first_label_size,first_input_size,conn_Str_size,second_input_size), margin=(2,2))
        self.studentEnrollmentYear.pack(side="top", pady=(10,0), fill="both")

        self.courseNumbersPerProgram = LabelInputCombo(self.parent,"Courses Per-Program: ", "5", size=(first_label_size,first_input_size), margin=(2,2))
        self.courseNumbersPerProgram.pack(side="top", pady=(10,0), fill="both")

        self.remoteLearningStartsAt = LabelInputCombo(self.parent,"Hybrid Learning starts from(Year): ", "2019", size=(first_label_size,first_input_size), margin=(2,2))
        self.remoteLearningStartsAt.pack(side="top", pady=(10,0), fill="both")

        self.studentsNumber = LabelInputCombo(self.parent,"Students number Pre-Year: ", "15000", size=(first_label_size,first_input_size), margin=(2,2))
        self.studentsNumber.pack(side="top", pady=(10,0), fill="both")

        self.before = LabelTwoInputCombo(self.parent,"Before Hybrid Drop-Off(%): ", ("10","30"), ", because of remote(%): ", size=(first_label_size,first_input_size,conn_Str_size,second_input_size), margin=(2,2))
        self.before.pack(side="top", pady=(10,0), fill="both")

        self.after = LabelTwoInputCombo(self.parent,"After Hybrid Drop-Off(%): ", ("30","50"), ", because of remote(%): ", size=(first_label_size,first_input_size,conn_Str_size,second_input_size), margin=(2,2))
        self.after.pack(side="top", pady=(10,0), fill="both")

        self.runButton = tk.Button(self.parent, text="Run", command=self.runOnClick)
        self.runButton.pack(side="top", padx=(60,60), pady=(10,10), fill="both")

        self.resultMessage = tk.Label(self.parent, text="Based on the parameters, application may use more time, please be patient.", font=("Courier",9), fg="#f00", anchor="w")
        self.resultMessage.pack(side="top", padx=(60,60), pady=(30,10), fill="both")

    def checkValue(self):
        inputs = [
            self.professor_numbers,
            self.studentEnrollmentYear,
            self.courseNumbersPerProgram,
            self.remoteLearningStartsAt,
            self.studentsNumber,
            self.before,
            self.after
        ]

        for inputItem in inputs:
            errMsg = inputItem.selfCheck()
            if errMsg != None:
                self.resultMessage.config(text=errMsg)
                inputItem.focus()
                return False

        return True

    def runOnClick(self):
        if self.checkValue():
            parameters = Parameters()
            parameters.setProfessorNumber(self.professor_numbers.getInputValue())
            parameters.setStudentEnrollmentYear(self.studentEnrollmentYear.getInputValue()[0], self.studentEnrollmentYear.getInputValue()[1])
            courseNumberStart = int(int(self.courseNumbersPerProgram.getInputValue())*0.7)
            courseNumberEnd = int(int(self.courseNumbersPerProgram.getInputValue())*1.5)
            parameters.setCourseNumberPerProgram(courseNumberStart,courseNumberEnd)
            parameters.setRemoteLearningStartYear(self.remoteLearningStartsAt.getInputValue())
            parameters.setStudentNumber(self.studentsNumber.getInputValue())
            parameters.setBeforeRemoteLearningDropOffAndReasonRate(self.before.getInputValue()[0],self.before.getInputValue()[1])
            parameters.setAfterRemoteLearningDropOffAndReasonRate(self.after.getInputValue()[0],self.after.getInputValue()[1])

            generator = Main(parameters)

            # generate courses
            coursesList = generator.courseFactory()
            
            # generate Professors
            profList = generator.professorFactory()
            
            # Bind Programs and Professors
            for course in coursesList:
                course.setProf(profList[randint(0, len(profList)-1)])
            
            # Generate reasons
            reasonList = generator.generateDropOffReason()
            
            # Student enroll
            studentList = generator.studentFactory(reasonList)
            
            currList, dropOffList = generator.currFactory(studentList, coursesList)

            # Save them to csv
            export = {"prof_dim.csv":profList,"course_dim.csv":coursesList,"student_dim.csv":studentList,"drop_off_reason_dim.csv":reasonList,"curr_fact.csv":currList,"drop_off_fact.csv":dropOffList}
            for fileName, data in export.items():
                with open(fileName,"w") as file:
                    # print(data[0].exportHead())
                    file.write(data[0].exportHead())
                    for line in data:
                        file.write("\n%s" % line.exportData())

            self.resultMessage.config(text="Done")

if __name__ =="__main__":
    app = tk.Tk()
    AppWindow(app)
    app.mainloop()
