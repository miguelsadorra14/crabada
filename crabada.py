import sqlite3
import csv
import requests 


connection = sqlite3.connect('crabada5.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Crabs
                ([crab_id] INT PRIMARY KEY, [class] TEXT, [shell] TEXT, [horn] TEXT, [body] TEXT, [mouth] TEXT, [eyes] TEXT, [pincer] TEXT, [skill] TEXT, [breed_count] INT)''')
# --------------------------------------------------------------------------------------------------

crabID = [] 
data = []   
api_url = 'https://api.crabada.com/public/crabada/info/' 

with open(r"C:\Users\Claire\2022-01-24-crabada-sales.csv", "r") as csvfile: 
    reader_variable = csv.reader(csvfile) 
    id = list(reader_variable) 
    for rows in id: 
        if rows[1] != 'crab_id':    
            p = api_url + rows[1]
            if p not in crabID:
                crabID.append(p)

print('There are a total of ' + str(len(crabID)) + ' items in the table') 
i = 0 
while i < len(crabID): 
    response = requests.get(crabID[i])
    print(i)
    data.append(response.json())
    i = i + 1 
    

j = 0
while j < len(data):
    itemID = data[j]
    itemID = itemID['result']['id']
    classname = data[j]
    classname = classname['result']['class_name']
    shell = data[j]
    shell = shell['result']['shell_name']
    horn = data[j]
    horn = horn['result']['horn_name']
    body = data[j]
    body = body['result']['body_name']
    mouth = data [j]
    mouth = mouth['result']['mouth_name']
    eyes = data[j]
    eyes = eyes['result']['eyes_name']
    pincer = data[j]
    pincer = pincer['result']['pincers_name']
    skill = data[j]
    skill = skill['result']['skills'][0]['name']
    breedcount = data[j]
    breedcount = breedcount['result']['breed_count']
    print(itemID + ' ' + skill)

    cursor.execute('''INSERT INTO Crabs (crab_id, class, shell, horn, body, mouth, eyes, pincer, skill, breed_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (itemID, classname, shell, horn, body, mouth, eyes, pincer, skill, breedcount))
    j = j + 1

print('done') 
print(len(crabID))

connection.commit()
connection.close()
