import tkinter
from tkinter import ttk
import os
from tkinter.messagebox import *
from generateinformation import *


class MjaWin:

    def _sampleback(self):
        self.entrylist = []
        for i in range(len(self.controllist)):
            if i % 2:
                self.entrylist.append(self.controllist[i])
        
        self.valueof = []

        for i in self.entrylist:
            if not i.get():
                showerror("WARNING", "You did not complete the information")
                return
            else:
                self.valueof.append(i.get())
        try:
            self.valueof[-1] = eval(self.valueof[-1])
            self.valueof[-2] = eval(self.valueof[-2])
        except NameError:
            showerror("WARNING", "You did not enter a number in the score input box")
        
        try:
            complte = geninformation(self.valueof)
        except ErrorOfInformation:
            showerror("WARNING", "You did not fill in the information correctly")

        with open(os.path.dirname(os.path.abspath(__file__)) + '\\information\main.txt', 'a+') as file:
            file.write('{}\t{}\t{}\t{}\t{}\t{}'.format(complte[0], complte[1], complte[2], complte[3], complte[4], complte[5]))
            showinfo('Tips', 'Submitted successfully')

    def _sample(self):
        samplewin = tkinter.Toplevel()
        samplewin.title('Add a sample')
        samplewin.iconphoto(False, self.logo)
        samplewin.geometry('600x256')
        
        difficult = tkinter.Label(samplewin,text="What do you think about the difficult of this exam/test")
        self.difficultcombobox = ttk.Combobox(samplewin)
        self.difficultcombobox['value'] = ('Easy', 'Normal', 'Hard')

        isreview = tkinter.Label(samplewin,text="Do you review exam content before you have this exam/test")
        self.isreviewcombobox = ttk.Combobox(samplewin)
        self.isreviewcombobox['value'] = ('Have reviewed', "Haven't reviewed")
        
        isexam = tkinter.Label(samplewin, text="Is it a exam or test")
        self.isexamcombobox = ttk.Combobox(samplewin)
        self.isexamcombobox['value'] = ('Mid/Final Exam', 'Test', 'Large scale examination')

        mentality = tkinter.Label(samplewin, text="How are you feeling before the exam/test")
        self.mentalitycombobox = ttk.Combobox(samplewin)
        self.mentalitycombobox['value'] = ('Very good', 'Good', 'Normal', 'Bad', 'Very bad')

        unexpectedly = tkinter.Label(samplewin, text="Is this a sudden test")
        self.unexpectedlycombobox = ttk.Combobox(samplewin)
        self.unexpectedlycombobox['value'] = ('Yes', 'No')

        score = tkinter.Label(samplewin, text="Please input your score.")
        self.scorecombobox = ttk.Entry(samplewin)

        fullscore = tkinter.Label(samplewin, text="Please enter the full score of this test/exam")
        self.fullscorecombobox = ttk.Entry(samplewin)

        self.controllist = [difficult, self.difficultcombobox,
        isreview,self.isreviewcombobox,
        isexam,self.isexamcombobox,
        mentality,self.mentalitycombobox,
        unexpectedly,self.unexpectedlycombobox,
        score, self.scorecombobox,
        fullscore, self.fullscorecombobox]
        
        cnt = 0
        
        buttonenter = tkinter.Button(samplewin, text="Submit sample", command=self._sampleback)
        for control in self.controllist:
            if cnt % 2 == 0:
                control.grid(column=0, row=cnt)
                
                
            else:
                control.grid(column=1, row=cnt-1)
            cnt+=1
        buttonenter.grid(row=cnt+1, column=0)
        samplewin.mainloop()
        
    def __init__(self):
        mainwin = tkinter.Tk()
        self.logo = tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+'\\logo.png')
        mainwin.title("Mja Predict Grades")
        mainwin.iconphoto(False, self.logo)
        
        mainwin.geometry('200x100')
        addpair = tkinter.Button(mainwin, text='Add a sample', command=self._sample)
        futurescore = tkinter.Button(mainwin, text='Predict grades')
        for control in [addpair, futurescore]:
            control.pack()
        mainwin.mainloop()

