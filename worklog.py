#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('diary_worklog.db')

class Entry(Model):
    employee = CharField(255)
    content = TextField()
    date = CharField(255)   
    timespent = CharField(255) 
    notes = CharField(255)

    timestamp = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        
def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    choice = None
    
    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        
        if choice in menu:
            menu[choice]()
    return choice         

def add_entry():
    """Add an entry."""

    name = input("Enter your full name: ")
    
    task = input("Enter your task: ")

    date_completed = get_date()
    
    time_spent = input("Time spent in HH:MM: ")
    
    notes_taken = input("Enter your notes: ")
    
    if task:
        if input('Save entry? [Y/n] ').lower() != 'n':
            Entry.create(content=task,date=date_completed, timespent=time_spent, notes=notes_taken, employee=name)
            print("Saved successfully!")
    return task
   

def view_employee_entries():
    query = Entry.select(Entry.employee).distinct()
    for idx, x in enumerate(query):
        print("%d) %s" % (int(idx)+1, x.employee))
    view_entries(input('Enter employee name to search by: '))           
    

def view_entries(search_query=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp)
    if search_query:
        entries = Entry.select().where(
        Entry.content.contains(search_query) |
        Entry.employee.contains(search_query) |
        Entry.date.contains(search_query) |
        Entry.notes.contains(search_query) |
        Entry.timespent.contains(search_query)
        )       
        
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print("\n" + timestamp)
        print('='*len(timestamp) + "\n")

        print("Employee Name: {}".format(entry.employee))
        print("Task Completed: {}".format(entry.content))
        print("Date Completed: {}".format(entry.date))
        print("Total Timespent: {}".format(entry.timespent))
        print("Notes Completed: {}".format(entry.notes) + "\n")

        print('='*len(timestamp))
        
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu' + "\n")
        
        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def get_date():	
    # repeat all this logic until its valid	
    not_valid = True
    
    while not_valid:
        intial_date = input("Date Completed — MM/DD/YY format: ")
        try:           
            intial_date = datetime.datetime.strptime(intial_date, '%m/%d/%y')
            date = intial_date.strftime('%m/%d/%y')
            not_valid = False
        except ValueError:
            print("Opps! Wrong date format. Please post in MM/DD/YY format ")
            
    return date  


def search_entries():
    """Search entries for a string."""
    print("Would you like to search by A) Viewing all employees B) Search term? ")
    answer = input("Answer: ").upper()
    if answer == "A":
        view_employee_entries()
    if answer == "B":                                
        view_entries(input('Search query (i.e. employee name, date, or subject): '))
                                  

def delete_entry(entry):
    """Delete an entry."""
    if input("Are you sure? [yN] ").lower() == 'y':
        entry.delete_instance()
        print("Entry deleted!")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])
  
if __name__ == '__main__':
    initialize()
    menu_loop()
