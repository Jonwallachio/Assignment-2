# import everything from tkinter so we can make a gui
from tkinter import *
from tkinter import ttk
# imports python inbuilt image library
from PIL import ImageTk, Image
# importing strftime function to retrieve system time
from time import strftime


# creates a reference variable to the Tkinter library
# so that we can access its methods
root = Tk()
# creates a reference variable to the Style methods
style = ttk.Style()
# window size is set
root.geometry("350x500")
# title and icon of app changed
root.title("WorkLife App v0.3")
root.iconbitmap(r"icons\rating.ico")
# turn off resizing
root.resizable(False, False)

# class created for the main window


class Window():
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    #
    rating = Canvas(root, width=90, height=90)
    rating.place(x=0, y=0)
    rating_img = ImageTk.PhotoImage(Image.open(r"icons\rating.png"))
    rating.create_image(20, 20, anchor=NW, image=rating_img)
    #


# class which holds the buttons and places them on the gui
class Buttons():
    # 1
    tasks_button_image = PhotoImage(file=r"icons\to-do-list.png")
    tasks_button = Button(root, width=81, height=65, image=tasks_button_image)
    tasks_button.place(x=0, y=430,)
    # 2
    insight_button_img = PhotoImage(file=r"icons\insights.png")
    insights_button = Button(root, width=83, height=65,
                             image=insight_button_img)
    insights_button.place(x=85, y=430)
    # 3
    mindfulness_button_img = PhotoImage(file=r"icons\mindfulness.png")
    mindfulness_button = Button(
        root, width=86, height=65, image=mindfulness_button_img)
    mindfulness_button.place(x=172, y=430)
    # 4
    exercise_button_img = PhotoImage(file=r"icons\calorie_tracker.png")
    exercise_button = Button(root, width=87, height=65,
                             image=exercise_button_img)
    exercise_button.place(x=262, y=430)

# class created to create the icon that holds the health
# score, arguments are a WIP


class HealthScore():
    current_score = 0
    score = Label(root, text=str(current_score))
    score.place(x=380, y=200)


# class which holds the methods that allow the clock to
# display system time, refresh method WIP
class clock():
    def __init__(self):
        time_str = strftime("%H:%M:%S")
        self.time_label = Label(root, font=("calibri", 20, "bold"),
                                foreground="black")
        self.time_label.config(text=time_str)
        self.time_label.place(x=0, y=90)

# class created to hold the attributes and methods for the calendar


class Calendar():
    def date_clicked(self):
        img = PhotoImage(file=r"icons\date_ticked.png")
        click = Label(root, image=img)
        click.pack()

    # creating the buttons for the calendar and placing them in frame
    calendar_button1 = Button(root, width=2, height=1,
                              text="1", command=date_clicked)
    calendar_button1.place(x=152, y=20)

    calendar_button2 = Button(root, width=2, height=1, text="2")
    calendar_button2.place(x=175.5, y=20)

    calendar_button3 = Button(root, width=2, height=1, text="3")
    calendar_button3.place(x=199.5, y=20)

    calendar_button4 = Button(root, width=2, height=1, text="4")
    calendar_button4.place(x=224, y=20)

    calendar_button5 = Button(root, width=2, height=1, text="5")
    calendar_button5.place(x=248, y=20)

    calendar_button6 = Button(root, width=2, height=1, text="6")
    calendar_button6.place(x=272, y=20)

    calendar_button7 = Button(root, width=2, height=1, text="7")
    calendar_button7.place(x=296, y=20)

    calendar_button8 = Button(root, width=2, height=1, text="8")
    calendar_button8.place(x=152, y=47)

    calendar_button9 = Button(root, width=2, height=1, text="9")
    calendar_button9.place(x=175.5, y=47)

    calendar_button10 = Button(root, width=2, height=1, text="10")
    calendar_button10.place(x=199.5, y=47)

    calendar_button11 = Button(root, width=2, height=1, text="11")
    calendar_button11.place(x=224, y=47)

    calendar_button12 = Button(root, width=2, height=1, text="12")
    calendar_button12.place(x=248, y=47)

    calendar_button13 = Button(root, width=2, height=1, text="13")
    calendar_button13.place(x=272, y=47)

    calendar_button14 = Button(root, width=2, height=1, text="14")
    calendar_button14.place(x=296, y=47)

    calendar_button15 = Button(root, width=2, height=1, text="15")
    calendar_button15.place(x=152, y=74)

    calendar_button16 = Button(root, width=2, height=1, text="16")
    calendar_button16.place(x=175.5, y=74)

    calendar_button17 = Button(root, width=2, height=1, text="17")
    calendar_button17.place(x=200.5, y=74)

    calendar_button18 = Button(root, width=2, height=1, text="18")
    calendar_button18.place(x=224, y=74)

    calendar_button19 = Button(root, width=2, height=1, text="19")
    calendar_button19.place(x=248, y=74)

    calendar_button20 = Button(root, width=2, height=1, text="20")
    calendar_button20.place(x=272, y=74)

    calendar_button21 = Button(root, width=2, height=1, text="21")
    calendar_button21.place(x=296, y=74)

    calendar_button22 = Button(root, width=2, height=1, text="22")
    calendar_button22.place(x=152, y=100)

    calendar_button23 = Button(root, width=2, height=1, text="23")
    calendar_button23.place(x=175.5, y=100)

    calendar_button24 = Button(root, width=2, height=1, text="24")
    calendar_button24.place(x=199.5, y=100)

    calendar_button25 = Button(root, width=2, height=1, text="25")
    calendar_button25.place(x=224, y=100)

    calendar_button26 = Button(root, width=2, height=1, text="26")
    calendar_button26.place(x=248, y=100)

    calendar_button27 = Button(root, width=2, height=1, text="27")
    calendar_button27.place(x=272, y=100)

    calendar_button28 = Button(root, width=2, height=1, text="28")
    calendar_button28.place(x=296, y=100)


# clock is defined and called
refresh = clock()
refresh.__init__

# event loop
root.mainloop()
