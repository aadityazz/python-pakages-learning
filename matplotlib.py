import matplotlib.pyplot as plt
import numpy as np

# Creating coordinates of x-axis and y-axis
x = [1, 2, 3]
y = [2, 4, 6]

# Creating another x-axis and y-axis
x2 = [3, 4, 5]
y2 = [2, 4, 6]

# function will show points of coordinates on graph
plt.scatter(x, y)
plt.show()

# function will connect the points of coordinates on graph using line
plt.plot(x2, y2)
plt.plot(x, y)
plt.show()

# To show both points and connected lines on graph
plt.scatter(x, y)
plt.plot(x, y)
plt.show()

# Plot function x^3
x = np.array([1, 2, 3, 4, 5])
y = x ** 3
plt.plot(x, y)
plt.show()

'''
Matplotlib gives us a functionality that as a parameter that is 
plot(x, y, params). The params will take first character tto represent
the line color (r, b, p, w etc) and then further character for line 
representation as lines or dots or dashes etc (--, -., -, o, ^, +) 
'''

# Plotting function x^3 more curvy
x = np.arange([0, 5, 0.1])
y = x ** 3
plt.plot(x, y)
plt.show()

# Interesting thing to do is
''''
In this method we have only one array and the matplotlib will take that array as
y-axis and it will create an array for x-axis as [0, 1, 2, -----, upto n-1]
'''
a = [3, 4, 5]
plt.plot(a)
plt.show()

# Customizing Graph-->

# Another way to define line color and its type
plt.plot(x, y, color="red", marker='p')

# Defining the line width
plt.plot(x, y, linewidth=5)

# Labelling specific line on the plot
plt.plot(x, y, label="line")
plt.legend()

# Defining the axis ratios
plt.axis([0, 10, 0, 100])

# Making Grid of the graph
plt.grid()

# Adding some texts on some particular points
plt.text(2, 80, "text", fontsize=12)

# Labelling Title of graph, x-axis, y-axis
plt.ylabel("y")
plt.xlabel("x")
plt.title("Title")

# Bubble Chart -->

year = [2012, 2013, 2014, 2015, 2016, 2017]
salary = [12, 13, 14, 17, 19, 20]
population = [100, 120, 180, 300, 370]

plt.scatter(year, salary, s=population, c='r', alpha=0.5)  # Alpha is opacity on bubble
plt.show()

# To make bubble of different color we use this Approach
c = np.arange(len(year))
plt.scatter(year, salary, s=population, c=c, alpha=0.5, edgecolors='black', marker='^')
plt.show()

# To show some text on point on graph
plt.text(year[0] + 0.1, salary[0] + 0.1, population[0])
plt.show()

# pie graphs
labels = ["A", "B", "C", "D"]
sizes = [3, 4, 6, 2]
colors = ["blue", "purple", "red", "pink"]
explode = [0.1, 0.2, 0, 0]
plt.title("Split among classes")
plt.pie(sizes, colors=colors, explode=explode, labels=labels, autopct="%.2f%%", startangle=100)
plt.axis("equal")
plt.show()

#Histrogram -->
a = [1,2,3,4,1,3,4,2,1,1,]
plt.hist(a, edgecolor = 'black')
plt.xticks(np.arange(23))
plt.show()


#BarGraphs -->
year = [2012, 2013, 2014, 2015, 2016, 2017]
salary = [12, 13, 14, 17, 19, 20]
population = [100, 120, 180, 300, 370]

plt.bar(year, population, width=1)
plt.xticks(rotation=45)
plt.show()