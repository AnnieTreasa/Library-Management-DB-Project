from tkinter import *


class dashboard(Tk):  # profile page : name,books taken,date
    def __init__(self):
        super().__init__()
        self.geometry("750x500")
        self.resizable(False, False)

    def Label(self):
        self.backGroundImage = PhotoImage(file="bg3.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        self.title = Label(self, text="DASHBOARD", font=(
            'Microsoft Yehei UI Light', 16, 'bold'))
        self.title.place(x=300, y=60)

        self.nameLabel = Label(self, text="Name", font=(
            'Microsoft Yehei UI Light', 11))
        self.nameLabel.place(x=200, y=120)

        self.bookdetailsHead = Label(self, text="Date\t\tTitle\t\tAccession no.", font=(
            'Microsoft Yehei UI Light', 11))
        self.bookdetailsHead.place(x=200, y=170)

    """def Data(self):
        # self.name=Label(self,text=user.name,font=(
        # 'Microsoft Yehei UI Light', 11))
        # self.name.place(x=320, y=120)

        if(books.length == 0):  # using profileFn
            print("No books taken!")
        else:
            # estimate of no of books taken by a student-use for loop
            self.bookdetailsHead = Label(self, text="Date\t\tTitle\t\tAccession no.", font=(
                'Microsoft Yehei UI Light', 11))
            self.bookdetailsHead.place(x=200, y=170)"""


if __name__ == "__main__":
    Dashboard = dashboard()
    Dashboard.Label()
    # Dashboard.Data()
    Dashboard.mainloop()
