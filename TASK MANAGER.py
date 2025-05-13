
Delete={7:{'TASK TO BE DONE':'HW', 'SUBJECT': 'BIO', 'STATUS': 'DONE','DUE DATE': '12/5/2022'}}
DelTasks={'TASK TO BE DONE':'HW', 'SUBJECT': 'BIO', 'STATUS': 'DONE','DUE DATE': '12/5/2022'}
Math={6:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'MATH', 'STATUS': 'DONE', 'DUE DATE': '13/5/2022'}}
Phy={2:{'TASK TO BE DONE':'STUDY', 'SUBJECT': 'PHY', 'STATUS': 'PENDING','DUE DATE': '09/8/2022'}}
Csc={4:{'TASK TO BE DONE':'HW', 'SUBJECT': 'CSC', 'STATUS': 'DONE','DUE DATE': '06/5/2022'}}
Chem={1:{'TASK TO BE DONE':'HW', 'SUBJECT': 'CHEM', 'STATUS': 'PENDING','DUE DATE': '07/10/2022'},3:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'CHEM', 'STATUS': 'PENDING','DUE DATE': '24/8/2022'}} 
Eng={5:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'ENG', 'STATUS': 'DONE','DUE DATE': '19/3/2022'}}
done={4:{'TASK TO BE DONE':'HW', 'SUBJECT': 'CSC', 'STATUS': 'DONE','DUE DATE': '06/5/2022'},5:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'ENG', 'STATUS': 'DONE','DUE DATE': '19/3/2022'},6:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'MATH', 'STATUS': 'DONE', 'DUE DATE': '13/5/2022'}}
Pending={1:{'TASK TO BE DONE':'HW', 'SUBJECT': 'CHEM', 'STATUS': 'PENDING','DUE DATE': '07/10/2022'},2:{'TASK TO BE DONE':'STUDY', 'SUBJECT': 'PHY', 'STATUS': 'PENDING','DUE DATE': '09/8/2022'},3:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'CHEM', 'STATUS': 'PENDING','DUE DATE': '24/8/2022'}}
taskno={1:{'TASK TO BE DONE':'HW', 'SUBJECT': 'CHEM', 'STATUS': 'PENDING','DUE DATE': '07/10/2022'},2:{'TASK TO BE DONE':'STUDY', 'SUBJECT': 'PHY', 'STATUS': 'PENDING','DUE DATE': '09/8/2022'},3:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'CHEM', 'STATUS': 'PENDING','DUE DATE': '24/8/2022'},4:{'TASK TO BE DONE':'HW', 'SUBJECT': 'CSC', 'STATUS': 'DONE','DUE DATE': '06/5/2022'},5:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'ENG', 'STATUS': 'DONE','DUE DATE': '19/3/2022'},6:{'TASK TO BE DONE':'NOTES', 'SUBJECT': 'MATH', 'STATUS': 'DONE','DUE DATE': '13/5/2022'}}
#CREATION OF DICTIONARY
'''num=int(input("Enter the number of tasks you want to add:"))
for i in range(num):
    task_code=int(input("Enter the task number : "))
    task_do= input("Enter the task you have to do "+str(task_code)+":")
    task_subject=input("Enter the subject in which you have to do the task "+str(task_code)+":")
    task_status= input("Enter the status of your task "+str(task_code)+":")
    task_date=input("Enter the due date of your task in the form(DD/MM/YY)" + str(task_code)+ ":")
    tasks={'TASK TO BE DONE':task_do, 'SUBJECT':task_subject, 'STATUS':task_status, 'DUE DATE':task_date}
    taskno[task_code]=tasks
    print(" ")'''
#choice="Y"
#while choice=="Y" or choice=="y":
print()
print()
print()
print('-'*133)
print()
from datetime import date
import pyfiglet
today = date.today()
# Textual month, day and year	
d4 = today.strftime("%b-%d-%Y")
print('\t\t\t\t\t\t',d4)
print()
print('+'*133)
print()
import pyfiglet
print(pyfiglet.figlet_format("WELCOME TO EXCELLAR",justify="center",width=133))
print()
print('+'*133)
import sys
import time
#DEFINE DELAY PRINT.
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
print()
print("Bringing the best task manager at your one-stop")
print()
print('+'*133)

