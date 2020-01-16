from tkinter import *
from Charpresent import *
from Charmodle import *
class window():


    def submit(self):
        name = nametext.get(self)
        clas = clastext.get(self)
        race = racetext.get(self)
        confirmation = Label(root, text= name, class, race)
    root = Tk()
    root.title("Character Builder")
    root.geometry("600x600")
    root.configure(bg = "green")

    welcome = Label(root, text="Character Builder", bg="green", fg="black")
    welcome.grid(row=0, column=30)
    # pack means put the widget in the first open space
    namelabel = Label(root, text="Whats your name? ", bg="green", fg="black")
    nametext = Entry(root)
    namelabel.grid(row=1, column=1)
    nametext.grid(row=1, column=2)


    claslabel = Label(root, text ="Class? ", bg ="green", fg ="black")
    classcroll = Scrollbar(root)
    clastext = Listbox(root, yscrollcommand = classcroll.set)
    for i in listc:
        clastext.insert(END, i)
    classcroll.grid(row=2, column=2)
    claslabel.grid(row=2, column=1)
    clastext.grid(row=2, column=3)



    racelabel = Label(root, text ="Race? ", bg ="green", fg="black")
    racescroll = Scrollbar(root)
    racetext = Listbox(root, yscrollcommand = racescroll.set)
    for i in listr:
        racetext.insert(END, i)
    racelabel.grid(row=3, column=1)
    racescroll.grid(row=3, column=2)
    racetext.grid(row=3, column=2)

    weaponlabel = Label(root, text ="Weapons ", bg ="green", fg="black")
    weapon1 = Checkbutton(root)
    weaponlabel.grid(row=4, column=1)
    weapon1.grid(row=4, column=2)

    submitb = Button(root,  text = "Submit", command= submit())
    submitb.grid(row=5, column=2)

    root.mainloop()
    # when I say open I mean open and stay there, please



