# Import the customtkinter library
import customtkinter as ctk


# The main widget/window
root = ctk.CTk()
root.geometry('750x450')
root.title("Real Estate Rental Calculator")


# This is the "Initial Capital Investment" section.
initial_capital_frame = ctk.CTkFrame(root)
initial_capital_frame.pack()

initial_capital_label = ctk.CTkLabel(initial_capital_frame, text = "Initial Capital Investment")
initial_capital_label.pack()

purchase_price_label = ctk.CTkLabel(initial_capital_frame, text = "Purchase Price")
purchase_price_label.pack()

mrr_costs_label = ctk.CTkLabel(initial_capital_frame, text = "Make-Rent-Ready Costs")
mrr_costs_label.pack()

down_payment_label = ctk.CTkLabel(initial_capital_frame, text = "Down Payment")
down_payment_label.pack()

closing_costs_label = ctk.CTkLabel(initial_capital_frame, text = "Closing Costs")
closing_costs_label.pack()


# Always include this to actually make the desktop app window pop up.
root.mainloop()
