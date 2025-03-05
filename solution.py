"""
Level One
Understanding:
I need to print a list of the empty tables.
Input: Tables
Output: List of the free tables
C: 
Possible tools:
Function
For loop
Empty List for empty tables
append to add an object to the end of a list #https://www.digitalocean.com/community/tutorials/python-add-to-list

Pseudocode:
empty list
have user enter timeslot
check if timeslot is valid
for loop:
for each table in tables:
check if table is empty/has an o
add the table to the list

print list of tables
  


"""
import restaurantTables as st # from lesson 9 code about us states, to take the data from restaurantTables.py

all_tables = st.restaurant_tables2 # To specifically use a list from restaurantTables, can be changed from restaurant_tables2 to restaurant_tables


def check_open_tables():
   available_tables = []

   time = int(input("Enter a timeslot (Number from 1-6): "))
   
   if time < 1 or time >= len(all_tables): # to make sure the timeslot is valid
     print('Error.')
     return [] # to return a blank string
   # I found this as the solution for how to iterate through the list, since it's specifically for numbers as well
   # https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/

   for i in range(1,
   len(all_tables[time])): # starts from one because 0 is the index:
     if all_tables[time][i] == 'o': # checks if there's an o, or if the table is free
      available_tables.append(all_tables[0][i]) # 0 is for the name from the index row

   print(available_tables)

      
  
#check_open_tables()





"""
Level Two
Input: Number of People
Output: Single table that seats the exact num of people and is unoccupied at the moment.
Possible Tools:
int input for party_size
conversion from string to int int(str)
f string to print a sentence saying what table is available with the variable storing the free table

pseudocode:
ask user for party size
check if this number works in context
ask user for timeslor
check if this number works in context


"""
def find_table_with_size(): 
   party_size = int(input('Enter your party size: ')) # decided to take user input for this function
   
   if party_size < 1 or party_size > 20: # for edge cases where the user inputs a number greater than all of our tables combined or smaller than the least amount of people there could be 
     print('Error.')
     return []
   time = int(input("Enter a timeslot (Number from 1-6): "))   
   if time < 1 or time >= len(all_tables): # to make sure the timeslot is
     print('Error.')
     return []
   

   for i in range(1,
   len(all_tables[time])): # starts from one because 0 is the index:
     table_party = all_tables[0][i][3]
     if all_tables[time][i] == 'o' and int(table_party) >= party_size: # checks if there's an o, or if the table is free, https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/ to convert the table party to int
      table = (all_tables[0][i])
      print(f"{table} is available")
      return table

   print('Error') 
   
   
# find_table_with_size() 

"""
Level 3: 
Return all tables that can fit a certain party size or more. 
Inputs: party size and timeslor
Output: list of tables that would fit the party size or more at the timeslot time

Possible tools: 
int input for party size
int input timeslot
empty list
append like in level 1

pseudocode:
empty list for tables
ask for party size
check if this number works in the context
ask for time
check if this number works in the context
for table in tables:
  check if it's free/has an o
  if yes, append to list

  print list
"""
 
def find_all_tables_with_size():
  party_size = int(input('Enter your party size: ')) # decided to take user input for this function
   
  if party_size < 1 or party_size > 20: # for edge cases where the user inputs a number greater than all of our tables combined or smaller than the least amount of people there could be 
     print('Error.')
     return []
  time = int(input("Enter a timeslot (Number from 1-6): "))   
  if time < 1 or time >= len(all_tables): # to make sure the timeslot is
     print('Error.')
     return []
  free_tables = []
  for i in range(1,
   len(all_tables[time])): # starts from one because 0 is the index:
     table_party = all_tables[0][i][3]
     if all_tables[time][i] == 'o' and int(table_party) >= party_size: # checks if there's an o, or if the table is free
      free_tables.append(all_tables[0][i])
    
  print(free_tables)
    
# find_all_tables_with_size()

"""
I didn't get a chance to get to level 4.
Input: Timeslot and Number of People
Output: List of tables singularly or added together that can seat that amount of people at that time
Possible tools: 
int input for party size and timeslot
empty list to store the combinations and tables
extracting number from string
adding the numbers (number of seats) of one table and another
pseudocode:
empty list
ask user for party number
check if valid
ask user for timeslot
check if valid
for table in tables:
if size >= party number and table is available
append to list
for table in tables:
check for sums between all available tables
if sum >= party number
append to list 

print list
"""