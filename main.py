from tkinter import *

from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.window = window
        self.window.title("Cool Cash")
        self.window.geometry("300x266")

        # Account type selection
        self.account_type_label = Label(window, text="select your account type")
        self.account_type_label.pack()

        self.account_type_var = StringVar()
        self.account_type_var.set("savings")

        # savings button
        self.savings_rd = Radiobutton(window, text="Savings", variable=self.account_type_var, value="savings", command=self.update_buttons)
        self.savings_rd.pack()

        # Current button
        self.current_rd = Radiobutton(window, text="Current", variable=self.account_type_var, value="current", command=self.update_buttons)
        self.current_rd.pack()

        # Balance
        self.balance_lbl = Label(window, text="Balance: $10000\nWithdrawal/deposite limit\n$5000")
        self.balance_lbl.pack()

        # withdraw button
        self.withdrawal_btn = Button(master=window, text="Withdrawal", command=self.withdrawal)
        self.withdrawal_btn.pack()

        # Deposit button
        self.deposit_btn = Button(master=window, text="   Deposit   ", command=self.deposit)
        self.deposit_btn.pack()
        # Amount entry
        self.amount_entry = Entry(window)
        self.amount_entry.pack()

        # balance withdrawal limit
        self.balance_value = 10000.00
        self.withdrawal_limit = 5000.00
    def update_buttons(self):
        account_type = self.account_type_var.get()
        if account_type == "Savings":
            self.withdrawal_btn.config(state=NORMAL)
            self.deposit_btn.config(state=NORMAL)
            self.withdrawal_limit = 30000
        elif account_type == "current":
            self.withdrawal_btn.config(state=NORMAL)
            self.deposit_btn.config(state=NORMAL)
            self.deposit_btn.config(state=NORMAL)
            self.withdrawal_limit = float("int")

    def withdrawal(self):
        amount = float(self.amount_entry.get())
        if amount <= self.withdrawal_limit and amount <= self.balance_value:
            self.balance_value -= amount
            self.update_balance_label()
        elif amount > self.withdrawal_limit:
            messagebox.showerror("Error", "Withdrawal limit exceeded")
        else:
            messagebox.showerror("Error", "Insufficient funds")

    def deposit(self):
        amount = float(self.amount_entry.get())
        self.balance_value += amount
        self.update_balance_label()

    def update_balance_label(self):
        self.balance_lbl.config(text="Balance: $" + str(self.balance_value))

window = Tk()
app = BankApp(window)
main_lbl = Label(master=window, text="welcome to Cool Cash")
main_lbl.pack()
window.mainloop()