# acme-employees
This program will get information of ACME's employees worked schedules and output a table containing how many times a pair of employees have coincided in office. I used Python for this exercise.

# Modules used in this program
  - sys: to get the name of the file cointaining the schedules from the commmand line.
  - itertools - combinations: to get all possible employees' pair combinations.
  - datetime: to make datetime objects from the schedules and be able to compare them.
 
# The exercise

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

- Example 1:

  INPUT
  RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
  ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
  ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

  OUTPUT:
  ASTRID-RENE: 2
  ASTRID-ANDRES: 3
  RENE-ANDRES: 2

- Example 2:

  INPUT:
  RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
  ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

  OUTPUT:
  RENE-ASTRID: 3

# Files in the repository

- main.py: the main program. This program will take a command line argument to output the tables. Scroll down to find the instructions to run it.
- acme_test.py: the unit tests for the main program. I used Python's unittest for it. 
- employees.txt: text file containing the employees info for example #1.
- employees1.txt: text file containing the employees info for example #2.

# How to run the program

This is a command line program. Download the main.py file and save it in the same folder as the employees data files. You can download employees and employees1 for testing, and the file for test itself. Once you have the main.py in the same folder as your data, open a command line in that folder and run:

    - python main.py (NAME OF THE FILE WITH THE DATA.txt)
    
    E.G:
    - python main.py employees.txt

# Program logic

To get the desired result we need to compare the times worked by all the possible combinations of two employees. We compare the worked schedule on each weekday and combination and count how many times some employee was working in the time range of other employee in the whole week. When we have the worked schedule, we can split it in "START TIME" and "END TIME". To know if the time range of an employee falls in the time range of another, we could say that:

  - IF the start time of the employee X is GREATER OR EQUAL than the start time of the employee Y, AND the end time of X employee is LESS OR EQUAL than the end time of the employee Y, then they coincided in the office.

  # Functions in my progam:
    - get_data()
    - organize_data()
    - make_combinations()
    - choose_pair()
    - make_matrix()
    - prepare_time()
    - find_coincidences()
    - main()
    
# My approach

The first thing to do when working with data is clean it. So, the program first gets the name of the file with get_data(), which is the name parsed in the command line argument. Then, it reads the file safely, creates a list without the line splits and without white spaces. Erasing this symbol is just a security approach to any wrong whitespaces that could be in the data (check example #1 - RENE - SUNDAY). Finally, it creates a dict with the name of the employee as key and his schedule as value. E.G: {"ASTRID": "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"), we will reffer this list as employees list from now.

After having the employees dict, we could get each employees name from the keys. That's when make_combinations() takes action. It will take every employees name and make all possible combinations of pair of the employees dict. It returns a list containing the combinations.

Now we want to compare the schedules of every combinations. For this, I created the funcion choose_pair(), which will extract the information of the pair of employees from the employees dict. This action is done by turning the lists with the employees' names (chosen combination and all employees) into a set, and finding their intersection. It returns a new dict only with the information of that pair.

For easier comparison purposes, I decided to turn the information in a 2D Matrix in which we have the employees name as columns and their info as a row. The worked hours info that is needed in this step is for a specific weekday. This action is done with the make_matrix() function, and then the rows' info are turned into a dict WEEKDAY: HOURS with the prepare_time() function.

The last function of the program implements the logic described before. The find_coincidences() function takes each hour and turns it into a datetime.time object. It divides them into "Start time" and "End time" and apply the logic with a boolean operation described in the logic of the program. If the comparisson is True, it increase a counter's value. After doing all the operations it returns how many times the pair of employees coincided in the office that day. This is function does its operation for a weekday and a pair of employees.

Now with all the functions defined, the program runs with the main() function. It holds a list with the weekdays, with the format previously defined by the data, wich is two digits: "MO", "TU", "WE" etc. The program iterates over every pair of employees' combination, makes the matrix for that combination and then iterates over each weekday. Then, the program applies the find_coincidences() function only to those matrix with more than one employee (We only need the weekdays that more than one employee worked). The program returns the pair of employees and the sum of the times they coincided in the office over the week in the following format:

    - EMPLOYEE1-EMPLOYEE2: N
    N is a integer that represents the total time this pair of employees coincided in the office.
