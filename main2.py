from pyscript import document, display
import logging 
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import numpy as np
import matplotlib.pyplot as plt

#hides the Matplotlib error message
plt.figure()
plt.plot([0, 1], [0,1])
plt.close

quarters = []
absences = []

#retrieves values from webpage
def add_absence(event):

    quarter = document.getElementById("Quarters").value
    number = int(document.getElementById("Absent").value)

    quarters.append(quarter)
    absences.append(number)

    document.getElementById("output").innerHTML = (
        f"{quarter}: {number} absences added!"
    )

    generate_graph()


def generate_graph():
    #clears previous graph
    plt.clf()

    #x and y values to be inputed into the graph
    x = np.array(quarters)
    y = np.array(absences)

    #plots the graph
    plt.plot(x, y)

    #labels for the graph
    plt.title("Quarterly Attendance (Absences)")
    plt.xlabel("Quarter")
    plt.ylabel("Absences")

    #displays the graph in the webpage
    display(plt, target="graph", append=False)

    # for skills test