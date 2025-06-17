# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()


import datetime #To be used for certain date coding

BOLD = '\033[1m' # Used for bolding and unbolding and coloring of some print outputs
RESET = '\033[0m'
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Function to get start day of the week for the reports.
def get_date_start_week():
    today = datetime.date.today()
    # Calculate the start of the week (Monday)
    # weekday() returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
    days_since_monday = today.weekday()
    display_date = today - datetime.timedelta(days=days_since_monday)
    
    # Format the date as "Month Day, Year"
    global formatted_date
    formatted_date = display_date.strftime("%B %d, %Y").strip().title()
    
    print(f"{BOLD}For the week of {formatted_date}{RESET}")
    print()
    return formatted_date
    #print(f"{BOLD}{formatted_date}{RESET}")
get_date_start_week()


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.


def report_week(habit_dict, task_dict, file_n):
    #get_date_start_week() #Don't really need this here but have to call the function somewhere
    heading = "Welcome to the weekly report generator. You can create a report of the habits completed or a report of tasks completed or incompleted."
    print(f"{BOLD}{heading}{RESET}")
    print("*" * len(heading))
    #print('Welcome to the weekly report generator. You can create a report of the habits completed\n or a report of tasks completed or incompleted.')
    rep_yn = input('Do you want to create a report for your habits and tasks? Y/N').strip().title()
  
    
    if rep_yn == "Y":
        if not habit_dict:
            print('Sorry! But there are no habits being tracked') #Need to empy habits to check this.
        elif not task_dict:
            print('Sorry! But there are no tasks being tracked') #Need to empy tasks to check this.
        else:
            print("Alright. Let's create a report. For your convenience here is a list of your habits and tasks" + '\n')
            print(f"{BOLD}My Habits so far:{RESET}")
            print(*habit_dict) #Need comma in between habits
            print()
            print(f"{BOLD}My Tasks so far:{RESET}")
            
            for day,tasks in task_dict.items():
                for task_name in tasks.keys():
                    print(f"{task_name}, ", end=' ') 
           
            print("\n")
            print('*' * len(heading))
    
            #Loop though habits to count number of time each habit was completed
            print(f"{BOLD}{GREEN}Habits Completed for the week of {formatted_date}!{RESET}")
            print(' ')
            
            for habit,day in habit_dict.items():
                num_compl = 0
                for day, compl in day.items(): 
                    if compl:
                        num_compl += 1 
                if num_compl > 1:
                    print(f"{habit} was completed {num_compl} days out of 7 this week.") #So print says days(plural)
                elif num_compl == 1:
                    print(f"{habit} was completed {num_compl} day out of 7 this week.") #So it prints day(singular)
            print(' ')

            
            #Loop through tasks dict and list tasks as completed and incompleted
            
            
            task_compl_list = []
            task_notcompl_list = []
            for day, task in task_dict.items():
                for task_name, compl in task.items():
                    formatted_task = f"{task_name} ({day})"
                    if compl:
                        task_compl_list.append(formatted_task)
                    else:
                        task_notcompl_list.append(formatted_task)
                        
            print(f"{BOLD}{GREEN}Completed Tasks for the week of {formatted_date}{RESET}")
            #get_date_start_week()
            if task_compl_list:
                print(", ".join(task_compl_list)) #.join() to print all tasks on a single line
            else:
                print("No tasks completed this week.")
            print("\n"f"{BOLD}{RED}Uncompleted tasks for the week of {formatted_date}{RESET}")
            if task_notcompl_list:
                print(", ".join(task_notcompl_list))
            else:
                print("All tasks completed! (Or no uncompleted tasks found).")
    else:
        print('Reporting has been cancelled!')
        
#week_rep = report_week(tasks_pass_dict,habits_pass_dict,file_list)

# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.

file_list = ['dictionaries_1.txt', 'dictionaries_2.txt', 'dictionaries_3.txt', 'dictionaries_4.txt', 'dictionaries_5.txt', 
            'dictionaries_6.txt', 'dictionaries_7.txt', 'dictionaries_8.txt', 'dictionaries_9.txt', 
            'dictionaries_10.txt'] # List of dictionaries as text files


# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        report_week(data[0], data[1], file_name)
