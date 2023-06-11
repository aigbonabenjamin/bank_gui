from tkinter import *
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Bank App")
        self.root.geometry("300x250")

        # Account type selection
        self.account_type_label = Label(root, text="Select Account Type:")
        self.account_type_label.pack()

        self.account_type_var = StringVar()
        self.account_type_var.set("savings")

        self.savings_radio = Radiobutton(root, text="Savings", variable=self.account_type_var, value="savings", command=self.open_transaction_window)
        self.savings_radio.pack()

        self.current_radio = Radiobutton(root, text="Current", variable=self.account_type_var, value="current", command=self.open_transaction_window)
        self.current_radio.pack()

        # Initialize balance and withdrawal limit
        self.balance = 0.00
        self.withdrawal_limit = 30000.00

    def open_transaction_window(self):
        account_type = self.account_type_var.get()
        if account_type == "savings":
            self.withdrawal_limit = 30000.00
        elif account_type == "current":
            self.withdrawal_limit = float("inf")
        self.root.withdraw()  # Hide the main window
        transaction_window = Toplevel()  # Create a new window for transactions
        transaction_window.title("Transactions")
        transaction_window.geometry("300x200")

        # Balance label
        balance_label = Label(transaction_window, text=f"Balance: ${self.balance:.2f}")
        balance_label.pack()

        # Withdraw button
        withdraw_button = Button(transaction_window, text="Withdraw", command=self.withdraw)
        withdraw_button.pack()

        # Deposit button
        deposit_button = Button(transaction_window, text="Deposit", command=self.deposit)
        deposit_button.pack()


        amount_entry = Entry(transaction_window)
        amount_entry.pack()

        def close_transaction_window():
            transaction_window.destroy()  # Close the transaction window
            self.root.deiconify()  # Show the main window again

        # Close button
        close_button = Button(transaction_window, text="Close", command=close_transaction_window)
        close_button.pack()

    def withdraw(self):
        amount = float(amount_entry.get())
        if amount <= self.withdrawal_limit and amount <= self.balance:
            self.balance -= amount
            balance_label.config(text=f"Balance: ${self.balance:.2f}")
        elif amount > self.withdrawal_limit:
            messagebox.showerror("Error", "Withdrawal limit exceeded")
        else:
            messagebox.showerror("Error", "Insufficient funds")

    def deposit(self):
        amount = amount_entry.get()
        self.balance += amount
        balance_label.config(text=f"Balance: ${self.balance:.2f}")


# Create the main window
root = Tk()
app = BankApp(root)
root.mainloop()