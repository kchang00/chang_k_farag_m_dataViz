import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
medals = []

'''
with open('data/test.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print('pushing text rows to categories array')
            categories.append(row)
            line_count += 1
            # makes sure it counts number of lines processed
            # since array can start on different number?
        else:
            medalsData = row[0]  # changes table "columns"
            # medalsData = medalsData.replace('Gold', '1')
            # medalsData = medalsData.replace('Silver', '2')
            # medalsData = medalsData.replace('Bronze', '3')
            medals.append(medalsData)
            line_count += 1

print('processed', line_count, 'rows of data')
print('first line:', medals[1])  # gets first row inside array
print('last line:', medals[-1])  # gets last row (goes backwards = end)
'''

with open('data/olympics_men_women.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print('pushing text rows to categories array')
            categories.append(row)
            line_count += 1
            # makes sure it counts number of lines processed
            # since array can start on different number?
        else:
            medalsData = row[7]  # changes table "columns", count from 0
            medalsData = medalsData.replace('Gold', '1')
            medalsData = medalsData.replace('Silver', '2')
            medalsData = medalsData.replace('Bronze', '3')
            medalsData = medalsData.replace(',', '')
            medalsData = medalsData.replace('Total', '')
            medalsData = medalsData.replace('Medal', '')
            medalsData = medalsData.replace('386', '')
            medalsData = medalsData.replace('239', '')
            medals.append(medalsData)
            line_count += 1

print('processed', line_count, 'rows of data')
print('first line:', medals[3])  # gets first row inside array
print('last line:', medals[-1])

np_medals = np.array(medals)

total_medals = np_medals == {'Gold': 1, 'Silver': 2, 'Bronze': 3}

total_gold_medals = np_medals == 1
t_g = int(len(np_medals[total_gold_medals]) / len(np_medals) * 100)  # gets percentages
print(t_g)

total_silver_medals = np_medals == 2
t_s = int(len(np_medals[total_gold_medals]) / len(np_medals) * 100)
print(t_s)

total_bronze_medals = 3
t_b = 100 - (t_g + t_s)
print(t_b)

# total medals plots

    # pie chart

labels = 'Gold', 'Silver', 'Bronze'
sizes = [(192 + 123), (128 + 75), (66 + 41)]
colors = ['#FFDF00', '#C0C0C0', '#CD7F32']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode = explode, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')

plt.legend(labels, loc = 1)
plt.title('Percentage of Medals Won')
plt.xlabel('1924 - 2014 Winter Olympics: Canada Medal Results')
plt.show()
    
    # another chart here

# men vs. women

    # pie chart

labels = 'Men', 'Women'
sizes = [(386), (239)]
colors = ['#228B22', '#4b0082']
explode = (0.1, 0.1)

plt.pie(sizes, explode = explode, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.axis('equal')

plt.legend(labels, loc = 1)
plt.title('Percentage of Medals Won Between Men and Women')
plt.xlabel('1924 - 2014 Winter Olympics: Canada Medal Results')
plt.show()

    # bar graph

men = (192, 128, 66)
women = (123, 75, 41)

ind = np.arange(len(men))  # the x locations for the groups
width = 0.35  # width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men, width,
                color='#228B22', label='Men')
rects2 = ax.bar(ind + width/2, women, width,
                color='#4b0082', label='Women')


ax.set_ylabel('# Medals Won')
ax.set_title('Types of Medals Won Between Men and Women')
ax.set_xticks(ind)
ax.set_xticklabels(('Gold', 'Silver', 'Bronze'))
ax.legend()


def autolabel(rects, xpos='center'):
    xpos = xpos.lower()
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()

# medals per sport

    # pie chart

    # another graph here
