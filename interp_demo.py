"""
A demo file for the interpreter. Should create a graphical display for the predictor.
@author: Kesavan Kushalnagar
"""

import tkinter as tk
import webbrowser
import new_db_interpreter as interp


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # self.create_widgets()
        signs = interp.demo_predict(db)
        for i in range(4):
            # index needs to start at 1 and go to 4
            j = 1
            for sign in signs[i]:
                self.make_button(sign, j, i+1)
                j += 1


    def make_button(self, text, row, column):
        self.new = tk.Button(self)
        self.new["text"] = text
        cleaned = '-'.join(text.split())  # split by spaces, then add dashes.
        # This puts it in the proper format for urls on signasl.org
        # self.new["command"] = self.gotourl("www.signasl.org/sign/" + cleaned)
        self.new["command"] = lambda: self.gotourl("www.signasl.org/sign/" + cleaned)
        # self.new.pack(side='top')
        self.new.grid(row=row, column=column)

    def say_hi(self):
        print("hi there, everyone!")
        # print(pop)

    def gotourl(self, url):
        webbrowser.open_new(url)

db = interp.pd.read_pickle("newdb.pkl")


def update():
    signs = interp.demo_predict(db)
    app.grid_forget()  # destroy the grid
    # for i in range(4):
    #     # index needs to start at 1 and go to 4
    #     j = 1
    #     for sign in signs[i]:
    #         app.make_button(sign, j, i+1)
    #         j += 1
    # root.after(2000, update)
    print(signs)

root = tk.Tk()
root.after(2000, update)
app = Application(master=root)
app.mainloop()
