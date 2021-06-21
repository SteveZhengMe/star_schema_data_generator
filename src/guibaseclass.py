import tkinter as tk

class LabelInputBaseClass(tk.Frame):
    def isNumber(self,input):
        try:
            if input=='NaN' or input=="":
                return False
            float(input)
        except ValueError:
            return False
        else:
            return True

    def selfCheck(self):
        if isinstance(self, LabelInputCombo):
            if not self.isNumber(self.getInputValue()):
                return self.getErrorMsg()
            else:
                return None

        if isinstance(self, LabelTwoInputCombo):
            if not self.isNumber(self.getInputValue()[0]) or not self.isNumber(self.getInputValue()[1]):
                return self.getErrorMsg()
            else:
                return None
    
    def getErrorMsg(self):
        return "Please input a number in " + self.label["text"]

    # When focus, focus the input box
    def focus(self):
        self.input.focus()
    

class LabelInputCombo(LabelInputBaseClass):
    def __init__(self, parent, labelName="Label Name", defaultValue="", entryState="normal", packSide="left", size=(0,0), margin=(0,0),*args,**kw):
        super().__init__(master=parent, *args, **kw)
        
        # Create label and pack
        self.label = tk.Label(self, text=labelName, font=("Courier",9), fg="#333", anchor="e")
        if size[0] != None:
            self.label.config(width=size[0])
        self.label.pack(side=packSide, padx=(margin[0],0), pady=margin[1])
        
        # Create input and pack
        self.inputValue = tk.StringVar()
        self.input = tk.Entry(self, textvariable=self.inputValue, state=entryState)
        if size[1] != None:
            self.input.config(width=size[1])
        self.input.insert(0,defaultValue)
        self.input.pack(side=packSide, padx=(0,margin[0]), pady=margin[1])
    
    # Return the input value
    def getInputValue(self):
        return self.inputValue.get()

class LabelTwoInputCombo(LabelInputBaseClass):
    def __init__(self, parent, labelName="Label Name", defaultValue="", connectionString = "->", entryState="normal", packSide="left", size=(0,0,0,0), margin=(0,0),*args,**kw):
        super().__init__(master=parent, *args, **kw)
        
        # Create label and pack
        self.label = tk.Label(self, text=labelName, font=("Courier",9), fg="#333", anchor="e")
        if size[0] != None:
            self.label.config(width=size[0])
        self.label.pack(side=packSide, padx=(margin[0],0), pady=margin[1])
        
        # Create input and pack
        self.inputValueLeft = tk.StringVar()
        self.input = tk.Entry(self, textvariable=self.inputValueLeft, state=entryState)
        if size[1] != None:
            self.input.config(width=size[1])
        self.input.insert(0,defaultValue[0])
        self.input.pack(side=packSide, padx=(0,margin[0]), pady=margin[1])

        # Create connection String and pack
        self.conn = tk.Label(self, text=connectionString, font=("Courier",9), fg="#333", anchor="e")
        if size[2] != None:
            self.conn.config(width=size[2])
        self.conn.pack(side=packSide, padx=(margin[0],0), pady=margin[1])
        
        # Create input and pack
        self.inputValueRight = tk.StringVar()
        self.inputRight = tk.Entry(self, textvariable=self.inputValueRight, state=entryState)
        if size[3] != None:
            self.inputRight.config(width=size[3])
        self.inputRight.insert(0,defaultValue[1])
        self.inputRight.pack(side=packSide, padx=(0,margin[0]), pady=margin[1])
    
    # Return the input value
    def getInputValue(self):
        return self.inputValueLeft.get(), self.inputValueRight.get()