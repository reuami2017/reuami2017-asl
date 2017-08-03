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
        master.minsize(width=800, height=700)
        master.maxsize(width=800, height=700)
        self.pack()
        # self.create_widgets()
        signs = interp.demo_predict(db)
        tk.Label(self, text="Right").grid(row=1,column=1)
        tk.Label(self, text="Left").grid(row=1, column=2)
        tk.Label(self, text="Right1").grid(row=1, column=3)
        tk.Label(self, text="Left1").grid(row=1, column=4)
        for i in range(4):
            # index needs to start at 1 and go to 4
            j = 2
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


def update():
    """
    updates the frame
    :return: none
    """
    signs = interp.demo_predict(db)
    # app.grid_forget()  # destroy the grid
    for label in app.grid_slaves():
        if int(label.grid_info()["row"]) > 1: # dont remove the first row that contains the names
            label.grid_forget()
    for i in range(4):
        # index needs to start at 1 and go to 4, hence the i+1 later
        j = 2
        for sign in signs[i]:
            app.make_button(sign, j, i+1)
            j += 1
    root.after(2000, update)
    print(signs)

if __name__ == "__main__":
    db = interp.pd.read_pickle("newdb.pkl")
    root = tk.Tk()
    root.after(2000, update)
    app = Application(master=root)
    app.mainloop()