print()
delay_print("\t\t\t\t HELLO!! I'm excellar bot.\n\t\tLet me walk you through what you will be able to do here!!\t\n")
print()
import webbrowser   
# url13='https://drive.google.com/file/d/1f7pwtjtI_3HphlpAMXZ1XGCKZwg9Jh27/view?usp=share_link'   
# webbrowser.open_new_tab(url13)
print('-'*133)
delay_print("\t\t\t\t\t1.ADD TASKS TO YOUR LIST\t")
print()
print('-'*133)
delay_print("\t\t\t\t\t2.SEARCH TASKS BY THEIR STATUS\t")
print()
print('-'*133)
delay_print("\t\t\t\t\t3.SEARCH TASKS BY SUBJECT\t")
print()
print('-'*133)
delay_print("\t\t\t\t\t4.DELETE TASKS \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t5.UPDATE TASKS \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t6.TIMER \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t7.CALCULATOR \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t8.DICTIONARY \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t9.NOTEPAD \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t10.RESOURCES[SOLUTIONS/SAMPLE PAPERS] \t")
print()
print('-'*133)
delay_print("\t\t\t\t\t11.VISIT OUR WEBSITE FOR MORE.... \t")
print()
print('-'*133)


choice="Y"
while choice=="Y" or choice=="y":
    print("1.ADD TASKS TO YOUR LIST")
    print("2.SEARCH TASKS BY THEIR STATUS")
    print("3.SEARCH TASKS BY SUBJECT")
    print("4.DELETE TASKS")
    print("5.UPDATE TASKS")
    print("6.TIMER")
    print("7.CALCULATOR")
    print("8.DICTIONARY")
    print("9.NOTEPAD")
    print("10.RESOURCES[SOLUTIONS/SAMPLE PAPERS]")
    print("11.VISIT OUR WEBSITE FOR MORE..")
    print()
    print()
    print()
    print()
    opt=int(input("Enter what you want to do: "))
    if opt==1:
        choice2="Y"
        while choice2=="Y" or choice2=="y":
            num=int(input("Enter the number of tasks you want to add:"))
            for i in range(num):
                task_code=int(input("Enter the task number : "))
                task_do= input("Enter the task you have to do "+str(task_code)+":")
                task_subject=input("Enter the subject in which you have to do the task "+str(task_code)+":")
                task_status= input("Enter the status of your task "+str(task_code)+":")
                task_date=input("Enter the due date of your task in the form(DD/MM/YY)" + str(task_code)+ ":")
                tasks={'TASK TO BE DONE':task_do, 'SUBJECT':task_subject, 'STATUS':task_status, 'DUE DATE':task_date}
                taskno[task_code]=tasks
                print(" ")
            
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in taskno:
                print(key,end="\t\t\t")
                value=taskno[key]
                for keys in value:
                    taskm=value[keys]
                    print(taskm,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
            choice2=input("Do you want to add more tasks[Y/N]:" )
    if opt==2:
        tstatus=input("Enter the status you want to search for[Pending/Done]): ")
        #for task_code,tasks in taskno.items():
        if tstatus=="PENDING":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in Pending:
                print(key,end="\t\t\t")
                value=Pending[key]
                for keys in value:
                    Pen=value[keys]
                    print(Pen,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        elif tstatus=="DONE":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in done:
                print(key,end="\t\t\t")
                value=done[key]
                for keys in value:
                    Com=value[keys]
                    print(Com,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        else:
            print("The Status you have serached for is not found. Please check again while entering.",tstatus,"is not in the format[COMPLETED/PENDING]")
    if opt==3:
        tsubject=input("Enter the subject tasks you want to search for: ")
        #for task_code,tasks in taskno.items():
        if tsubject=="MATH":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in Math:
                print(key,end="\t\t\t")
                value=Math[key]
                for keys in value:
                    M=value[keys]
                    print(M,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        elif tsubject=="CSC":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in Csc:
                print(key,end="\t\t\t")
                value=Csc[key]
                for keys in value:
                    C=value[keys]
                    print(C,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        elif tsubject=="PHY":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in Phy:
                print(key,end="\t\t\t")
                value=Phy[key]
                for keys in value:
                    P=value[keys]
                    print(P,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        elif tsubject=="CHEM":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in Chem:
                print(key,end="\t\t\t")
                value=Chem[key]
                for keys in value:
                    Chems=value[keys]
                    print(Chems,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        elif tsubject=="ENG":
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in Eng:
                print(key,end="\t\t\t")
                value=Eng[key]
                for keys in value:
                    E=value[keys]
                    print(E,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
        else:
            print("The Subject you have serached for is not found. Please check again while entering.",tsubject,"is not in the format[MATH/ENG/CHEM/PHY/CSC]")
                
    if opt==4:
        ttask_code=int(input("Enter the task to be deleted:"))
        if ttask_code in taskno:
            del taskno[ttask_code]
            print(" ")
            print(" "*4)                       
            print("-"*110)
            print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
            print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
            print(" ")
            for key in taskno:
                print(key,end="\t\t\t")
                value=taskno[key]
                for keys in value:
                    taskm=value[keys]
                    print(taskm,end='\t\t\t')
                print("\t\t\t")
            print("-"*110)
            print(" ")
            print(" ")
            
        else:
            print("Task not found")
    if opt==5:
        upd_ans='Y'
        t3task_code=int(input("Enter the task no. of the task you want to update"))
        if t3task_code in taskno:
            t1task_do= input("Enter the task you have to update "+str(t3task_code)+":")
            t1task_subject=input("Enter the subject in which you want to update the task "+str(t3task_code)+":")
            t1task_status= input("Enter the status you want to update "+str(t3task_code)+":")
            t1task_date=input("Enter the due date of your task in the form(DD/MM/YY)" + str(t3task_code)+ ":")
            tasks={'TASK TO BE DONE':t1task_do, 'SUBJECT':t1task_subject, 'STATUS':t1task_status, 'DUE DATE': t1task_date}
            upd_ans=input("Are you sure you want to update this item?[Y/N]:")
            if upd_ans=='Y' or upd_ans=='y':
                taskno[t3task_code]=tasks
                print("record updated")
                print(" ")
                print(" "*4)                       
                print("-"*110)
                print("Task\t\t\tTask\t\t\tSubject\t\t\tYour  \t\t\tDue")
                print("No.\t\t\tGiven\t\t\tTask\t\t\tStatus\t\t\tDate")
                print(" ")
                for key in taskno:
                    print(key,end="\t\t\t")
                    value=taskno[key]
                    for keys in value:
                        taskm=value[keys]
                        print(taskm,end='\t\t\t')
                    print("\t\t\t")
                print("-"*110)
                print(" ")
                print(" ")
            
            else:
                print("Error!! Record cannot be updated")
        else:
            print("Error!! Record does not exsist to update")
    
    
    
    elif opt==6:#timer
#DataFlair Guide for python Countdown Timer
#Import necessary modules
        
        from plyer import notification
        from tkinter import messagebox
        from tkinter import *
        import time

#Assign class and set dimensions of the interface
        window = Tk()
        window.geometry("300x200")
        window.title("DataFlair - python Countdown timer and notification")

#Remove the placeholders for every entry field based on click   
        def h_click(event):
            hour_entry.delete(0, 'end')        
        def m_click(event):
            min_entry.delete(0, 'end')
        def s_click(event):
            sec_entry.delete(0, 'end')
 
#Function to activate python countdown timer and show notifications once timer is up
        def timer():
   #Since we use placeholders(represent values that the reader must replace when they use the sample input), we check if the user entered an integer
   #try->lets you test a block of code for errors
            try:
                timer_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())
   #except-> used to catch and handle the exception(s) that are encountered in the try clause.
            except:
                messagebox.showerror(message="Enter Valid Time")
   #The user cannot activate a timer with no time set
   #To update the timer with every decreasing second and display a notification   
            if timer_time >0:
                hour = 0
                min = 0
                sec = 0   
       #If minutes is more than 60, it has to be set to the next hour
                while timer_time >= 0:
                    min, sec = divmod(timer_time,60)
                    if min > 60:
                        hour, min = divmod(min,60)
           #Set the declared variables with the new values to display               
                    hours.set(hour)
                    mins.set(min)
                    secs.set(sec)
           #Sleep for 1 creates a delay of 1 second
                    time.sleep(1)  
           #Update the changes on the window for every second
                    window.update()
           #Decrement the timer value by 1
                    timer_time -= 1
       #Create a desktop notification
                notification.notify(
           #Title of the notification,
                   title = "TIMER ALERT",
           #Body of the notification
                #   message = "Hey amigo!\nDid you do what you wanted to achieve? \nIf not, try again with a new timer",
        #app_icon=r"C:\\Users\\subas\\Desktop\\ADIS Manojna 11A\\COMPUTER SCIENCE\\LOGO.png",
           #Notification stays for 30 seconds
                   timeout  = 30,
               )
       #This notification is provided by tkinter with the created app
                messagebox.showinfo(message="TIME FOR YOUR BREAK!!")
#Label for displaying the title of the app
#position of the label or widget is set using pack().
#pack defaults to centered alignment on a x row and y column coordinate
        title_label_1=Label(window,text="STUDY TIMER", font=("Gayathri", 12)).pack()
        title_label_2 = Label(window, text="Put 0 in fields not of use", font=("Gayathri", 10),fg='white').pack()


#Variables using which the timer is updated in the function
#A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it as well using getter and setter methods.
        hours = IntVar()
        mins = IntVar()
        secs = IntVar() 
#To read user input for hours, minutes and seconds
        hour_entry=Entry(window,width=3,textvariable=hours,font=("Ubuntu Mono",18))
        min_entry=Entry(window,width=3,textvariable=mins,font=("Ubuntu Mono",18))
        sec_entry=Entry(window,width=3,textvariable=secs,font=("Ubuntu Mono",18))
 
#Placeholder for the entry widgets
        hour_entry.insert(0,00)
        min_entry.insert(0,00)
        sec_entry.insert(0,00)
 
#Positioning the entry widgets.
#place() takes an x(from the left) and y(from the top) coordinate
        hour_entry.place(x=80,y=40)
        min_entry.place(x=130,y=40)
        sec_entry.place(x=180,y=40)
 
#To link the defined placeholder removal functions on mouse click
        hour_entry.bind("<1>", h_click)
        min_entry.bind("<1>", m_click)
        sec_entry.bind("<1>", s_click)

#button to activate the timer function
        button = Button(window,text='START TIMER',bg='black',fg='white', command=timer).pack(pady=40)
#Close the window and exit the app
        window.mainloop()
    
    
    elif opt==7:
        from tkinter import *

        win = Tk() # This is to create a basic window
        win.geometry("400x500")  # this is for the size of the window 
        win.resizable(0, 0)  # this is to prevent from resizing the window
        win.title("Calculator")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number
#Global->variables that are declared outside of a function are known as global variables.

        def btn_click(item):
            global expression
            expression = expression + str(item)
            input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

        def bt_clear():
            global expression 
            expression = "" 
            input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
        def bt_equal():
            global expression
            result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
            input_text.set(result)
            expression = ""
 
        expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
        input_text = StringVar()
 
# Let us creating a frame for the input field
 
        input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
        input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
        input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
        input_field.grid(row=0, column=0)
 
        input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
        btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
        btns_frame.pack()
#Lambda-> an anonymous function (i.e., defined without a name) that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression
 
# first row
 
        clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
        divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
        seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
        eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
        nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
        multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
        four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
        five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
        six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
        minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
        one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    
        two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
        three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
        plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
        zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
  
        point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
        win.mainloop()
    
    
# PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words.
    elif opt==8:
        #import nltk
        #nltk.download('wordnet')
        #nltk.download('omw-1.4')

        import tkinter as tk
        from tkinter import ttk, messagebox
        from nltk.corpus import wordnet

        # Function to get meaning, synonyms, antonyms
        def search_word():
            query = word_entry.get().strip()
            if not query:
                messagebox.showwarning("Input Error", "Please enter a word.")
                return

            synsets = wordnet.synsets(query)

            if not synsets:
                result_text.set("No results found.")
                return

            # Collect definitions
            meanings = []
            synonyms = set()
            antonyms = set()

            for syn in synsets:
                meanings.append(f"{syn.pos().upper()} - {syn.definition()}")
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name())
                    if lemma.antonyms():
                        antonyms.add(lemma.antonyms()[0].name())

            # Build result string
            output = f"Meanings:\n" + "\n".join(meanings[:3])  # First 3 meanings
            output += "\n\nSynonyms:\n" + ", ".join(sorted(synonyms)) if synonyms else "\n\nNo synonyms found."
            output += "\n\nAntonyms:\n" + ", ".join(sorted(antonyms)) if antonyms else "\n\nNo antonyms found."

            result_text.set(output)

        # UI Setup
        root = tk.Tk()
        root.title("English Dictionary")
        root.geometry("800x500")
        root.configure(bg="#f0f0f0")

        # Title
        title = tk.Label(root, text="📘 English Dictionary", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        # Entry Frame
        entry_frame = tk.Frame(root, bg="#f0f0f0")
        entry_frame.pack()

        tk.Label(entry_frame, text="Enter Word:", font=("Helvetica", 14), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
        word_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=30)
        word_entry.pack(side=tk.LEFT, padx=5)

        search_btn = tk.Button(entry_frame, text="Search", font=("Helvetica", 12), command=search_word)
        search_btn.pack(side=tk.LEFT, padx=10)

        # Result Frame
        result_frame = tk.Frame(root, bg="#f0f0f0")
        result_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Scrollable Text Area
        result_text = tk.StringVar()
        result_display = tk.Message(result_frame, textvariable=result_text, font=("Helvetica", 12), bg="white", width=700)
        result_display.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Run App
        root.mainloop()

    
    
    
    elif opt==9:
        import tkinter
        import os
        from tkinter import *
        from tkinter.messagebox import *
        from tkinter.filedialog import *

        class Notepad:
            __root = Tk()
            __thisWidth = 300
            __thisHeight = 300
            __thisTextArea = Text(__root)
            __thisMenuBar = Menu(__root)
            __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
            __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
            __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
            __thisScrollBar = Scrollbar(__thisTextArea)
            __file = None

            def __init__(self,**kwargs):

        
                try:
                    self.__root.wm_iconbitmap("Notepad.ico")
                except:
                    pass


                try:
                    self.__thisWidth = kwargs['width']
                except KeyError:
                    pass

                try:
                    self.__thisHeight = kwargs['height']
                except KeyError:
                    pass

                self.__root.title("Untitled - Notepad")

                screenWidth = self.__root.winfo_screenwidth()
                screenHeight = self.__root.winfo_screenheight()
    
                left = (screenWidth / 2) - (self.__thisWidth / 2)
        
                top = (screenHeight / 2) - (self.__thisHeight /2)
        
        # For top and bottom
                self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                                      self.__thisHeight,
                                                      left, top))

        # To make the textarea auto resizable
                self.__root.grid_rowconfigure(0, weight=1)
                self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
                self.__thisTextArea.grid(sticky = N + E + S + W)
        
        # To open new file
                self.__thisFileMenu.add_command(label="New",
                                                command=self.__newFile)
        
        # To open a already existing file
                self.__thisFileMenu.add_command(label="Open",
                                                command=self.__openFile)
        
        # To save current file
                self.__thisFileMenu.add_command(label="Save",
                                                command=self.__saveFile)

        # To create a line in the dialog    
                self.__thisFileMenu.add_separator()                                     
                self.__thisFileMenu.add_command(label="Exit",
                                                command=self.__quitApplication)
                self.__thisMenuBar.add_cascade(label="File",
                                               menu=self.__thisFileMenu)    
        
                                    
        # To give a feature of cut
                self.__thisEditMenu.add_command(label="Cut",
                                                command=self.__cut)         
    
        # to give a feature of copy
                self.__thisEditMenu.add_command(label="Copy",
                                                command=self.__copy)        
        
        # To give a feature of paste
                self.__thisEditMenu.add_command(label="Paste",
                                                command=self.__paste)       
        
        # To give a feature of editing
                self.__thisMenuBar.add_cascade(label="Edit",
                                               menu=self.__thisEditMenu)    
         
        # To create a feature of description of the notepad
                self.__thisHelpMenu.add_command(label="About Notepad",
                                                command=self.__showAbout)
                self.__thisMenuBar.add_cascade(label="Help",
                                               menu=self.__thisHelpMenu)

                self.__root.config(menu=self.__thisMenuBar)

                self.__thisScrollBar.pack(side=RIGHT,fill=Y)                
        
        # Scrollbar will adjust automatically according to the content  
                self.__thisScrollBar.config(command=self.__thisTextArea.yview)  
                self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
            def __quitApplication(self):
                self.__root.destroy()
        # exit()

            def __showAbout(self):
                showinfo("Notepad","Have questions to ask for later? Need to express your thoughts or vent out? Our notepad was built-in just for things as such and more. Creators--->Manojna and Mufliha")

            def __openFile(self):
        
                self.__file = askopenfilename(defaultextension=".txt",
                                              filetypes=[("All Files","*.*"),
                                                         ("Text Documents","*.txt")])
                                          
                                                     

                if self.__file == "":
            
            # no file to open
                    self.__file = None
                else:
            
            # Try to open the file
            # set the window title
                    self.__root.title(os.path.basename(self.__file) + " - Notepad")
                    self.__thisTextArea.delete(1.0,END)

                    file = open(self.__file,"r")

                    self.__thisTextArea.insert(1.0,file.read())

                    file.close()

        
            def __newFile(self):
                self.__root.title("Untitled - Notepad")
                self.__file = None
                self.__thisTextArea.delete(1.0,END)

            def __saveFile(self):

                if self.__file == None:
            # Save as new file
                    self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                    defaultextension=".txt",
                                                    filetypes=[("All Files","*.*"),
                                                               ("Text Documents","*.txt")])
                                                
                                                
                                                           

                    if self.__file == "":
                        self.__file = None
                    else:
                
                # Try to save the file
                        file = open(self.__file,"w")
                        file.write(self.__thisTextArea.get(1.0,END))
                        file.close()
                
                # Change the window title
                        self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
            
                else:
                    file = open(self.__file,"w")
                    file.write(self.__thisTextArea.get(1.0,END))
                    file.close()
 
            def __cut(self):
                self.__thisTextArea.event_generate("<<Cut>>")

            def __copy(self):
                self.__thisTextArea.event_generate("<<Copy>>")

            def __paste(self):
                self.__thisTextArea.event_generate("<<Paste>>")

            def run(self):

        # Run main application
                self.__root.mainloop()




# Run main application
        notepad = Notepad(width=600,height=400)
        notepad.run()


        
        
        

    elif opt==10:
        class1=input("Enter your class[9/10/11/12]: ")
        if class1=="9":
            import webbrowser   
            url="https://byjus.com/ncert-solutions-class-9/" 
            webbrowser.open_new_tab(url)
                   
        if class1=="10":
            import webbrowser   
            url1="https://byjus.com/ncert-solutions-class-10/" 
            webbrowser.open_new_tab(url1)
            
        if class1=="11":
            sub=input("What do you want[JEE/NEET/NCERT]: ")
            if sub=="JEE":
                import webbrowser   
                url= 'https://byjus.com/jee/'    
                webbrowser.open_new_tab(url)
            elif sub=="NEET":
                import webbrowser   
                url2= 'https://byjus.com/neet/'    
                webbrowser.open_new_tab(url2)
            elif sub=="NCERT":
                import webbrowser   
                url2= 'https://byjus.com/ncert-solutions-class-11/'    
                webbrowser.open_new_tab(url2)
        
        if class1=="12":
            sub=input("What do you want[JEE/NEET/NCERT]: ")
            if sub=="JEE":
                import webbrowser   
                url= 'https://byjus.com/jee/'    
                webbrowser.open_new_tab(url)
            elif sub=="NEET":
                import webbrowser   
                url2= 'https://byjus.com/neet/'    
                webbrowser.open_new_tab(url2)
            elif sub=="NCERT":
                import webbrowser   
                url2= 'https://byjus.com/ncert-solutions-class-12/'    
                webbrowser.open_new_tab(url2)
                
                
    elif opt==11:
        print()
        print()
        print("-"*133)
        delay_print("For more information visit our website.......")
        print()
        print()
        print("-"*133)
        delay_print("1. Press 1 for visiting our website.")
        print()
        print()
        print("-"*133)
        delay_print("2. Press 2 to exit.")
        print()
        print()
        print("-"*133)
        print()
        print()
        press=int(input("Enter your choice: "))
        print()
        print()
        if press==1:
            import webbrowser   
            url3= 'https://mexcellarm.wixsite.com/excellar'    
            webbrowser.open_new_tab(url3)
        elif press==2:
            print()
            print("*"*133)
            print()
            print()
            
    choice=input("Do you want to go back to menu page:")
    print()
    print()
    print()
    print()
    print('+'*133)
    print()
import pyfiglet
print(pyfiglet.figlet_format("THANK YOU",justify="center",width=133))
print()
print('+'*133)
print()
print()
delay_print("Hope you liked using Excellar, don't forget to mention us to your friends.")
print()
print()
print('+'*133)
    

