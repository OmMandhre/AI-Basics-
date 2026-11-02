#simple reflex agent vaccume cleaner 

environment = {'A': 'Dirty', 'B': 'Dirty'}

location = 'A'

action_table={
    ('A', 'Dirty'): 'Cleaning..',
    ('A', 'Clean'): 'Move to B',
    ('B', 'Dirty'): 'Cleaning..',
    ('B', 'Clean'): 'Move to A'
}

while True:
    print("Location: ", location)
    print("Environment: ", environment)
    
    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("Action: Stop!, both rooms are clean")
        break
    
    percept=(location, environment[location])
    action = action_table[percept]
    
    print("Selected action: ", action)
    
    if action=='Cleaning..':
        environment[location]='Clean'
    elif action=='Move to B':
        location='B'
    elif action=='Move to A':
        location='A'
        
    print("-"*40)