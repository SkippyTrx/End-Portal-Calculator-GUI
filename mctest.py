# End Portal location calculator, based on location of end portal in the first ring of end portals
 
import math
import tkinter as tk

root = tk.Tk()
root.title("End Portal Location Calculator")

x11_label = tk.Label(root, text="X coordinate:")
x11_label.pack()

x11_entry = tk.Entry(root)
x11_entry.pack()

z11_label = tk.Label(root, text="Z coordinate:")
z11_label.pack()

z11_entry = tk.Entry(root)
z11_entry.pack()

def calculate():
    # clear output 
    output_text.delete(0.0, tk.END)

    # Get the values entered by the user and convert them to ints
    try:
        x11 = x11_entry.get()
        x11 = int(x11)
        z11 = z11_entry.get()
        z11 = int(z11)
    except:
        display_output("Error: Please enter a number in both input fields.")
        return
        
    # Check if the user has entered a value in the input fields
    if x11 == "" or z11 == "":
        # Display an error message if one or both of the input fields are empty
        display_output("Error: Please enter a value in both input fields.")
        return

    # distance from 0,0 (radius)
    r1 = int(math.sqrt((x11**2 + z11**2)))
 
    # variables for which circle, the minimum distance from 0,0, the amount of portals in each circle, and the angle of seperation between each portal
    circle = 10
    minrad = [1280, 4352, 7424, 10496, 13568, 16640, 19712, 22784]
    pcount = [3, 6, 10, 15, 21, 28, 36, 9]
    angle = [120, 60, 36, 24, (360/21), (360/28), 10, 40]
 
    # finds which circle you are in
    if 1279 < r1 < 2817:
        circle = 0
        c = False
    elif 4351 < r1 < 5889:
        circle = 1
        c = False
    elif 7423 < r1 < 8961:
        circle = 2
        c = False
    elif 10495 < r1 < 12033:
        circle = 3
        c = False
    elif 13567 < r1 < 15105:
        circle = 4
        c = False
    elif 16639 < r1 < 18177:
        circle = 5
        c = False
    elif 19711 < r1 < 21249:
        circle = 6
        c = False
    elif 22783 < r1 < 24321:
        circle = 7
        c = False
    else:
        display_output("Invalid Coordinates")
        return
        
    # finds the angle from the postitive x-axis
    a11 = (math.degrees(math.atan2(z11, x11)))
    if a11 < 0:
        a11 = 360 + a11
 
    # open the output file using the with statement
    with open("Server Portal Coords.txt", "a") as output:
        # write the circle number to the text file
        cout = "\nCircle Number: {}\n".format(circle)
        output.write(cout)
 
    # variables for finding aproximate portal locations
    t = pcount[circle]
    s = 1
    a = a11
 
    # open the output file using the with statement
    with open("Server Portal Coords.txt", "a") as output:
 
    # write the circle number to the text file
        cout = "\nCircle Number: {}\n".format(circle + 1)
        output.write(cout)
 
        while t > 0:
            # finding nether portal coords
            x = x11/8
            z = z11/8
            # combining data into a string to write to the text document
            pout = "{}  X: {}    Z: {}    X nether: {}   Z nether: {}\n".format(s, int(x11), int(z11), int(x), int(z))
            # printing and writing to the console and document
            output.write(pout)
            display_output(pout)
            # getting the portal number
            s = s + 1
            # finding the angle from the positive x-axis and calculating coordinates
            a = a + angle[circle]
            x11 = (minrad[circle] + 768) * math.cos(math.radians(a))
            z11 = (minrad[circle] + 768) * math.sin(math.radians(a))
            t = t - 1

# create calculate button    
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

output_text = tk.Text(root)
output_text.pack()

def display_output(output):
    output_text.insert(tk.END, output)
