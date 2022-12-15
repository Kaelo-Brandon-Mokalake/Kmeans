import csv
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# a function that computes the distance between two data points
def euclidean_distance():

    # getting user input
    option = input('''Enter the file name you want to use:
            data1953.csv
            data2008.csv
            dataBoth.csv \n\t: ''')
    # read the file
    data_2 = pd.read_csv(option)

    x = data_2.iloc[:, 1:2].values
    y = data_2.iloc[:, 2].values

    # determining the distance
    dis = np.sqrt(sum(pow(x-y, 2) for x, y in zip(x, y)))

    # returning th result
    return dis


# a function that finds the closest centroid to each point out of all the centroids
def mean(option):

    # reading the data
    data_1 = pd.read_csv(option)

    # getting the x and y values
    x = data_1.iloc[:, 1:2].values
    y = data_1.iloc[:, 2].values

    # determining and returning the mean
    return np.mean(x), np.mean(y)


# a function that finds the closest centroid to each point out of all the centroids
def centroid(func):

    # determining the centroid
    min_v = np.min(func)

    # returning the result
    return np.where(func == min_v)[0]


# a function that visualizes data as a scatter plot to the screen
def plot_graph():

    # getting user input
    option = input('''Enter the file name you want to use:
                data1953.csv
                data2008.csv
                dataBoth.csv \n\t: ''')
    # reading the data
    data_3 = pd.read_csv(option)

    # getting x and y values
    x = data_3.iloc[:, 1:2].values
    y = data_3.iloc[:, 2].values

    # scattering data
    plt.scatter(x, y, color="blue", label="X values")
    plt.scatter(y, x, color="red", label="Y values")

    plt.title('(life expectancy, birth rate) measured for each country')
    plt.xlabel('Birth Rate')
    plt.ylabel('Life Expectancy')

    # displaying data to the screen as a scatter plot
    plt.legend()
    plt.show()


# getting user input
choice = input('''Welcome, please input your choice below:
    r - read the csv file
    d - determine the euclidean distance between two points
    c - determine the distance to each of the centroids from each of the points
    m -  the two-dimensional mean
    s - visualize data as scatter plot
    : ''').lower()

if choice == "r":

    # getting user input
    file = input('''Enter the file name you want to use:
    data1953.csv
    data2008.csv
    dataBoth.csv \n\t: ''')
    data = pd.read_csv(file)

    # displaying the data
    print(data)

elif choice == "d":

    # calling a function
    distance = euclidean_distance()

    # displaying data to the screen
    print("The Euclidean distance between two points is: ", distance)

elif choice == "c":

    # initializing a called function to a declared variable
    cent = centroid(euclidean_distance())

    # displaying data to the screen
    print("The centroid is: ", cent)

elif choice == "m":

    # getting user input
    option = input('''Enter the file name you want to use:
                data1953.csv
                data2008.csv
                dataBoth.csv \n\t: ''')

    # displaying data to the screen
    print(f"\nThe mean for X values is: {mean(option)[0]} \nThe mean for Y values is: {mean(option)[1]}")

elif choice == "s":

    # calling a function
    plot_graph()
