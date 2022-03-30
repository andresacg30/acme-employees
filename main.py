from itertools import combinations

from datetime import datetime

import sys

# ACME Employees

"""
This program will evaluate the schedule worked by ACME employees and output a table containing the number of times a
pair of employees have coincided in the office.

"""


def get_data():
    """
    Get filename from command line.
    :return: str
    """
    my_file = sys.argv[1]
    return my_file


def organize_data(file: str):
    """
    Safely opens a file and reads it. Cleans the parsed text, and turns it into a dict with employees as keys
    and worked schedule as values.
    :return: dict
    """
    with open(file, 'r') as f:
        f = f.readlines()  # List of employees
    employees_list = [employee.replace("\n", "").replace(" ", "") for employee in f]  # Erase new line and whitespaces
    employees_dict = {employee.split("=")[0]: employee.split("=")[1] for employee
                      in employees_list}  # Dict of pairs of employee: full schedule
    return employees_dict


def make_combinations(lst: list, n: int):
    """
    Takes a list with the employees names and returns any possible combinations of len n.
    :return: list
    """
    c = list(combinations(lst, n))
    return c


def choose_pair(combination: list, employees: dict):
    """
    Takes the pair of employees' combination, cleans the employees' dict with only the values of the
    combination and returns a new dict.
    :return: dict
    """
    combination = set(combination)  # Set for further intersection
    new_employees = list(set(employees.keys()).intersection(combination))
    new_employees_dict = dict()  # Empty dict to store new combination's values

    # Search among the employees' dict those who match with the names in combination, and assign them to a new dict
    for i, j in employees.items():
        for k in new_employees:
            if i == k:
                new_employees_dict[k] = j
    return new_employees_dict


def make_matrix(weekday: str, employees: dict):
    """
    Takes a two digit format weekday name (e.g. MO for Monday) and searches the worked time of that day
    among the employees' dict. Returns a 2D matrix.
    :return: list
    """
    pair_employees = []
    pair_hours = []
    for employee, j in employees.items():  # Employees and schedules
        for k in j.split(","):  # Divide weekdays
            if k[:2] == weekday:  # Choose only values for the selected weekday
                pair_employees.append(employee)
                pair_hours.append(k)
    # Return new matrix with each employee and his worked schedule
    return [pair_employees, pair_hours]


def prepare_time(matrix: list):
    """
    Prepares the schedule values to turn them into time objects. Returns a list with its second value as a dict with
    the format DAY: WORKED TIME RANGE.
    :return: list
    """
    for index, date in enumerate(matrix[1]):
        matrix[1][index] = {date[:2]: date[2:]}  # Separate the weekday from the hours as dict
    return matrix


def find_coincidences(matrix: list, weekday: str):
    """
    Counts each time the employees have been in the office in the same time interval in a weekday. Returns the
    total of times they have coincided that day.
    :return: int
    """
    counter = 0
    for schedule in matrix[1]:  # Turns time range in a datetime.time object
        for day, hour in schedule.items():
            schedule[day] = {"Start time": datetime.strptime(hour.split("-")[0], "%H:%M").time(),
                             "End time": datetime.strptime(hour.split("-")[1], "%H:%M").time()}

    # Store start time and end time of each employee in the pair
    time_first_employee = [matrix[1][0][weekday]["Start time"], matrix[1][0][weekday]["End time"]]
    time_second_employee = [matrix[1][1][weekday]["Start time"], matrix[1][1][weekday]["End time"]]

    # Increment counter if the start time of one of the employees is greater or equal to the other employee's
    # and the end time of one is less or equal to the other.
    if time_first_employee[0] >= time_second_employee[0] and time_first_employee[1] <= time_second_employee[1]:
        counter += 1

    elif time_second_employee[0] >= time_first_employee[0] and time_second_employee[1] <= time_first_employee[1]:
        counter += 1

    return counter


def main():  # Run program
    weekdays = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']  # List of weekdays to iterate over
    file = get_data()
    employees_file = organize_data(file)
    employees_combinations = make_combinations(employees_file.keys(), 2)
    for combination in employees_combinations:  # Iterate over each pair of employees
        pair = choose_pair(combination, employees_file)
        counter = 0  # Counter for total of days the have coincided
        for weekday in weekdays:  # Iterate over each day of the week
            matrix = make_matrix(weekday, pair)
            matrix = prepare_time(matrix)
            if len(matrix[0]) > 1:  # Only takes the days that more than one employee worked
                coincidences = find_coincidences(matrix, weekday)
                counter += coincidences
        combination = "-".join(list(sorted(combination)))
        print(f"{combination}: {counter}")


if __name__ == "__main__":
    main()
