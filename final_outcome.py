#VERSION 54 (at home as of October 13)
#importing Tkinter and ttk
#must remove ttk if formatting a widget
#need to make sure student cannot proceed if name is invalid and if year level/school is not selected
#NO MORE IMAGES IN MY PROGRAM
#changed subject frame colours for Kristin year 11 option
#adding in Kristin Year 13 subjects, fixed the comboboxes, added radiobuttons for Year 13 windows

#---------------------------------------------------------this program shows what the set up should look like even though it is not done, it is the general idea of what it is supposed to look like--------------------------------------------------------------

from tkinter import *
import ttk #enables me to use comboboxes (drop down widget)
import tkMessageBox #this enables a message to appear when a student enters an invalid name or does not follow the instructions given on the screen

#-------------------------------------------------------------------------------

#creating the window of the program
root = Tk()
root.title("untitled") #I don't have a name for it yet

#-------------------------------------------------------------------------------
#made empty variables so that the student's name, school and year level that the student has typed/chosen is stored in these variables
name = " " 
school = " " 
year_level = " "
class Window():
    """The Window class runs all the methods. There is a method for updating and displaying the student's name on the program, a big method which allows the student to enter their name and select their school/year levels, a method which gets rid of the content shown on the window and methods which allows students to pick their subjects. """
    """In all methods I have made attributes so that they can be used in other methods (eg self.root = root // root can be used as the parent in other methods)"""
    def update_name(self): #creating a function to get the student's name stored in the 'name' variable and shown in the program
        global name #so that the 'name' variable can be used in this function and the updated name works outside the function
        
        #.isalpha() means the data entered is in letters
        if len(self.name_text.get()) < 2 and self.name_text.get().isalpha(): 
            self.name_show.set("ERROR")
            tkMessageBox.showinfo("NAME ERROR", "Sorry, the name you entered is too short, please try again.") #appears if a student tries to enter a name less than 2 characters and the text is in letters (no special characters or numbers)
        elif len(self.name_text.get()) == 0: 
            tkMessageBox.showinfo("NAME ERROR", "Sorry, you must enter a name between 2-15 characters.") #appears if a student does not enter their name
        elif len(self.name_text.get()) > 15 and self.name_text.get().isalpha(): 
            self.name_show.set("ERROR")
            tkMessageBox.showinfo("NAME ERROR", "Sorry, the name you entered is too long, please try again.") #appears if a student tries to enter a name more than 15 characters and the text is in letters (no special characters or numbers)
        elif not self.name_text.get().isalpha(): 
            self.name_show.set("ERROR")
            tkMessageBox.showinfo("NAME ERROR", "Sorry, you can only enter your name using letters, please try again.") #appears if a student tries to enter a name by using other characters (and not letters)
        else: #if a student enters a valid name
            name = self.name_text.get() #made a variable which stores the name that the student has typed in the entry box
            name_string = "Hello {}!".format(name) #the new name is shown on the label that was initially blank
            self.name_show.set(name_string)
    
    def __init__(self, root): #made a function for the window of the program
        self.root = root #made a root attribute so I can use the 'root = Tk()' code from outside the Window class"
        self.root.geometry('{}x{}'.format(900,750)) #first number is the width, second is the length
        self.root.configure(background='powderBlue') #made the background of the window blue
        
        #---------------------------------FRAME ONE-------------------------------------
        
        #creating the first frame to group the main heading and the window together
        self.frame1 = Frame(self.root, bg='lightSteelBlue')
        self.frame1.grid(row=0, column=1, padx=285, pady=20, sticky="NSEW")
        
        #creating a heading of the opening window (set up stage)
        greeting_label1 = Label(self.frame1, text="WELCOME", bg='lightSteelBlue')
        greeting_label1.grid(row=1, column=1, padx=153, pady=20)
        
        #show student name
        self.name_show = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers) #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
        self.name_show.set("Hello!") #this is what appears on the window before the student has entered their name
        
        show_label = Label(self.frame1, textvariable=self.name_show, bg='lightSteelBlue')
        show_label.grid(row=2, column=1, padx=85, pady=15, sticky="NSEW")        

        #creating a String variable so that the student's name can be stored
        self.name_text = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers) #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
        self.name_text.set=(" ") #this is made blank because when the student first sees the screen their name would not appear
        
        #---------------------------------FRAME TWO-------------------------------------
        
        #creating the second frame for the name entry and submit button
        self.frame2 = Frame(self.root, bg='cadetBlue')
        self.frame2.grid(row=3, column=1, padx=285, pady=20, sticky="NSEW")   
        
        #creating a message instructing the student to enter their name
        name_message_text= StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers) #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
        name_message_text.set("PLEASE ENTER YOUR NAME BELOW")
        
        name_message_label = Label(self.frame2, textvariable=name_message_text, bg='cadetBlue')
        name_message_label.grid(row=4, column=1, padx=85, pady=20, sticky="NSEW")  
        
        #creating a text field where the student can type their name in
        name_entry = ttk.Entry(self.frame2, textvariable=self.name_text)
        name_entry.grid(row=5, column=1, padx=85, pady=5, sticky="NSEW")
        
        #creating a button which allows the student to display their name on the screen
        submit_button1 = Button(self.frame2, text="SUBMIT", bg='gainsboro', command=self.update_name)
        submit_button1.grid(row=6, column=1, padx=85, pady=20, sticky="NSEW")
        
        
        #-------------------------------FRAME THREE-------------------------------------
        
        #creating the third frame for the first combobox (selecting the school)
        self.frame3 = Frame(self.root, bg='dodgerBlue')
        self.frame3.grid(row=7, column=1, padx=285, pady=20, sticky="NSEW")
        
        #creating a label for the first combobox
        school_label = Label(self.frame3, text="PLEASE SELECT YOUR SCHOOL", bg='dodgerBlue')
        school_label.grid(row=8, column=1, padx=100, pady=10, sticky="NSEW")
        
        #setting up variables and option list for the school combobox
        school_names = ["Carmel College", "Kristin School"] #made a list which contains the schools the student can select // appearance of program is dependent on this
        self.chosen_school = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers) #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
        self.chosen_school.set("[PLEASE SELECT]")
        
        #creating a combobox (dropdown menu) for the student to choose their school
        school_box = ttk.Combobox(self.frame3, textvariable=self.chosen_school, state="readonly")
        school_box['values'] = school_names #this means that the drop down contains the schools listed in the list
        school_box.grid(row=9, column=1, padx=90, pady=20, sticky="NSEW")      
        
        #--------------------------------FRAME FOUR-------------------------------------
        
        #creating fourth frame for the second combobox, choosing year levels
        self.frame4 = Frame(self.root, bg='slateBlue')
        self.frame4.grid(row=10, column=1, padx=285, pady=20, sticky="NSEW")
        
        year_label = Label(self.frame4, text="PLEASE SELECT YOUR YEAR LEVEL:", bg='slateBlue')
        year_label.grid(row=11, column=1, padx=95, pady=10, sticky="NSEW")
        
        #setting up variables and option list for year level combobox
        year_levels = ["Year 11", "Year 12", "Year 13"] #made a list which contains the year levels the student can select // appearance of program is dependent on this
        self.chosen_year = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers) #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
        self.chosen_year.set("[PLEASE SELECT]")
        
        #creating a combobox for the student to select their year level
        self.year_box = ttk.Combobox(self.frame4, textvariable=self.chosen_year, state="readonly")
        self.year_box['values'] = year_levels #this means that the drop drown contains the year levels listed in the list
        self.year_box.grid(row=12, column=1, padx=80, pady=20, sticky="NSEW")
        
        #--------------------------------FRAME FIVE-------------------------------------
        
        #creating a fifth frame for the next button
        self.frame5 = Frame(self.root, bg='paleTurquoise')
        self.frame5.grid(row=13, column=1, padx=285, pady=20, sticky="NSEW")
        
        next_button1 = Button(self.frame5, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy, self.new_window_one]]) #the lambda function enables more than one function to be executed at the same time
        next_button1.grid(row=14, column=1, padx=165, pady=20, sticky="NSEW")
        #Lambda code is from https://stackoverflow.com/questions/13865009/have-multiple-commands-when-button-is-pressed
        
    def destroy(self): #made a function that gets rid of everything on the screen once the student clicks next
        #https://www.daniweb.com/programming/software-development/threads/386718/clear-and-replace-all-widgets-on-tkinter-frame --> SITE WHERE I GOT THE EXAMPLE CODE FOR DESTROYING FRAMES
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
            
    def new_window_one(self): #made a function that shows the next 'page' of the program
        #made variables have a global scope as these variables were created outside of the Window class
        global school, year_level
        #the .get() function means that whatever name has been entered or whatever school/year level has been selected, that data is stored in the variables below
        school = self.chosen_school.get()
        year_level = self.chosen_year.get()
                        
        if school == "Carmel College":
            self.root.configure(background='crimson') 
            
            #creating the first frame for the heading
            self.frame1 = Frame(root, bg='crimson')
            self.frame1.grid(row=0, column=0, columnspan=2, padx=285, pady=40, sticky="NSEW")
            
            self.greeting_label1 = Label(self.frame1, text="CHOOSE YOUR SUBJECTS AND STANDARDS", bg='crimson')
            self.greeting_label1.grid(row=1, column=1, padx=50, pady=20)    
            
            if year_level == "Year 11":              
                
                subjects = ["Accounting", "Digital Technology", "Drama", "Economics", "English", "French", "Food Technology", "Geography", "History", "Material Technology", "Mathematics", "Music", "Physical Education", "Science", "Te Reo Maori", "Visual Art"] #made a list which contains the Year 11 subjects that can be taken at Carmel
                chosen_subjects_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_one.set("[PLEASE SELECT]") 
                chosen_subjects_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_two.set("[PLEASE SELECT]")             
                #-----------------------------------------------------------------------------------------------
                self.subject_frame1 = Frame(self.root, bg='darkRed')
                self.subject_frame1.grid(row=10, column=0, padx=48, pady=20)
                    
                self.subject_label1 = Label(self.subject_frame1, text="Subject One")
                self.subject_label1.grid(row=11, column=1, padx=80, pady=10)
            
                #choose first subject
                self.subject_one_box = ttk.Combobox(self.subject_frame1, textvariable=chosen_subjects_one, state="readonly")
                self.subject_one_box['values'] = subjects
                self.subject_one_box.grid(row=12, column=1, padx=20, pady=10) 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame2 = Frame(self.root, bg='darkRed')
                self.subject_frame2.grid(row=10, column=1, padx=48, pady=20)
        
                self.subject_label2 = Label(self.subject_frame2, text="Subject Two")
                self.subject_label2.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose second subject
                self.subject_two_box = ttk.Combobox(self.subject_frame2, textvariable=chosen_subjects_two, state="readonly")
                self.subject_two_box['values'] = subjects
                self.subject_two_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
                #-----------------------------------------------------------------------------------------------
                #making radiobuttons for subject one's standards // radiobuttons are like circular checkboxes
                subject_one_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_one_choose_one = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_one)
                subject_one_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_one_choose_two = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_two)
                subject_one_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_one_choose_three = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_three)
                subject_one_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_one_choose_four = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_four)
                subject_one_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_one_choose_five = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_five)
                subject_one_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_one_choose_six = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_six)
                subject_one_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject two's standards // radiobuttons are like circular checkboxes
                subject_two_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)                
                
                subject_two_choose_one = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_one)
                subject_two_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_two_choose_two = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_two)
                subject_two_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_two_choose_three = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_three)
                subject_two_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_two_choose_four = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_four)
                subject_two_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_two_choose_five = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_five)
                subject_two_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_two_choose_six = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_six)
                subject_two_choose_six.grid(row=18, column=0, padx=30, pady=10) 
                
                #-----------------------------------------------------------------------------------------------
                self.button_frame1 = Frame(self.root, bg='maroon')
                self.button_frame1.grid(row=18, column=0, columnspan=2, padx=48, pady=20)  
                
                next_button1 = Button(self.button_frame1, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_one, self.new_window_two]])
                next_button1.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW")            
                                
            elif year_level == "Year 12":
                
                #setting up variables for the subject option combobox
                subjects = ["Accounting", "Art History", "Biology", "Chemistry", "Digital Technology", "Drama", "Economics", "English", "French", "Food Technology", "Geography", "History", "Material Technology", "Mathematics", "Music", "Photography", "Physical Education", "Physics", "Te Reo Maori", "Tourism", "Visual Art"] #made a list which contains the Year 12 subjects that can be taken at Carmel
                chosen_subjects_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_one.set("[PLEASE SELECT]") 
                chosen_subjects_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_two.set("[PLEASE SELECT]")             
                #-----------------------------------------------------------------------------------------------
                self.subject_frame1 = Frame(self.root, bg='darkRed')
                self.subject_frame1.grid(row=10, column=0, padx=48, pady=20)
                    
                self.subject_label1 = Label(self.subject_frame1, text="Subject One")
                self.subject_label1.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose first subject
                self.subject_one_box = ttk.Combobox(self.subject_frame1, textvariable=chosen_subjects_one, state="readonly")
                self.subject_one_box['values'] = subjects
                self.subject_one_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame2 = Frame(self.root, bg='darkRed')
                self.subject_frame2.grid(row=10, column=1, padx=48, pady=20)
        
                self.subject_label2 = Label(self.subject_frame2, text="Subject Two")
                self.subject_label2.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose second subject
                self.subject_two_box = ttk.Combobox(self.subject_frame2, textvariable=chosen_subjects_two, state="readonly")
                self.subject_two_box['values'] = subjects
                self.subject_two_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
                #-----------------------------------------------------------------------------------------------
                #making radiobuttons for subject one's standards // radiobuttons are like circular checkboxes
                subject_one_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_one_choose_one = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_one)
                subject_one_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_one_choose_two = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_two)
                subject_one_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_one_choose_three = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_three)
                subject_one_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_one_choose_four = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_four)
                subject_one_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_one_choose_five = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_five)
                subject_one_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_one_choose_six = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_six)
                subject_one_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject two's standards // radiobuttons are like circular checkboxes
                subject_two_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)                
                
                subject_two_choose_one = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_one)
                subject_two_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_two_choose_two = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_two)
                subject_two_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_two_choose_three = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_three)
                subject_two_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_two_choose_four = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_four)
                subject_two_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_two_choose_five = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_five)
                subject_two_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_two_choose_six = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_six)
                subject_two_choose_six.grid(row=18, column=0, padx=30, pady=10) 
                
                #-----------------------------------------------------------------------------------------------
                self.button_frame1 = Frame(self.root, bg='maroon')
                self.button_frame1.grid(row=18, column=0, columnspan=2, padx=48, pady=20) 
                
                next_button1 = Button(self.button_frame1, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_one, self.new_window_two]])
                next_button1.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW")              
                
            elif year_level == "Year 13":
                    
                subjects = ["Accounting", "Art History", "Biology", "Calculus", "Chemistry", "Classical Studies", "Design", "Digital Technology", "Drama", "Economics", "English (Core)", "English (Visual)", "Food Technology", "French", "Geography", "History", "Hospitality", "Material Technology", "Music", "Photography", "Physical Education", "Physics", "Statistics", "Te Reo", "Tourism", "Visual Art (Painting)", "STUDY"] #made a list which contains the Year 13 subjects that can be taken at Carmel
                chosen_subjects_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_one.set("[PLEASE SELECT]") 
                chosen_subjects_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_two.set("[PLEASE SELECT]")             
                #-----------------------------------------------------------------------------------------------
                self.subject_frame1 = Frame(self.root, bg='darkRed')
                self.subject_frame1.grid(row=10, column=0, padx=48, pady=20)
                    
                self.subject_label1 = Label(self.subject_frame1, text="Subject One")
                self.subject_label1.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose first subject
                self.subject_one_box = ttk.Combobox(self.subject_frame1, textvariable=chosen_subjects_one, state="readonly")
                self.subject_one_box['values'] = subjects
                self.subject_one_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame2 = Frame(self.root, bg='darkRed')
                self.subject_frame2.grid(row=10, column=1, padx=48, pady=20)
        
                self.subject_label2 = Label(self.subject_frame2, text="Subject Two")
                self.subject_label2.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose second subject
                self.subject_two_box = ttk.Combobox(self.subject_frame2, textvariable=chosen_subjects_two, state="readonly")
                self.subject_two_box['values'] = subjects
                self.subject_two_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
               #-----------------------------------------------------------------------------------------------
                #making radiobuttons for subject one's standards // radiobuttons are like circular checkboxes
                subject_one_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_one_choose_one = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_one)
                subject_one_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_one_choose_two = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_two)
                subject_one_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_one_choose_three = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_three)
                subject_one_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_one_choose_four = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_four)
                subject_one_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_one_choose_five = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_five)
                subject_one_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_one_choose_six = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_six)
                subject_one_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject two's standards // radiobuttons are like circular checkboxes
                subject_two_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)                
                
                subject_two_choose_one = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_one)
                subject_two_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_two_choose_two = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_two)
                subject_two_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_two_choose_three = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_three)
                subject_two_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_two_choose_four = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_four)
                subject_two_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_two_choose_five = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_five)
                subject_two_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_two_choose_six = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_six)
                subject_two_choose_six.grid(row=18, column=0, padx=30, pady=10) 
                
                #-----------------------------------------------------------------------------------------------
                self.button_frame1 = Frame(self.root, bg='maroon')
                self.button_frame1.grid(row=18, column=0, columnspan=2, padx=48, pady=20)    
                
                next_button1 = Button(self.button_frame1, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_one, self.new_window_two]])
                next_button1.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW") 
                
            else:
                pass
        elif school == "Kristin School":
            self.root.configure(background='paleTurquoise')
            self.frame1 = Frame(root, bg='paleTurquoise')
            self.frame1.grid(row=0, column=0, columnspan=2, padx=285, pady=40, sticky="NSEW")
            
            self.greeting_label1 = Label(self.frame1, text="CHOOSE YOUR SUBJECTS AND STANDARDS", bg='paleTurquoise')
            self.greeting_label1.grid(row=1, column=1, padx=50, pady=20)   
            
            if year_level == "Year 11":
                #setting up variables for the subject option combobox
                subjects = ["Art", "Business Studies (Accounting)", "Chinese", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "French", "Further Science (extension)", "Geography", "Graphics", "Hard Tech (Woodwork)", "History", "Japanese", "Mathematics", "Media Studies", "Music", "Physical Education/Health (Core)", "Physical Education (Optional)", "Science", "Spanish", "Soft Technology (Materials)"] #made a list which contains the Year 11 subjects that can be taken at Kristin
                chosen_subjects_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_one.set("[PLEASE SELECT]") 
                chosen_subjects_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_two.set("[PLEASE SELECT]")             
                #-----------------------------------------------------------------------------------------------
                self.subject_frame1 = Frame(self.root, bg='teal')
                self.subject_frame1.grid(row=10, column=0, padx=48, pady=20)
                    
                self.subject_label1 = Label(self.subject_frame1, text="Subject One")
                self.subject_label1.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose first subject
                self.subject_one_box = ttk.Combobox(self.subject_frame1, textvariable=chosen_subjects_one, state="readonly")
                self.subject_one_box['values'] = subjects
                self.subject_one_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame2 = Frame(self.root, bg='teal')
                self.subject_frame2.grid(row=10, column=1, padx=48, pady=20)
        
                self.subject_label2 = Label(self.subject_frame2, text="Subject Two")
                self.subject_label2.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose second subject
                self.subject_two_box = ttk.Combobox(self.subject_frame2, textvariable=chosen_subjects_two, state="readonly")
                self.subject_two_box['values'] = subjects
                self.subject_two_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
                #-----------------------------------------------------------------------------------------------
                #making radiobuttons for subject one's standards // radiobuttons are like circular checkboxes
                subject_one_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_one_choose_one = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_one)
                subject_one_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_one_choose_two = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_two)
                subject_one_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_one_choose_three = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_three)
                subject_one_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_one_choose_four = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_four)
                subject_one_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_one_choose_five = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_five)
                subject_one_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_one_choose_six = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_six)
                subject_one_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject two's standards // radiobuttons are like circular checkboxes
                subject_two_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)                
                
                subject_two_choose_one = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_one)
                subject_two_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_two_choose_two = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_two)
                subject_two_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_two_choose_three = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_three)
                subject_two_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_two_choose_four = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_four)
                subject_two_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_two_choose_five = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_five)
                subject_two_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_two_choose_six = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_six)
                subject_two_choose_six.grid(row=18, column=0, padx=30, pady=10) 
                
                #-----------------------------------------------------------------------------------------------
                self.button_frame1 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame1.grid(row=18, column=0, columnspan=2, padx=48, pady=20)                    
                
                next_button1 = Button(self.button_frame1, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_one, self.new_window_two]])
                next_button1.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW")
                
            elif year_level == "Year 12":
               
                #setting up variables for the subject option combobox
                subjects = ["Art", "Biology", "Business Studies (Accounting)", "Chemistry", "Chinese", "Classical Studies", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "Food Tech", "French", "Geography", "Graphics", "Hard Tech (Woodwork)", "History", "Japanese", "Mathematics", "Mathematics Applied", "Media Studies", "Music", "Outdoor Education", "Photography", "Physical Education/Health (Core)", "Physical Education (Optional)", "Physics", "Spanish", "Soft Technology (Materials)"] #made a list which contains the Year 12 subjects that can be taken at Kristin
                chosen_subjects_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_one.set("[PLEASE SELECT]") 
                chosen_subjects_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_two.set("[PLEASE SELECT]")             
                #-----------------------------------------------------------------------------------------------
                self.subject_frame1 = Frame(self.root, bg='teal')
                self.subject_frame1.grid(row=10, column=0, padx=48, pady=20)
                    
                self.subject_label1 = Label(self.subject_frame1, text="Subject One")
                self.subject_label1.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose first subject
                self.subject_one_box = ttk.Combobox(self.subject_frame1, textvariable=chosen_subjects_one, state="readonly")
                self.subject_one_box['values'] = subjects
                self.subject_one_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame2 = Frame(self.root, bg='teal')
                self.subject_frame2.grid(row=10, column=1, padx=48, pady=20)
        
                self.subject_label2 = Label(self.subject_frame2, text="Subject Two")
                self.subject_label2.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose second subject
                self.subject_two_box = ttk.Combobox(self.subject_frame2, textvariable=chosen_subjects_two, state="readonly")
                self.subject_two_box['values'] = subjects
                self.subject_two_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
                #-----------------------------------------------------------------------------------------------
                #making radiobuttons for subject one's standards // radiobuttons are like circular checkboxes
                subject_one_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_one_choose_one = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_one)
                subject_one_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_one_choose_two = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_two)
                subject_one_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_one_choose_three = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_three)
                subject_one_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_one_choose_four = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_four)
                subject_one_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_one_choose_five = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_five)
                subject_one_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_one_choose_six = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_six)
                subject_one_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject two's standards // radiobuttons are like circular checkboxes
                subject_two_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)                
                
                subject_two_choose_one = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_one)
                subject_two_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_two_choose_two = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_two)
                subject_two_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_two_choose_three = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_three)
                subject_two_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_two_choose_four = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_four)
                subject_two_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_two_choose_five = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_five)
                subject_two_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_two_choose_six = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_six)
                subject_two_choose_six.grid(row=18, column=0, padx=30, pady=10) 
                
                #-----------------------------------------------------------------------------------------------
                self.button_frame1 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame1.grid(row=18, column=0, columnspan=2, padx=48, pady=20)                    
                          
                next_button1 = Button(self.button_frame1, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_one, self.new_window_two]])
                next_button1.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW")    
                
            elif year_level == "Year 13":
                #setting up variables for the subject option combobox
                subjects = ["Biology", "Business Studies (Accounting)", "Calculus", "Chemistry", "Chinese", "Classical Studies", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "French", "Geography", "Graphics", "Hard Tech (Woodwork)", "Health (Optional)", "History", "Japanese", "Media Studies", "Music", "Outdoor Education", "Painting", "Photography", "Physical Education (Optional)", "Physics", "Statistics", "Soft Technology (Materials)"] #made a list which contains the Year 13 subjects that can be taken at Kristin
                chosen_subjects_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_one.set("[PLEASE SELECT]") 
                chosen_subjects_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_two.set("[PLEASE SELECT]")             
                #----------------------------------------------------------------------------------------------- 
                self.subject_frame1 = Frame(self.root, bg='teal')
                self.subject_frame1.grid(row=10, column=0, padx=48, pady=20)
                    
                self.subject_label1 = Label(self.subject_frame1, text="Subject One")
                self.subject_label1.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose first subject
                self.subject_one_box = ttk.Combobox(self.subject_frame1, textvariable=chosen_subjects_one, state="readonly")
                self.subject_one_box['values'] = subjects
                self.subject_one_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame2 = Frame(self.root, bg='teal')
                self.subject_frame2.grid(row=10, column=1, padx=48, pady=20)
        
                self.subject_label2 = Label(self.subject_frame2, text="Subject Two")
                self.subject_label2.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose second subject
                self.subject_two_box = ttk.Combobox(self.subject_frame2, textvariable=chosen_subjects_two, state="readonly")
                self.subject_two_box['values'] = subjects
                self.subject_two_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
                #-----------------------------------------------------------------------------------------------
                #making radiobuttons for subject one's standards // radiobuttons are like circular checkboxes
                subject_one_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_one_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_one_choose_one = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_one)
                subject_one_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_one_choose_two = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_two)
                subject_one_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_one_choose_three = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_three)
                subject_one_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_one_choose_four = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_four)
                subject_one_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_one_choose_five = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_five)
                subject_one_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_one_choose_six = ttk.Radiobutton(self.subject_frame1, variable=subject_one_standard_six)
                subject_one_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject two's standards // radiobuttons are like circular checkboxes
                subject_two_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_two_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)                
                
                subject_two_choose_one = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_one)
                subject_two_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_two_choose_two = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_two)
                subject_two_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_two_choose_three = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_three)
                subject_two_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_two_choose_four = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_four)
                subject_two_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_two_choose_five = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_five)
                subject_two_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_two_choose_six = ttk.Radiobutton(self.subject_frame2, variable=subject_two_standard_six)
                subject_two_choose_six.grid(row=18, column=0, padx=30, pady=10) 
                
                #-----------------------------------------------------------------------------------------------
                self.button_frame1 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame1.grid(row=18, column=0, columnspan=2, padx=48, pady=20)                    
                          
                next_button1 = Button(self.button_frame1, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_one, self.new_window_two]])
                next_button1.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW")       
        else:
            self.frame1.destroy()
            self.__init__(root) #calls the main window function if the student has not entered any data into the program
            tkMessageBox.showinfo("ERROR", "Sorry {}, you didn't select your school and year level, please try again.".format(name))
            #Message Box code from https://www.tutorialspoint.com/python/tk_messagebox.htm
    
    def destroy_window_one(self): #gets rid of all the content from the subject one/two page
        self.frame1.destroy()
        self.subject_frame1.destroy() 
        self.subject_frame2.destroy()   
        self.button_frame1.destroy()
        
    def new_window_two(self):
        #made variables have a global scope as these variables were created outside of the Window class
        global school, year_level
        #the .get() function means that whatever name has been entered or whatever school/year level has been selected, that data is stored in the variables below
        school = self.chosen_school.get()
        year_level = self.chosen_year.get()       
                
        if school == "Carmel College":
            self.root.configure(background='crimson')
            
            #creating the first frame for the heading            
            self.frame2 = Frame(root, bg='crimson')
            self.frame2.grid(row=0, column=0, columnspan=2, padx=285, pady=40, sticky="NSEW")
             
            self.greeting_label2 = Label(self.frame2, text="CHOOSE YOUR SUBJECTS AND STANDARDS", bg='crimson')
            self.greeting_label2.grid(row=1, column=1, padx=50, pady=20)  
            
            if year_level == "Year 11":
                        
                subjects = ["Accounting", "Digital Technology", "Drama", "Economics", "English", "French", "Food Technology", "Geography", "History", "Material Technology", "Mathematics", "Music", "Physical Education", "Science", "Te Reo Maori", "Visual Art"] #made a list which contains the Year 11 subjects that can be taken at Carmel
                chosen_subjects_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_three.set("[PLEASE SELECT]")             
                chosen_subjects_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_four.set("[PLEASE SELECT]")              
                #-----------------------------------------------------------------------------------------------
                self.subject_frame3 = Frame(self.root, bg='darkRed')
                self.subject_frame3.grid(row=10, column=0, padx=48, pady=20)
                            
                self.subject_label3 = Label(self.subject_frame3, text="Subject Three")
                self.subject_label3.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose third subject
                self.subject_three_box = ttk.Combobox(self.subject_frame3, textvariable=chosen_subjects_three, state="readonly")
                self.subject_three_box['values'] = subjects
                self.subject_three_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame4 = Frame(self.root, bg='darkRed')
                self.subject_frame4.grid(row=10, column=1, padx=48, pady=20)
                
                self.subject_label4 = Label(self.subject_frame4, text="Subject Four")
                self.subject_label4.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose fourth subject
                self.subject_four_box = ttk.Combobox(self.subject_frame4, textvariable=chosen_subjects_four, state="readonly")
                self.subject_four_box['values'] = subjects
                self.subject_four_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                
                #---------------------------------------------------------------------------------------------------
                #making radiobuttons for subject three's standards // radiobuttons are like circular checkboxes
                subject_three_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_three_choose_one = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_one)
                subject_three_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_three_choose_two = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_two)
                subject_three_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_three_choose_three = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_three)
                subject_three_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_three_choose_four = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_four)
                subject_three_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_three_choose_five = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_five)
                subject_three_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_three_choose_six = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_six)
                subject_three_choose_six.grid(row=18, column=0, padx=30, pady=10)  
                
                #making radiobuttons for subject four's standards // radiobuttons are like circular checkboxes
                subject_four_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)       
                
                subject_four_choose_one = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_one)
                subject_four_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_four_choose_two = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_two)
                subject_four_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_four_choose_three = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_three)
                subject_four_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_four_choose_four = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_four)
                subject_four_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_four_choose_five = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_five)
                subject_four_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_four_choose_six = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_six)
                subject_four_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                #-----------------------------------------------------------------------------------------------
                self.button_frame2 = Frame(self.root, bg='maroon')
                self.button_frame2.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
                                            
                next_button2 = Button(self.button_frame2, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_two, self.new_window_three]])
                next_button2.grid(row=19, column=1, padx=80, pady=10, sticky="NSEW")             
                        
            elif year_level == "Year 12":
                        
                #setting up variables for the subject option combobox
                subjects = ["Accounting", "Art History", "Biology", "Chemistry", "Digital Technology", "Drama", "Economics", "English", "French", "Food Technology", "Geography", "History", "Material Technology", "Mathematics", "Music", "Photography", "Physical Education", "Physics", "Te Reo Maori", "Tourism", "Visual Art"] #made a list which contains the Year 12 subjects that can be taken at Carmel
                chosen_subjects_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_three.set("[PLEASE SELECT]")             
                chosen_subjects_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_four.set("[PLEASE SELECT]")              
                #-----------------------------------------------------------------------------------------------
                self.subject_frame3 = Frame(self.root, bg='darkRed')
                self.subject_frame3.grid(row=10, column=0, padx=48, pady=20)
                            
                self.subject_label3 = Label(self.subject_frame3, text="Subject Three")
                self.subject_label3.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose third subject
                self.subject_three_box = ttk.Combobox(self.subject_frame3, textvariable=chosen_subjects_three, state="readonly")
                self.subject_three_box['values'] = subjects
                self.subject_three_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame4 = Frame(self.root, bg='darkRed')
                self.subject_frame4.grid(row=10, column=1, padx=48, pady=20)
                
                self.subject_label4 = Label(self.subject_frame4, text="Subject Four")
                self.subject_label4.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose fourth subject
                self.subject_four_box = ttk.Combobox(self.subject_frame4, textvariable=chosen_subjects_four, state="readonly")
                self.subject_four_box['values'] = subjects
                self.subject_four_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                        
                #---------------------------------------------------------------------------------------------------
                #making radiobuttons for subject three's standards // radiobuttons are like circular checkboxes
                subject_three_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_three_choose_one = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_one)
                subject_three_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_three_choose_two = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_two)
                subject_three_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_three_choose_three = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_three)
                subject_three_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_three_choose_four = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_four)
                subject_three_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_three_choose_five = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_five)
                subject_three_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_three_choose_six = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_six)
                subject_three_choose_six.grid(row=18, column=0, padx=30, pady=10)  
                
                #making radiobuttons for subject four's standards // radiobuttons are like circular checkboxes
                subject_four_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)       
                
                subject_four_choose_one = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_one)
                subject_four_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_four_choose_two = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_two)
                subject_four_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_four_choose_three = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_three)
                subject_four_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_four_choose_four = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_four)
                subject_four_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_four_choose_five = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_five)
                subject_four_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_four_choose_six = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_six)
                subject_four_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                #-----------------------------------------------------------------------------------------------
                self.button_frame2 = Frame(self.root, bg='maroon')
                self.button_frame2.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
                                            
                next_button2 = Button(self.button_frame2, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_two, self.new_window_three]])
                next_button2.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")               
                
            elif year_level == "Year 13":
                
                subjects = ["Accounting", "Art History", "Biology", "Calculus", "Chemistry", "Classical Studies", "Design", "Digital Technology", "Drama", "Economics", "English (Core)", "English (Visual)", "Food Technology", "French", "Geography", "History", "Hospitality", "Material Technology", "Music", "Photography", "Physical Education", "Physics", "Statistics", "Te Reo", "Tourism", "Visual Art (Painting)", "STUDY"] #made a list which contains the Year 13 subjects that can be taken at Carmel     
                chosen_subjects_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_three.set("[PLEASE SELECT]")             
                chosen_subjects_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_four.set("[PLEASE SELECT]")              
                #-----------------------------------------------------------------------------------------------
                self.subject_frame3 = Frame(self.root, bg='darkRed')
                self.subject_frame3.grid(row=10, column=0, padx=48, pady=20)
                            
                self.subject_label3 = Label(self.subject_frame3, text="Subject Three")
                self.subject_label3.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose third subject
                self.subject_three_box = ttk.Combobox(self.subject_frame3, textvariable=chosen_subjects_three, state="readonly")
                self.subject_three_box['values'] = subjects
                self.subject_three_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame4 = Frame(self.root, bg='darkRed')
                self.subject_frame4.grid(row=10, column=1, padx=48, pady=20)
                
                self.subject_label4 = Label(self.subject_frame4, text="Subject Four")
                self.subject_label4.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose fourth subject
                self.subject_four_box = ttk.Combobox(self.subject_frame4, textvariable=chosen_subjects_four, state="readonly")
                self.subject_four_box['values'] = subjects
                self.subject_four_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                        
                #---------------------------------------------------------------------------------------------------
                #making radiobuttons for subject three's standards // radiobuttons are like circular checkboxes
                subject_three_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_three_choose_one = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_one)
                subject_three_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_three_choose_two = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_two)
                subject_three_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_three_choose_three = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_three)
                subject_three_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_three_choose_four = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_four)
                subject_three_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_three_choose_five = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_five)
                subject_three_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_three_choose_six = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_six)
                subject_three_choose_six.grid(row=18, column=0, padx=30, pady=10)  
                
                #making radiobuttons for subject four's standards // radiobuttons are like circular checkboxes
                subject_four_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)       
                
                subject_four_choose_one = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_one)
                subject_four_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_four_choose_two = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_two)
                subject_four_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_four_choose_three = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_three)
                subject_four_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_four_choose_four = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_four)
                subject_four_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_four_choose_five = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_five)
                subject_four_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_four_choose_six = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_six)
                subject_four_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                #-----------------------------------------------------------------------------------------------
                self.button_frame2 = Frame(self.root, bg='maroon')
                self.button_frame2.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
                                            
                next_button2 = Button(self.button_frame2, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_two, self.new_window_three]])
                next_button2.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")
                
            else:
                pass
        elif school == "Kristin School":
            self.root.configure(background='paleTurquoise')
            
            self.frame2 = Frame(root, bg='paleTurquoise')
            self.frame2.grid(row=0, column=0, columnspan=2, padx=285, pady=40, sticky="NSEW")
                     
            self.greeting_label2 = Label(self.frame2, text="CHOOSE YOUR SUBJECTS AND STANDARDS", bg='paleTurquoise')
            self.greeting_label2.grid(row=1, column=1, padx=50, pady=20)  
            
            if year_level == "Year 11":
                #setting up variables for the subject option combobox
                subjects = ["Art", "Business Studies (Accounting)", "Chinese", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "French", "Further Science (extension)", "Geography", "Graphics", "Hard Tech (Woodwork)", "History", "Japanese", "Mathematics", "Media Studies", "Music", "Physical Education/Health (Core)", "Physical Education (Optional)", "Science", "Spanish", "Soft Technology (Materials)"] #made a list which contains the Year 11 subjects that can be taken at Kristin
                chosen_subjects_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_three.set("[PLEASE SELECT]")             
                chosen_subjects_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_four.set("[PLEASE SELECT]")              
                #-----------------------------------------------------------------------------------------------
                self.subject_frame3 = Frame(self.root, bg='teal')
                self.subject_frame3.grid(row=10, column=0, padx=48, pady=20)
                            
                self.subject_label3 = Label(self.subject_frame3, text="Subject Three")
                self.subject_label3.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose third subject
                self.subject_three_box = ttk.Combobox(self.subject_frame3, textvariable=chosen_subjects_three, state="readonly")
                self.subject_three_box['values'] = subjects
                self.subject_three_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame4 = Frame(self.root, bg='teal')
                self.subject_frame4.grid(row=10, column=1, padx=48, pady=20)
                
                self.subject_label4 = Label(self.subject_frame4, text="Subject Four")
                self.subject_label4.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose fourth subject
                self.subject_four_box = ttk.Combobox(self.subject_frame4, textvariable=chosen_subjects_four, state="readonly")
                self.subject_four_box['values'] = subjects
                self.subject_four_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                        
                #---------------------------------------------------------------------------------------------------
                #making radiobuttons for subject three's standards // radiobuttons are like circular checkboxes
                subject_three_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_three_choose_one = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_one)
                subject_three_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_three_choose_two = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_two)
                subject_three_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_three_choose_three = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_three)
                subject_three_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_three_choose_four = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_four)
                subject_three_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_three_choose_five = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_five)
                subject_three_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_three_choose_six = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_six)
                subject_three_choose_six.grid(row=18, column=0, padx=30, pady=10)  
                
                #making radiobuttons for subject four's standards // radiobuttons are like circular checkboxes
                subject_four_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)       
                
                subject_four_choose_one = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_one)
                subject_four_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_four_choose_two = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_two)
                subject_four_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_four_choose_three = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_three)
                subject_four_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_four_choose_four = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_four)
                subject_four_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_four_choose_five = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_five)
                subject_four_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_four_choose_six = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_six)
                subject_four_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                #-----------------------------------------------------------------------------------------------
                self.button_frame2 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame2.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
                                            
                next_button2 = Button(self.button_frame2, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_two, self.new_window_three]])
                next_button2.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")    
                
            elif year_level == "Year 12":
               
                #setting up variables for the subject option combobox
                subjects = ["Art", "Biology", "Business Studies (Accounting)", "Chemistry", "Chinese", "Classical Studies", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "Food Tech", "French", "Geography", "Graphics", "Hard Tech (Woodwork)", "History", "Japanese", "Mathematics", "Mathematics Applied", "Media Studies", "Music", "Outdoor Education", "Photography", "Physical Education/Health (Core)", "Physical Education (Optional)", "Physics", "Spanish", "Soft Technology (Materials)"] #made a list which contains the Year 12 subjects that can be taken at Kristin
                chosen_subjects_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_three.set("[PLEASE SELECT]")             
                chosen_subjects_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_four.set("[PLEASE SELECT]")              
                #-----------------------------------------------------------------------------------------------
                self.subject_frame3 = Frame(self.root, bg='teal')
                self.subject_frame3.grid(row=10, column=0, padx=48, pady=20)
                            
                self.subject_label3 = Label(self.subject_frame3, text="Subject Three")
                self.subject_label3.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose third subject
                self.subject_three_box = ttk.Combobox(self.subject_frame3, textvariable=chosen_subjects_three, state="readonly")
                self.subject_three_box['values'] = subjects
                self.subject_three_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame4 = Frame(self.root, bg='teal')
                self.subject_frame4.grid(row=10, column=1, padx=48, pady=20)
                
                self.subject_label4 = Label(self.subject_frame4, text="Subject Four")
                self.subject_label4.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose fourth subject
                self.subject_four_box = ttk.Combobox(self.subject_frame4, textvariable=chosen_subjects_four, state="readonly")
                self.subject_four_box['values'] = subjects
                self.subject_four_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                        
                #---------------------------------------------------------------------------------------------------
                #making radiobuttons for subject three's standards // radiobuttons are like circular checkboxes
                subject_three_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_three_choose_one = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_one)
                subject_three_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_three_choose_two = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_two)
                subject_three_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_three_choose_three = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_three)
                subject_three_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_three_choose_four = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_four)
                subject_three_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_three_choose_five = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_five)
                subject_three_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_three_choose_six = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_six)
                subject_three_choose_six.grid(row=18, column=0, padx=30, pady=10)  
                
                #making radiobuttons for subject four's standards // radiobuttons are like circular checkboxes
                subject_four_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)       
                
                subject_four_choose_one = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_one)
                subject_four_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_four_choose_two = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_two)
                subject_four_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_four_choose_three = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_three)
                subject_four_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_four_choose_four = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_four)
                subject_four_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_four_choose_five = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_five)
                subject_four_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_four_choose_six = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_six)
                subject_four_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                #-----------------------------------------------------------------------------------------------
                self.button_frame2 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame2.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
                                            
                next_button2 = Button(self.button_frame2, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_two, self.new_window_three]])
                next_button2.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")   
                
            elif year_level == "Year 13":
                #setting up variables for the subject option combobox
                subjects = ["Biology", "Business Studies (Accounting)", "Calculus", "Chemistry", "Chinese", "Classical Studies", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "French", "Geography", "Graphics", "Hard Tech (Woodwork)", "Health (Optional)", "History", "Japanese", "Media Studies", "Music", "Outdoor Education", "Painting", "Photography", "Physical Education (Optional)", "Physics", "Statistics", "Soft Technology (Materials)"] #made a list which contains the Year 13 subjects that can be taken at Kristin 
                chosen_subjects_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_three.set("[PLEASE SELECT]")             
                chosen_subjects_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_four.set("[PLEASE SELECT]")              
                #-----------------------------------------------------------------------------------------------
                self.subject_frame3 = Frame(self.root, bg='teal')
                self.subject_frame3.grid(row=10, column=0, padx=48, pady=20)
                            
                self.subject_label3 = Label(self.subject_frame3, text="Subject Three")
                self.subject_label3.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose third subject
                self.subject_three_box = ttk.Combobox(self.subject_frame3, textvariable=chosen_subjects_three, state="readonly")
                self.subject_three_box['values'] = subjects
                self.subject_three_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame4 = Frame(self.root, bg='teal')
                self.subject_frame4.grid(row=10, column=1, padx=48, pady=20)
                
                self.subject_label4 = Label(self.subject_frame4, text="Subject Four")
                self.subject_label4.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                    
                #choose fourth subject
                self.subject_four_box = ttk.Combobox(self.subject_frame4, textvariable=chosen_subjects_four, state="readonly")
                self.subject_four_box['values'] = subjects
                self.subject_four_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")         
                        
                #---------------------------------------------------------------------------------------------------
                #making radiobuttons for subject three's standards // radiobuttons are like circular checkboxes
                subject_three_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_three_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_three_choose_one = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_one)
                subject_three_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_three_choose_two = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_two)
                subject_three_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_three_choose_three = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_three)
                subject_three_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_three_choose_four = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_four)
                subject_three_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_three_choose_five = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_five)
                subject_three_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_three_choose_six = ttk.Radiobutton(self.subject_frame3, variable=subject_three_standard_six)
                subject_three_choose_six.grid(row=18, column=0, padx=30, pady=10)  
                
                #making radiobuttons for subject four's standards // radiobuttons are like circular checkboxes
                subject_four_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_four_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)       
                
                subject_four_choose_one = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_one)
                subject_four_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_four_choose_two = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_two)
                subject_four_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_four_choose_three = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_three)
                subject_four_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_four_choose_four = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_four)
                subject_four_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_four_choose_five = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_five)
                subject_four_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_four_choose_six = ttk.Radiobutton(self.subject_frame4, variable=subject_four_standard_six)
                subject_four_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                #-----------------------------------------------------------------------------------------------
                self.button_frame2 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame2.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
                                            
                next_button2 = Button(self.button_frame2, text="NEXT", bg='gainsboro', command=lambda:[f() for f in [self.destroy_window_two, self.new_window_three]])
                next_button2.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")                
            #-
    def destroy_window_two(self): #gets rid of all the content from the subject three/four page
        self.frame2.destroy()
        self.subject_frame3.destroy() 
        self.subject_frame4.destroy() 
        self.button_frame2.destroy()
            
    def new_window_three(self):
        #made variables have a global scope as these variables were created outside of the Window class
        global school, year_level
        #the .get() function means that whatever name has been entered or whatever school/year level has been selected, that data is stored in the variables below
        school = self.chosen_school.get()
        year_level = self.chosen_year.get()
                        
        if school == "Carmel College":
            self.root.configure(background='crimson')
            
            #creating the first frame for the heading
            self.frame3 = Frame(root, bg='crimson')
            self.frame3.grid(row=0, column=0, columnspan=2, padx=285, pady=15, sticky="NSEW")
                       
            self.greeting_label3 = Label(self.frame3, text="CHOOSE YOUR SUBJECTS AND STANDARDS", bg='crimson')
            self.greeting_label3.grid(row=1, column=1, padx=50, pady=20)     
            
            if year_level == "Year 11":
                            
                subjects = ["Accounting", "Digital Technology", "Drama", "Economics", "English", "French", "Food Technology", "Geography", "History", "Material Technology", "Mathematics", "Music", "Physical Education", "Science", "Te Reo Maori", "Visual Art"] #made a list which contains the Year 11 subjects that can be taken at Carmel
                seventh_subject = ["Religious Education"]
                chosen_subjects_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_five.set("[PLEASE SELECT]")
                chosen_subjects_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_six.set("[PLEASE SELECT]")
                chosen_subjects_seven = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_seven.set(seventh_subject)
                #-----------------------------------------------------------------------------------------------
                self.subject_frame5 = Frame(self.root, bg='darkRed')
                self.subject_frame5.grid(row=10, column=0, padx=48)
                    
                self.subject_label5 = Label(self.subject_frame5, text="Subject Five")
                self.subject_label5.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose fifth subject
                self.subject_five_box = ttk.Combobox(self.subject_frame5, textvariable=chosen_subjects_five, state="readonly")
                self.subject_five_box['values'] = subjects
                self.subject_five_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame6 = Frame(self.root, bg='darkRed')
                self.subject_frame6.grid(row=10, column=1, padx=48)
                
                self.subject_label6 = Label(self.subject_frame6, text="Subject Six")
                self.subject_label6.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")                
                
                #choose sixth subject
                self.subject_six_box = ttk.Combobox(self.subject_frame6, textvariable=chosen_subjects_six, state="readonly")
                self.subject_six_box['values'] = subjects
                self.subject_six_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")                 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame7 = Frame(self.root, bg='darkRed')
                self.subject_frame7.grid(row=11, column=0, columnspan=2, padx=48, pady=20)
                
                self.subject_label7 = Label(self.subject_frame7, text="Subject Seven")
                self.subject_label7.grid(row=12, column=1, padx=80, pady=10, sticky="NSEW")
                
                #seventh subject should be RE
                self.subject_seven_box = ttk.Combobox(self.subject_frame7, textvariable=chosen_subjects_seven, state="readonly")
                self.subject_seven_box['values'] = seventh_subject
                self.subject_seven_box.grid(row=13, column=1, columnspan=1, padx=20, pady=20, sticky="NSEW")         
                
                #------RADIOBUTTONS------
                #making radiobuttons for subject five's standards // radiobuttons are like circular checkboxes
                subject_five_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_five_choose_one = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_one)
                subject_five_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_five_choose_two = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_two)
                subject_five_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_five_choose_three = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_three)
                subject_five_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_five_choose_four = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_four)
                subject_five_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_five_choose_five = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_five)
                subject_five_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_five_choose_six = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_six)
                subject_five_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject six's standards // radiobuttons are like circular checkboxes
                subject_six_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)    
                
                subject_six_choose_one = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_one)
                subject_six_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_six_choose_two = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_two)
                subject_six_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_six_choose_three = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_three)
                subject_six_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_six_choose_four = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_four)
                subject_six_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_six_choose_five = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_five)
                subject_six_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_six_choose_six = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_six)
                subject_six_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject seven's standards // radiobuttons are like circular checkboxes
                subject_seven_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_seven_choose_one = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_one)
                subject_seven_choose_one.grid(row=14, column=0, padx=30, pady=10)
                subject_seven_choose_two = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_two)
                subject_seven_choose_two.grid(row=15, column=0, padx=30, pady=10)       
                subject_seven_choose_three = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_three)
                subject_seven_choose_three.grid(row=16, column=0, padx=30, pady=10)                
                subject_seven_choose_four = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_four)
                subject_seven_choose_four.grid(row=17, column=0, padx=30, pady=10)               
              
                #-----------------------------------------------------------------------------------------------
                self.button_frame3 = Frame(self.root, bg='maroon')
                self.button_frame3.grid(row=13, column=0, columnspan=2, padx=48, pady=10)                    
                        
                next_button3 = Button(self.button_frame3, text="NEXT", bg='gainsboro')  
                next_button3.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")             
        
            elif year_level == "Year 12":
        
                #setting up variables for the subject option combobox
                subjects = ["Accounting", "Art History", "Biology", "Chemistry", "Digital Technology", "Drama", "Economics", "English", "French", "Food Technology", "Geography", "History", "Material Technology", "Mathematics", "Music", "Photography", "Physical Education", "Physics", "Te Reo Maori", "Tourism", "Visual Art"] #made a list which contains the Year 12 subjects that can be taken at Carmel
                seventh_subject = ["Religious Education"]
                chosen_subjects_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_five.set("[PLEASE SELECT]")
                chosen_subjects_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_six.set("[PLEASE SELECT]")
                chosen_subjects_seven = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_seven.set(seventh_subject)
                #-----------------------------------------------------------------------------------------------
                self.subject_frame5 = Frame(self.root, bg='darkRed')
                self.subject_frame5.grid(row=10, column=0, padx=48)
                    
                self.subject_label5 = Label(self.subject_frame5, text="Subject Five")
                self.subject_label5.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose fifth subject
                self.subject_five_box = ttk.Combobox(self.subject_frame5, textvariable=chosen_subjects_five, state="readonly")
                self.subject_five_box['values'] = subjects
                self.subject_five_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame6 = Frame(self.root, bg='darkRed')
                self.subject_frame6.grid(row=10, column=1, padx=48)
                
                self.subject_label6 = Label(self.subject_frame6, text="Subject Six")
                self.subject_label6.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")                
                
                #choose sixth subject
                self.subject_six_box = ttk.Combobox(self.subject_frame6, textvariable=chosen_subjects_six, state="readonly")
                self.subject_six_box['values'] = subjects
                self.subject_six_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")                 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame7 = Frame(self.root, bg='darkRed')
                self.subject_frame7.grid(row=11, column=0, columnspan=2, padx=48, pady=20)
                
                self.subject_label7 = Label(self.subject_frame7, text="Subject Seven")
                self.subject_label7.grid(row=12, column=1, padx=80, pady=10, sticky="NSEW")
                
                #seventh subject should be RE
                self.subject_seven_box = ttk.Combobox(self.subject_frame7, textvariable=chosen_subjects_seven, state="readonly")
                self.subject_seven_box['values'] = seventh_subject 
                self.subject_seven_box.grid(row=13, column=1, columnspan=1, padx=20, pady=20, sticky="NSEW")         
                
                #------RADIOBUTTONS------
                #making radiobuttons for subject five's standards // radiobuttons are like circular checkboxes
                subject_five_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_five_choose_one = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_one)
                subject_five_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_five_choose_two = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_two)
                subject_five_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_five_choose_three = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_three)
                subject_five_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_five_choose_four = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_four)
                subject_five_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_five_choose_five = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_five)
                subject_five_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_five_choose_six = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_six)
                subject_five_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject six's standards // radiobuttons are like circular checkboxes
                subject_six_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)    
                
                subject_six_choose_one = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_one)
                subject_six_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_six_choose_two = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_two)
                subject_six_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_six_choose_three = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_three)
                subject_six_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_six_choose_four = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_four)
                subject_six_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_six_choose_five = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_five)
                subject_six_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_six_choose_six = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_six)
                subject_six_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject seven's standards // radiobuttons are like circular checkboxes
                subject_seven_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_seven_choose_one = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_one)
                subject_seven_choose_one.grid(row=14, column=0, padx=30, pady=10)
                subject_seven_choose_two = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_two)
                subject_seven_choose_two.grid(row=15, column=0, padx=30, pady=10)       
                subject_seven_choose_three = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_three)
                subject_seven_choose_three.grid(row=16, column=0, padx=30, pady=10)                
                subject_seven_choose_four = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_four)
                subject_seven_choose_four.grid(row=17, column=0, padx=30, pady=10)                   
           
                #-----------------------------------------------------------------------------------------------
                self.button_frame3 = Frame(self.root, bg='maroon')
                self.button_frame3.grid(row=13, column=0, columnspan=2, padx=48, pady=10)                  
                        
                next_button3 = Button(self.button_frame3, text="NEXT", bg='gainsboro')  
                next_button3.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")          
                
            elif year_level == "Year 13":
                    
                subjects = ["Accounting", "Art History", "Biology", "Calculus", "Chemistry", "Classical Studies", "Design", "Digital Technology", "Drama", "Economics", "English (Core)", "English (Visual)", "Food Technology", "French", "Geography", "History", "Hospitality", "Material Technology", "Music", "Photography", "Physical Education", "Physics", "Statistics", "Te Reo", "Tourism", "Visual Art (Painting)", "STUDY"] #made a list which contains the Year 13 subjects that can be taken at Carmel
                seventh_subject = ["Religious Education"]
                chosen_subjects_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_five.set("[PLEASE SELECT]")
                chosen_subjects_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_six.set("[PLEASE SELECT]")
                chosen_subjects_seven = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_seven.set(seventh_subject)
                #-----------------------------------------------------------------------------------------------
                self.subject_frame5 = Frame(self.root, bg='darkRed')
                self.subject_frame5.grid(row=10, column=0, padx=48)
                    
                self.subject_label5 = Label(self.subject_frame5, text="Subject Five")
                self.subject_label5.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
            
                #choose fifth subject
                self.subject_five_box = ttk.Combobox(self.subject_frame5, textvariable=chosen_subjects_five, state="readonly")
                self.subject_five_box['values'] = subjects
                self.subject_five_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame6 = Frame(self.root, bg='darkRed')
                self.subject_frame6.grid(row=10, column=1, padx=48)
                
                self.subject_label6 = Label(self.subject_frame6, text="Subject Six")
                self.subject_label6.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")                
                
                #choose sixth subject
                self.subject_six_box = ttk.Combobox(self.subject_frame6, textvariable=chosen_subjects_six, state="readonly")
                self.subject_six_box['values'] = subjects
                self.subject_six_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")                 
                #-----------------------------------------------------------------------------------------------
                self.subject_frame7 = Frame(self.root, bg='darkRed')
                self.subject_frame7.grid(row=11, column=0, columnspan=2, padx=48, pady=20)
                
                self.subject_label7 = Label(self.subject_frame7, text="Subject Seven")
                self.subject_label7.grid(row=12, column=1, padx=80, pady=10, sticky="NSEW")
                
                #seventh subject should be RE
                self.subject_seven_box = ttk.Combobox(self.subject_frame7, textvariable=chosen_subjects_seven, state="readonly")
                self.subject_seven_box['values'] = seventh_subject
                self.subject_seven_box.grid(row=13, column=1, columnspan=1, padx=20, pady=20, sticky="NSEW")         
                
                #------RADIOBUTTONS------
                #making radiobuttons for subject five's standards // radiobuttons are like circular checkboxes
                subject_five_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_five_choose_one = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_one)
                subject_five_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_five_choose_two = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_two)
                subject_five_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_five_choose_three = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_three)
                subject_five_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_five_choose_four = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_four)
                subject_five_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_five_choose_five = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_five)
                subject_five_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_five_choose_six = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_six)
                subject_five_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject six's standards // radiobuttons are like circular checkboxes
                subject_six_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)    
                
                subject_six_choose_one = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_one)
                subject_six_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_six_choose_two = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_two)
                subject_six_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_six_choose_three = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_three)
                subject_six_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_six_choose_four = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_four)
                subject_six_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_six_choose_five = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_five)
                subject_six_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_six_choose_six = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_six)
                subject_six_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
               #making radiobuttons for subject seven's standards // radiobuttons are like circular checkboxes
                subject_seven_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_seven_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_seven_choose_one = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_one)
                subject_seven_choose_one.grid(row=14, column=0, padx=30, pady=10)
                subject_seven_choose_two = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_two)
                subject_seven_choose_two.grid(row=15, column=0, padx=30, pady=10)       
                subject_seven_choose_three = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_three)
                subject_seven_choose_three.grid(row=16, column=0, padx=30, pady=10)                
                subject_seven_choose_four = ttk.Radiobutton(self.subject_frame7, variable=subject_seven_standard_four)
                subject_seven_choose_four.grid(row=17, column=0, padx=30, pady=10)                  

                #-----------------------------------------------------------------------------------------------
                self.button_frame3 = Frame(self.root, bg='maroon')
                self.button_frame3.grid(row=13, column=0, columnspan=2, padx=48, pady=10)                    
                        
                next_button3 = Button(self.button_frame3, text="NEXT", bg='gainsboro')  
                next_button3.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")
                
            else:
                pass
        elif school == "Kristin School":
            
            self.root.configure(background='paleTurquoise')  
            
            #creating the first frame for the heading
            self.frame3 = Frame(root, bg='paleTurquoise')
            self.frame3.grid(row=0, column=0, columnspan=2, padx=285, pady=40, sticky="NSEW")
                       
            self.greeting_label3 = Label(self.frame3, text="CHOOSE YOUR SUBJECTS AND STANDARDS", bg='paleTurquoise')
            self.greeting_label3.grid(row=1, column=1, padx=50, pady=20)      
            
            if year_level == "Year 11":
                
                #setting up variables for the subject option combobox
                subjects = ["Art", "Business Studies (Accounting)", "Chinese", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "French", "Further Science (extension)", "Geography", "Graphics", "Hard Tech (Woodwork)", "History", "Japanese", "Mathematics", "Media Studies", "Music", "Physical Education/Health (Core)", "Physical Education (Optional)", "Science", "Spanish", "Soft Technology (Materials)"] #made a list which contains the Year 11 subjects that can be taken at Kristin
                chosen_subjects_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_five.set("[PLEASE SELECT]")
                chosen_subjects_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_six.set("[PLEASE SELECT]")
                #----------------------------------------------------------------------------------------       -------
                self.subject_frame5 = Frame(self.root, bg='teal')
                self.subject_frame5.grid(row=10, column=0, padx=48, pady=20)
                
                self.subject_label5 = Label(self.subject_frame5, text="Subject Five")
                self.subject_label5.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                        
                #choose fifth subject
                self.subject_five_box = ttk.Combobox(self.subject_frame5, textvariable=chosen_subjects_five, state="readonly")
                self.subject_five_box['values'] = subjects
                self.subject_five_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #----------------------------------------------------------------------------------------       -------
                self.subject_frame6 = Frame(self.root, bg='teal')
                self.subject_frame6.grid(row=10, column=1, padx=48, pady=20)
                    
                self.subject_label6 = Label(self.subject_frame6, text="Subject Six")
                self.subject_label6.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                        
                #choose sixth subject
                self.subject_six_box = ttk.Combobox(self.subject_frame6, textvariable=chosen_subjects_six, state="readonly")
                self.subject_six_box['values'] = subjects
                self.subject_six_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")   
                
                #------RADIOBUTTONS------
                #making radiobuttons for subject five's standards // radiobuttons are like circular checkboxes
                subject_five_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_five_choose_one = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_one)
                subject_five_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_five_choose_two = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_two)
                subject_five_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_five_choose_three = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_three)
                subject_five_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_five_choose_four = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_four)
                subject_five_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_five_choose_five = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_five)
                subject_five_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_five_choose_six = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_six)
                subject_five_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject six's standards // radiobuttons are like circular checkboxes
                subject_six_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)    
                
                subject_six_choose_one = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_one)
                subject_six_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_six_choose_two = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_two)
                subject_six_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_six_choose_three = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_three)
                subject_six_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_six_choose_four = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_four)
                subject_six_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_six_choose_five = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_five)
                subject_six_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_six_choose_six = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_six)
                subject_six_choose_six.grid(row=18, column=0, padx=30, pady=10)   
                        
                #-----------------------------------------------------------------------------------------------
                self.button_frame3 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame3.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
        
                next_button3 = Button(self.button_frame3, text="NEXT", bg='gainsboro')  
                next_button3.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")
                
            elif year_level == "Year 12":
               
                #setting up variables for the subject option combobox
                subjects = ["Art", "Biology", "Business Studies (Accounting)", "Chemistry", "Chinese", "Classical Studies", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "Food Tech", "French", "Geography", "Graphics", "Hard Tech (Woodwork)", "History", "Japanese", "Mathematics", "Mathematics Applied", "Media Studies", "Music", "Outdoor Education", "Photography", "Physical Education/Health (Core)", "Physical Education (Optional)", "Physics", "Spanish", "Soft Technology (Materials)"] #made a list which contains the Year 12 subjects that can be taken at Kristin
                chosen_subjects_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_five.set("[PLEASE SELECT]")
                chosen_subjects_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_six.set("[PLEASE SELECT]")
                #----------------------------------------------------------------------------------------       -------
                self.subject_frame5 = Frame(self.root, bg='teal')
                self.subject_frame5.grid(row=10, column=0, padx=48, pady=20)
                
                self.subject_label5 = Label(self.subject_frame5, text="Subject Five")
                self.subject_label5.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                        
                #choose fifth subject
                self.subject_five_box = ttk.Combobox(self.subject_frame5, textvariable=chosen_subjects_five, state="readonly")
                self.subject_five_box['values'] = subjects
                self.subject_five_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #----------------------------------------------------------------------------------------       -------
                self.subject_frame6 = Frame(self.root, bg='teal')
                self.subject_frame6.grid(row=10, column=1, padx=48, pady=20)
                    
                self.subject_label6 = Label(self.subject_frame6, text="Subject Six")
                self.subject_label6.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                        
                #choose sixth subject
                self.subject_six_box = ttk.Combobox(self.subject_frame6, textvariable=chosen_subjects_six, state="readonly")
                self.subject_six_box['values'] = subjects
                self.subject_six_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                
                #------RADIOBUTTONS------
                #making radiobuttons for subject five's standards // radiobuttons are like circular checkboxes
                subject_five_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_five_choose_one = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_one)
                subject_five_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_five_choose_two = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_two)
                subject_five_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_five_choose_three = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_three)
                subject_five_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_five_choose_four = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_four)
                subject_five_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_five_choose_five = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_five)
                subject_five_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_five_choose_six = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_six)
                subject_five_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject six's standards // radiobuttons are like circular checkboxes
                subject_six_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)    
                
                subject_six_choose_one = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_one)
                subject_six_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_six_choose_two = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_two)
                subject_six_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_six_choose_three = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_three)
                subject_six_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_six_choose_four = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_four)
                subject_six_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_six_choose_five = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_five)
                subject_six_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_six_choose_six = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_six)
                subject_six_choose_six.grid(row=18, column=0, padx=30, pady=10)                 
                        
                #-----------------------------------------------------------------------------------------------
                self.button_frame3 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame3.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
        
                next_button3 = Button(self.button_frame3, text="NEXT", bg='gainsboro')  
                next_button3.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")      
                
            elif year_level == "Year 13":
                #setting up variables for the subject option combobox
                subjects = ["Biology", "Business Studies (Accounting)", "Calculus", "Chemistry", "Chinese", "Classical Studies", "Dance", "Digital Technology", "Drama", "EAP", "Economics", "English", "French", "Geography", "Graphics", "Hard Tech (Woodwork)", "Health (Optional)", "History", "Japanese", "Media Studies", "Music", "Outdoor Education", "Painting", "Photography", "Physical Education (Optional)", "Physics", "Statistics", "Soft Technology (Materials)"] #made a list which contains the Year 13 subjects that can be taken at Kristin    
                chosen_subjects_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_five.set("[PLEASE SELECT]")
                chosen_subjects_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                chosen_subjects_six.set("[PLEASE SELECT]")
                #----------------------------------------------------------------------------------------       -------
                self.subject_frame5 = Frame(self.root, bg='teal')
                self.subject_frame5.grid(row=10, column=0, padx=48, pady=20)
                
                self.subject_label5 = Label(self.subject_frame5, text="Subject Five")
                self.subject_label5.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                        
                #choose fifth subject
                self.subject_five_box = ttk.Combobox(self.subject_frame5, textvariable=chosen_subjects_five, state="readonly")
                self.subject_five_box['values'] = subjects
                self.subject_five_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW") 
                #----------------------------------------------------------------------------------------       -------
                self.subject_frame6 = Frame(self.root, bg='teal')
                self.subject_frame6.grid(row=10, column=1, padx=48, pady=20)
                    
                self.subject_label6 = Label(self.subject_frame6, text="Subject Six")
                self.subject_label6.grid(row=11, column=1, padx=80, pady=10, sticky="NSEW")
                        
                #choose sixth subject
                self.subject_six_box = ttk.Combobox(self.subject_frame6, textvariable=chosen_subjects_six, state="readonly")
                self.subject_six_box['values'] = subjects
                self.subject_six_box.grid(row=12, column=1, padx=20, pady=10, sticky="NSEW")     
                
                #------RADIOBUTTONS------
                #making radiobuttons for subject five's standards // radiobuttons are like circular checkboxes
                subject_five_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_five_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                
                subject_five_choose_one = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_one)
                subject_five_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_five_choose_two = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_two)
                subject_five_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_five_choose_three = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_three)
                subject_five_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_five_choose_four = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_four)
                subject_five_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_five_choose_five = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_five)
                subject_five_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_five_choose_six = ttk.Radiobutton(self.subject_frame5, variable=subject_five_standard_six)
                subject_five_choose_six.grid(row=18, column=0, padx=30, pady=10)                
                
                #making radiobuttons for subject six's standards // radiobuttons are like circular checkboxes
                subject_six_standard_one = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_two = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_three = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_four = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_five = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)
                subject_six_standard_six = StringVar() #this means that a variable is made to store data such as names, phrases, words, etc. (no numbers)    
                
                subject_six_choose_one = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_one)
                subject_six_choose_one.grid(row=13, column=0, padx=30, pady=10)
                subject_six_choose_two = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_two)
                subject_six_choose_two.grid(row=14, column=0, padx=30, pady=10)       
                subject_six_choose_three = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_three)
                subject_six_choose_three.grid(row=15, column=0, padx=30, pady=10)                
                subject_six_choose_four = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_four)
                subject_six_choose_four.grid(row=16, column=0, padx=30, pady=10)                
                subject_six_choose_five = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_five)
                subject_six_choose_five.grid(row=17, column=0, padx=30, pady=10)  
                subject_six_choose_six = ttk.Radiobutton(self.subject_frame6, variable=subject_six_standard_six)
                subject_six_choose_six.grid(row=18, column=0, padx=30, pady=10)       
                  
                #-----------------------------------------------------------------------------------------------
                self.button_frame3 = Frame(self.root, bg='lightSeaGreen')
                self.button_frame3.grid(row=13, column=0, columnspan=2, padx=48, pady=20)                    
        
                next_button3 = Button(self.button_frame3, text="NEXT", bg='gainsboro')  
                next_button3.grid(row=14, column=1, padx=80, pady=10, sticky="NSEW")                  
                
    def destroy_window_three(self): #gets rid of all the content from the subject five/six (or incl seven for Carmel) page
        self.frame3.destroy()
        self.subject_frame5.destroy() 
        self.subject_frame6.destroy()
        self.subject_frame7.destroy()
        self.button_frame3.destroy()

#run the program
run=Window(root)
root.mainloop()




