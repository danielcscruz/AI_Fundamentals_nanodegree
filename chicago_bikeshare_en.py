
# coding: utf-8

# ----- IMPORT -----
import csv, time
import matplotlib.pyplot as plt
# ----- /IMPORT -----


# ----- OPEN .CSV FILE -----
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
# ----- /OPEN .CSV FILE -----

# ----- DESIGN -----
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("Ok!")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(" _   _     _            _ _         \n| | | | __| | __ _  ___(_) |_ _   _ \n| | | |/ _` |/ _` |/ __| | __| | | |\n| |_| | (_| | (_| | (__| | |_| |_| |\n \___/ \__,_|\__,_|\___|_|\__|\__, |\n                              |___/")
print("----------------------------------------------------")
print("Machine Learning & AI Foundations Nanodegree Program")
print("Project: Explore Chicago Bikeshare Data")
print("----------------------------------------------------")
print("by Daniel Cruz")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("----------------------------------------------------")
# ----- /DESIGN -----

print("Number of rows:")
print(len(data_list)) 
print("Row 0: ") 
print(data_list[0]) 
print("Row 1: ")
print(data_list[1]) 

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n _ \n/ |\n| |\n| |\n|_|")
# ----- /DESIGN -----

# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
print("----------------------------------------------------")

data_list = data_list[1:] 
for x in range(0,20): 
    print(data_list[x]) 

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n ____  \n|___ \ \n  __) |\n / __/ \n|_____|")
# ------ /DESIGN ------

# TASK 2
# TODO: Print the `gender` of the first 20 rows
print("\nTASK 2: Printing the genders of the first 20 samples")
print("----------------------------------------------------")

for x in range(0,20): 
    print(data_list[x][6]) 

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n _____ \n|___ / \n  |_ \ \n ___) |\n|____/ ")
# ----- /DESIGN -----

def column_to_list(data, index):
    column_list = [] 
    for x in range(0,len(data)): 
        list_item = data[x][index] 
        column_list.append(list_item) 
    return column_list

    #Args:
        # data - matrix containing the lists of data
        # index - index of the column to be converted to list
    #Returns:
        # column_list - new list

print("\nTASK 3: Printing the list of genders of the first 20 samples")
print("----------------------------------------------------")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n _  _   \n| || |  \n| || |_ \n|__   _|\n   |_|")
# ----- /DESIGN -----

male = 0
female = 0

#count male
for m in range(0,len(data_list)):
    if data_list[m][-2] == "Male":
        male = male + 1

#count female
for f in range(0,len(data_list)):
    if data_list[f][-2] == "Female":
        female = female + 1

print("\nTASK 4: Printing how many males and females we found")
print("----------------------------------------------------")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n ____  \n| ___| \n|___ \ \n ___) |\n|____/ ")
# ----- /DESIGN -----

def count_gender(data_list): 
    male = 0 
    female = 0 
    for m in range(0,len(data_list)): 
        if data_list[m][-2] == "Male": 
            male = male + 1
    for f in range(0,len(data_list)): 
        if data_list[f][-2] == "Female": 
            female = female + 1  
    return [male, female]

    #Args:
        # data _list- matrix containing the lists of data
    #Returns:
        # male - sum of 'Male' values within the -2th ( or 6th) column
        # male - sum of 'Female' values within the -2th ( or 6th) column

print("\nTASK 5: Printing result of count_gender")
print("----------------------------------------------------")
print(count_gender(data_list))


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n  __   \n / /_  \n| '_ \ \n| (_) |\n \___/ ")
# ----- /DESIGN -----


def most_popular_gender(data_list): #create a function with data_list as parameter
    if count_gender(data_list)[0] > count_gender(data_list)[1]: # 
        answer = "Male"
    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer

    #Args:
        # data _list- matrix containing the lists of data
    #Returns:
        # answer - string of the most popular gender


print("\nTASK 6: Which one is the most popular gender?")
print("----------------------------------------------------")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------


# Graph - gender
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)


# function to count user types
def count_user_types(data_list):
    customer = 0
    subscriber = 0
    for c in range(0,len(data_list)):
        if data_list[c][-3] == "Customer":
            customer = customer + 1
    for s in range(0,len(data_list)):
        if data_list[s][-3] == "Subscriber":
            subscriber = subscriber + 1
    
    return [customer, subscriber]

        #Args:
        # data _list- matrix containing the lists of data
    #Returns:
        # customer - sum of 'Customer' values within the -3th ( or 5th) column
        # subscriber - sum of 'Subscriber' values within the -3th ( or 5th) column

# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n _____ \n|___  |\n   / / \n  / /  \n /_/")
# ----- /DESIGN -----

print("\nTASK 7: Check the chart (User types)! ")
print("----------------------------------------------------")


# graph - user types
user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantity by User Types')
plt.show(block=True)


# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n  ___  \n ( _ ) \n / _ \ \n| (_) |\n \___/ ")
# ----- /DESIGN -----


male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("----------------------------------------------------")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are customers that didn't inform their genders"
print("Answer:", answer)


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------


# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n  ___  \n / _ \ \n| (_) |\n \__, |\n   /_/ ")
# ----- /DESIGN -----

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# Convert every value from string to integer
trip_duration_list = [int(i) for i in trip_duration_list]

# Sort the list
trip_duration_list.sort()

# Loop to go over every element to count them
total_trip = 0.
qtd_trip = int(len(trip_duration_list))
for x in range(0, qtd_trip -1):
    total_trip = total_trip + int(trip_duration_list[x])

# Mean calculation
mean_trip = total_trip / qtd_trip

# Min trip = first value in the sorted list
min_trip = trip_duration_list[0]

# Max trip = last value in the sorted list
max_trip = trip_duration_list[len(trip_duration_list)-1]

# Median calculation
# List with even numbers
if len(trip_duration_list) % 2 == 0:
    index = int(len(trip_duration_list))
    median_trip = (trip_duration_list[index] + trip_duration_list[index+1]) / 2
# List with odd numbers
else:
    index = int(((len(trip_duration_list))/2)+0.5)
    median_trip = trip_duration_list[index]


print("\nTASK 9: Printing the min, max, mean and median")
print("----------------------------------------------------")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------


# ----- DESIGN -----
print("____________________________________________________")
input("Press Enter to continue...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n _  ___  \n/ |/ _ \ \n| | | | |\n| | |_| |\n|_|\___/ ")
# ----- /DESIGN -----

# check types how many start_stations do we have 
user_types= set(column_to_list(data_list, 3))


print("\nTASK 10: Printing start stations:")
print("----------------------------------------------------")
print(len(user_types), " stations: \n")
print(user_types)


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------


print("____________________________________________________")
input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
     # """
     # Example function with annotations.
     # Args:
     #     param1: The first parameter.
     #     param2: The second parameter.
     # Returns:
     #     List of X values

     # """


input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "no"


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------

