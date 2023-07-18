import math

def solve_trig_function():
    function = input("Enter the trigonometric function (e.g., sin, cos, tan): ")
    angle_type = input("Enter the angle type (radians or degrees): ")
    angle = float(input("Enter the angle value: "))

    if angle_type.lower() == "degrees":
        angle = math.radians(angle)

    if function.lower() == "sin":
        result = math.sin(angle)
    elif function.lower() == "cos":
        result = math.cos(angle)
    elif function.lower() == "tan":
        result = math.tan(angle)
    else:
        print("Invalid trigonometric function.")
        return

    print(f"The result of {function}({math.degrees(angle):.2f}) is {result:.4f}.")

solve_trig_function()
