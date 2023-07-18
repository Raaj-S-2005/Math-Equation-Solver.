import numpy as np
import matplotlib.pyplot as plt

def graph_trig_function():
    function = input("Enter the trigonometric function (sin, cos, tan): ")
    angle_type = input("Enter the angle type (radians or degrees): ")

    # Define the range of x values (angles)
    if angle_type.lower() == "degrees":
        x = np.linspace(0, 360, 100)
        x_rad = np.radians(x)
    else:
        x = np.linspace(0, 2 * np.pi, 100)
        x_rad = x

    # Evaluate the trigonometric function for each x value
    if function.lower() == "sin":
        y = np.sin(x_rad)
    elif function.lower() == "cos":
        y = np.cos(x_rad)
    elif function.lower() == "tan":
        y = np.tan(x_rad)
    else:
        print("Invalid trigonometric function.")
        return

    # Create the plot
    plt.plot(x, y)
    plt.title(f"Graph of {function}({angle_type} angle)")
    plt.xlabel("Angle")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

graph_trig_function()
