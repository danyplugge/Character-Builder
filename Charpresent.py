from Charview import *
from Charmodle import *
class input():

    def submit(self, name, clas, race):
        self.databace.tomithy.execute('INSERT INTO databace.charactors (name, clas, race) VALUES (NULL,?,?,?)', (name, clas, race))
        self.databace.tomithy.commit()
        confirmation = Label(root)




