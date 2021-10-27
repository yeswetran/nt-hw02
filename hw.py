import json
import csv
import matplotlib.pyplot as plt
import datetime

# 2015 Polling Places

total_polls = 0
labels = []
sizes = []
hosts = {
    "church" : 0,
    "school" : 0,
    "fire" : 0,
    "club" : 0
}

polls = open('C:/Users/yeswe/Google Drive/FA21/CSCI040/Labs/nt-hw02/polling-places-2015.csv')
reader = csv.reader(polls)
for row in reader:
    total_polls += 1
    for host in hosts:
        if host in str(row).lower():
            hosts[host] += 1

for host in hosts:
    sizes.append(((hosts[host]) / total_polls) * 100)

for host in hosts.keys():
    labels.append(host.capitalize())

fig1, ax1 = plt.subplots()
#ax1.set_title('2015 LA Polling Places, categorized by host', pad=25)

ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

# 2017 Polling Places

polls = open('C:/Users/yeswe/Google Drive/FA21/CSCI040/Labs/nt-hw02/polling-places-2017.csv')

total_polls = 0
labels = []
sizes = []
hosts = {
    "church" : 0,
    "school" : 0,
    "fire" : 0,
    "club" : 0
}

reader = csv.reader(polls)
for row in reader:
    total_polls += 1
    for host in hosts:
        if host in str(row).lower():
            hosts[host] += 1

for host in hosts.keys():
    labels.append(host.capitalize())

counts = hosts.values()

fig2, ax2 = plt.subplots()

#ax2.set_title('2017 LA Polling Places, categorized by host')
ax2.set_xlabel('Polling place host')
ax2.set_ylabel('Number of polling places')

ax2.bar(labels, counts)
plt.show()
