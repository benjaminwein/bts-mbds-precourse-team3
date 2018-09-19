import csv
f=open('C:\\Users\\jordi\\Downloads\\train.csv')
Sniffer = csv.Sniffer()
dialect = Sniffer.sniff(f.read(2048))
print(dialect)
f.seek(0)
reader = csv.reader(f,dialect)
Passenger_Id = []
Survived = []
Pclass = []
Name = []
Sex = []
Age = []
Sibsp = []
Parch = []
Ticket = []
Fare = []
Cabin = []
Embarked = []
for row in reader:
    Passenger_Id.append(row[0])
    Survived.append(row[1])
    Pclass.append(row[2])
    Name.append(row[3])
    Sex.append(row[4])
    Age.append(row[5])
    Sibsp.append(row[6])
    Parch.append(row[7])
    Ticket.append(row[8])
    Fare.append(row[9])
    Cabin.append(row[10])
    Embarked.append(row[11])
print(Passenger_Id)
print(Survived)
print(Pclass)
print(Name)
print(Sex)
print(Age)
print(Sibsp)
print(Parch)
print(Ticket)
print(Cabin)
print(Embarked)


import matplotlib
import scipy
import pandas as pd
df = pd.read_csv('C:\\Users\\jordi\\Downloads\\train.csv')

import pandas
df = pandas.read_csv('C:\\Users\\jordi\\Downloads\\train.csv', index_col='Name', parse_dates=['Survived'])
print(df['Survived'])

import matplotlib.pyplot as plt

data = {'Pclass': 1, 'Sex': 'female'}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey = True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.show()



# Age Categories vs death count
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('C:\\Users\\uni\\Downloads\\train.csv')



infants = df[(1 <=df['Age']) & (df['Age'] <= 5)]
children = df[(6 <=df['Age']) & (df['Age'] <= 12)]
youth = df[(13 <=df['Age']) & (df['Age'] <= 24)]
young_adults = df[(25 <=df['Age']) & (df['Age'] <= 39)]
adults = df[(40 <=df['Age']) & (df['Age'] <= 60)]
elderly = df[(61 <=df['Age']) & (df['Age'] <= 100)]

Agegroup_number = [len(infants), len(children), len(youth), len(young_adults), len(adults), len(elderly)]
Agegroup_name = ['infant', 'children', 'youth', 'young_adults', 'adults', 'elderly']
 
plt.show()
Agegroup_number                                                                                            
                                                                                            
                     
