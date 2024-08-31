import tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(height=400, width=850)

def bmi():
    height = float(h_entry.get())
    weight = float(w_entry.get())
    value = weight / (height / 100) ** 2
    value_l.config(text=f"Your BMI is:{value:.2f}")

    if value<18.5:
        final_value.config(text="You're  UnderWeight")
    elif (value>18.5 and value<25):
        final_value.config(text="You're Normal ")
    elif (value>25 and value<30):
        final_value.config(text="You're Overweight")
    elif(value>30 and value<35):
        final_value.config(text="You're Obese")
    elif(value>35):
        final_value.config(text="You're Extremly Obese")


heading = tkinter.Label(text="BMI Calculator", font=("Arial",24))
heading.pack()

height = tkinter.Label(text="Height(cm)", font=("Arial",18))
height.place(x=70, y= 70)
h_entry = tkinter.Entry(window)
h_entry.place(x=210, y=78)

weight = tkinter.Label(text="Weight(kg)", font=("Arial",18))
weight.place(x=67, y= 110)
w_entry = tkinter.Entry(window)
w_entry.place(x=210, y=118)

calculate = tkinter.Button(text="Calculate", font=("Arial",18), command= bmi)
calculate.place(x=150,y=155)

value_l = tkinter.Label(text="", font=("Arial",18))
value_l.place(x=100,y=220)

final_value = tkinter.Label(text="", font=("Arial",18))
final_value.place(x=100,y=250)

original_image = Image.open("C:\\Users\\sathv\\Downloads\\stock-vector-body-mass-index-vector-illustration-from-underweight-to-extremely-obese-man-with-different-obesity-2360333187-transformed.jpeg")
resized_image = original_image.resize((500,300))
new_image = ImageTk.PhotoImage(resized_image)
image_l = tkinter.Label(window, image=new_image)
image_l.place(x=350,y=50)

window.mainloop()