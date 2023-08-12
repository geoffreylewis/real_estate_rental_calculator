####################################
# Import the customtkinter library #
####################################
import customtkinter as ctk


##############################
### The main widget/window ###
##############################
root = ctk.CTk()
root.geometry('750x450')
root.title("Real Estate Rental Calculator")


##################################################
## "Initial Capital Investment" frame and label ##
##################################################
initial_capital_frame = ctk.CTkFrame(root)
initial_capital_frame.pack()
initial_capital_label = ctk.CTkLabel(initial_capital_frame, text = "Initial Capital Investment")
initial_capital_label.pack()

# "Purchase Price" frame, label, and entry #
purchase_price_frame = ctk.CTkFrame(initial_capital_frame)
purchase_price_frame.pack()
purchase_price_label = ctk.CTkLabel(purchase_price_frame, text = "Purchase Price")
purchase_price_label.pack()
purchase_price_entry = ctk.CTkEntry(purchase_price_frame, placeholder_text = "$")
purchase_price_entry.pack()

# "Down Payment" frame, label, and entry #
down_payment_frame = ctk.CTkFrame(initial_capital_frame)
down_payment_frame.pack()
down_payment_label = ctk.CTkLabel(down_payment_frame, text = "Down Payment")
down_payment_label.pack()
down_payment_entry = ctk.CTkEntry(down_payment_frame, placeholder_text = "%")
down_payment_entry.pack()

# "Closing Costs" frame, label, and entry #
closing_costs_frame = ctk.CTkFrame(initial_capital_frame)
closing_costs_frame.pack()
closing_costs_label = ctk.CTkLabel(closing_costs_frame, text = "Closing Costs")
closing_costs_label.pack()
closing_costs_entry = ctk.CTkEntry(closing_costs_frame, placeholder_text = "%")
closing_costs_entry.pack()

# "Make-Rent-Ready Costs" frame, label, and entry #
mrr_costs_frame = ctk.CTkFrame(initial_capital_frame)
mrr_costs_frame.pack()
mrr_costs_label = ctk.CTkLabel(mrr_costs_frame, text = "Make-Rent-Ready Costs")
mrr_costs_label.pack()
mrr_costs_entry = ctk.CTkEntry(mrr_costs_frame, placeholder_text = "$")
mrr_costs_entry.pack()


##################################################
## "Monthly Income" frame and label ##
##################################################
monthly_income_frame = ctk.CTkFrame(root)
monthly_income_frame.pack()
monthly_income_label = ctk.CTkLabel(monthly_income_frame, text = "Monthly Income")
monthly_income_label.pack()

# "Rent" frame, label, and entry #
rent_frame = ctk.CTkFrame(monthly_income_frame)
rent_frame.pack()
rent_label = ctk.CTkLabel(rent_frame, text = "Rent")
rent_label.pack()
rent_entry = ctk.CTkEntry(rent_frame, placeholder_text = "$")
rent_entry.pack()

# "Additional Income" frame, label, and entry #
additional_income_frame = ctk.CTkFrame(monthly_income_frame)
additional_income_frame.pack()
additional_income_label = ctk.CTkLabel(additional_income_frame, text = "Additional Income")
additional_income_label.pack()
additional_income_entry = ctk.CTkEntry(additional_income_frame, placeholder_text = "$")
additional_income_entry.pack()


#######################################################################
# Always include this to actually make the desktop app window pop up. #
#######################################################################
root.mainloop()
