# --------------------------------Python Package-----------------------------------#
import tkinter as tk


class BMI:
    def __init__(self, height: float, weight: float):
        self.height = height
        self.weight = weight

    def getBMI(self):
        try:
            height = self.height/100
            bmi = self.weight/(height*height)
            return bmi
        except Exception:
            return 'False'

    def getBMIInfo(self):
        bmi = self.getBMI()
        bmi = float(bmi)
        try:
            if 0 < bmi < 18.5:
                return "You Are Under Weight"
            elif 18.5 <= bmi <= 24:
                return "You Are Normal"
            elif 24 < bmi <= 29.9:
                return "You Are Over Weight"
            else:
                return "BMI is out of range"
        except Exception:
            pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x300+500+150")
        self.title("BMI Calculator")
        self.resizable(width=False, height=False)
        self.wm_iconbitmap("image/bmi.ico")

        # ----------------------------------------Variable-----------------------------------------#
        self.height = tk.StringVar()
        self.weight = tk.StringVar()
        self.bmi = tk.StringVar()
        self.info = tk.StringVar()

        # ------------------------------------------Body-------------------------------------------#
        frame = tk.Frame(self, width=300, height=300, bg='light blue')
        frame.place(x=0, y=0)

        frame1 = tk.Frame(frame, width=280, height=80, bg="light grey")
        frame1.place(x=10, y=20)

        label = tk.Label(frame1, text='Enter Your Weight In (Kg)', font=("Courier", 10, 'bold'))
        label.place(x=10, y=15)

        entry = tk.Entry(frame1, textvariable=self.weight, width=5, font=("bold", 11), fg="dark blue", justify="right")
        entry.place(x=225, y=15)

        entry.config(validate='key', validatecommand=(self.register(self.validate_weight), '%P'))

        label1 = tk.Label(frame1, text='Enter Your Height In (CM)', font=("Courier", 10, 'bold'))
        label1.place(x=10, y=35)

        entry1 = tk.Entry(frame1, textvariable=self.height, width=5, font=("bold", 11,), fg="dark blue", justify='right')
        entry1.place(x=225, y=35)

        entry1.config(validate='key', validatecommand=(self.register(self.validate_height), '%P'))

        but = tk.Button(frame, text="Calculate Your BMI", font=("Courier", 12, 'bold'), command=self.calculate, width=22,
                     bg='orange', borderwidth=10)
        but.place(x=28, y=110)

        entry2 = tk.Entry(frame, textvariable=self.bmi, state='readonly', justify="right", borderwidth=5,
                       font=("Courier", 12, "bold"), fg='red')
        entry2.place(x=45, y=165)

        entry3 = tk.Entry(frame, textvariable=self.info, state='readonly', borderwidth=5,
                       font=("Courier", 12, 'bold'), fg='green', width=24)
        entry3.place(x=25, y=255)

        but1 = tk.Button(frame, text="Get Information", font=("Courier", 12, 'bold'), command=self.information,
                      borderwidth=7, bg='orange')
        but1.place(x=25, y=205)

        but2 = tk.Button(frame, text="Clear", command=self.clear, font=("Courier", 13, 'bold'), fg='blue',
                      bg='light blue', borderwidth=7)
        but2.place(x=207, y=205)

    # --------------------------------Define function-----------------------------------#
    #                    ------------Clear Function------------                        #

    def clear(self):
        self.height.set("")
        self.weight.set("")
        self.bmi.set("")
        if self.info.get != "":
            self.info.set("")
        else:
            pass

    #                    -------------Main Function-------------                       #

    # noinspection PyBroadException
    def information(self):
        if self.height.get() == "" or self.weight.get() == "":
            self.info.set("Provide me detail.")
        else:
            s = BMI(float(self.height.get()), float(self.weight.get()))
            try:
                self.info.set(s.getBMIInfo())
            except Exception:
                pass

    #                     ------------Calculation Function-------------                                 #
    # noinspection PyBroadException
    def calculate(self):
        if self.height.get() == "" or self.weight.get() == "":
            self.bmi.set("Provide me detail.")
        else:
            s = BMI(float(self.height.get()), float(self.weight.get()))
            self.bmi.set("%.2f" % (s.getBMI()))

    #               --------------Validate Key for only number is allow----------------                #
    def validate_height(self, user_height):
        if user_height.isdigit():
            return True
        elif user_height == "":
            return True
        else:
            # mb.showinfo("Error",'Height should be Numbered')
            return False

    def validate_weight(self, user_weight):
        if user_weight.isdigit():
            return True
        elif user_weight == "":
            return True
        else:
            return False


if __name__ == '__main__':
    window = App()
    window.mainloop()

