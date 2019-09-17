# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:50:23 2018

@author: Courage Ekoh
"""

Choices = (1, 2, 3, 4, 5, 6)
Choice_assigned = {'First Choice': [], 'Second Choice': [], 'Third Choice': [],
                   'Fourth Choice':[], 'Fifth Choice': [], 'Sixth Choice': []}
Assigned = [] ##List of assigned Corpers

Unassigned = [] ##List of Unassigned Corpers

States =  {'Abia' : [], 'Adamawa' : [], 'AkwaIbom' : [], 'Anambra' : [],
           'Bauchi' : [], 'Bayelsa' : [], 'Benue' : [], 'Borno' : [],
           'CrossRiver' : [], 'Delta' : [], 'Ebonyi' : [] ,'Enugu' : [],
           'Edo': [], 'Ekiti' : [], 'Gombe' : [], 'Imo' : [], 'Jigawa' : [],
           'Kaduna' : [], 'Kano' : [], 'Katsina': [], 'Kebbi' : [],  
           'Kogi' : [], 'Kwara': [], 'Lagos' : [], 'Nasarawa' : [], 
           'Niger' : [], 'Ogun': [], 'Ondo' : [], 'Osun' : [], 'Oyo' : [], 
           'Plateau' : [], 'Rivers' : [], 'Sokoto': [], 'Taraba' : [],
           'Yobe' : [], 'Zamfara': []}
## Declaring the states to be assigned

with open("NYSC_instance.txt", "r") as NYSC:  ##Opening of the file having the entries by Prospective Corp Members
    lines = NYSC.readlines()
    NYSC_Entries =[]
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        NYSC_Entries.append(line)
        
for choice in Choices:
    for state, corp_members in States.items():
        for entry in NYSC_Entries:
            for i in entry:
                if entry.index(i) == choice:
                    if len(corp_members) < 30 and entry[choice] == state and entry[0] not in Assigned:
                        Assigned.append(entry[0])
                        corp_members.append(entry[0])
                
for state, corp_members in States.items():
    print('\n', state, "-- Number of Corps Members: ", len(corp_members), '\n', corp_members)
    
for entry in NYSC_Entries:
    for i in entry:
        if entry[0] not in Assigned:
            Unassigned.append(entry[0])
            Unassigned = list(set(Unassigned))
    

print('\n', "Number of Assigned: ", len(Assigned), '\n', "Number of Unassigned: ",
      len(Unassigned))
