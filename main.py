from pyscript import display, document
import numpy as np 
import matplotlib.pyplot as plt




def sample_numpy (e):
    document.getElementById("output").innerHTML = " "


    days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    old_boxes = np.array([4, 2 ,3 , 4, 1 ,2, 4,])
    sample_graph = plt.plot(days, old_boxes)

    plt.figure()
    plt.plot(days, old_boxes, marker='o', color='blue')
    plt.title("old boxes sold per day")
    plt.xlabel("Day")
    plt.ylabel("old boxes sold")

    display(plt.gcf(), target="output")
