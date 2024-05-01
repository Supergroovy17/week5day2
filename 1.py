# 1. City Infrastructure Management System
# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will 
#incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
#     class Vehicle:
#         def __init__(self, reg_num, type, owner):
#             self.registration_number = reg_num
#             self.type = type
#             self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.
# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding an attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
#     class Event:
#         def __init__(self, name, date):
#             self.name = name
#             self.date = date

class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

    
    def get_info(self):
        print(f'{self.registration_number} {self.type}{self.owner}')
         
           #implement a method update_owner to change the vehicle's owner
    def update_owner (self, new_owner):
        print(f' {self.owner} is selling vehicle too> {new_owner}!')
        self.owner = new_owner
    
Crown_Oldsmobile=Vehicle(registration_number=1,type='sedan ',owner='Jerry_the_race_car_driver ')
Crown_Oldsmobile.get_info()
Crown_Oldsmobile.update_owner('Primus')
print(Crown_Oldsmobile.owner)


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count
    # Creating an event

event = Event("Primus", "2024-05-01")

# Adding participants
event.add_participant()
event.add_participant()
event.add_participant()

# Getting participant count
print("Participant Count:", event.get_participant_count())