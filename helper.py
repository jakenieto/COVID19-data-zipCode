
import matplotlib.pyplot as plt

def derivative(x,y,start,end):
    y_prime = []
    prevX = start
    prevY = end
    for i in range(0,len(x)):
        delta_x = x[i] - prevX
        delta_y = y[i] - prevY
        if (delta_x == 0):
            delta_x = 1
        y_prime.append(delta_y/delta_x)
        prevX = x[i]
        prevY = y[i]
    return y_prime


def plotData(Data):
    plt.plot([day for day in range(0,Data["days"])], Data["data"])  
    plt.title(Data["title"])  
    # naming the x axis 
    plt.xlabel(Data["xlabel"]) 
    # naming the y axis 
    plt.ylabel(Data["ylabel"])    


    # function to show the plot 
    plt.show() 