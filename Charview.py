from tkinter import *
import Charpresent
import Charmodle
class databace:
    def __init__(self):
        self.connect = sqlite3.connect('Characters.db')
            #cursor= little gnome that does you db stuff you you
        self.tomithy = connect.cursor()
            # create tables
        self.tomithy.execute("""CREATE TABLE IF NOT EXISTS characters(
                        name text,
                        class text,
                        race text)""")
#check this
        tomithy.execute("INSERT INTO characters VALUES (bob, bard, gnome)")

        #make changes save
        self.connect.commit()
        #close db connection once done
        self.connect.close()


class input():

    def submit(self, name, clas, race):
        name = window.name.get(self)
        self.databace.tomithy.execute('INSERT INTO databace.charactors (name, clas, race) VALUES (NULL,?,?,?)', (name, clas, race))
        self.databace.tomithy.commit()


class window():
# create window
    root = Tk()
    root.title("Character Builder")
    root.geometry("600x600")
    root.configure(bg = "green")
#create welcome banner
    welcome = Label(root, text="Character Builder", bg="green", fg="black")
    welcome.grid(row=0, column=30)
    # pack means put the widget in the first open space
# Create name entry Label then text box
    namelabel = Label(root, text="Whats your name? ", bg="green", fg="black")
    namelabel.grid(row=1, column=1)
    nametext = Entry(root, textvariable = input.name)
    nametext.grid(row=1, column=2)

# Create class label then scrollbar then list
    claslabel = Label(root, text ="Class? ", bg ="green", fg ="black")
    claslabel.grid(row=2, column=1)
    classcroll = Scrollbar(root)
    classcroll.grid(row=2, column=2)
    clastext = Listbox(root, textvariable= input.clas)
    for i in Charmodle.listc:
        clastext.insert(END, i)
    clastext.grid(row=2, column=3)


# create race label then scrollbar then list
    racelabel = Label(root, text ="Race? ", bg ="green", fg="black")
    racelabel.grid(row=3, column=1)
    racescroll = Scrollbar(root)
    racescroll.grid(row=3, column=2)
    racetext = Listbox(root, textvariable= input.race)
    for i in Charmodle.listr:
        racetext.insert(END, i)
    racetext.grid(row=3, column=2)

# create submit button
    submitb = Button(root,  text = "Submit", command= input.submit())
    submitb.grid(row=5, column=2)

    root.mainloop()
    # when I say open I mean open and stay there, please



