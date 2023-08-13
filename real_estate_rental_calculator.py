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


##################################################
## "Monthly Expenses" frame and label ##
##################################################
monthly_expenses_frame = ctk.CTkFrame(root)
monthly_expenses_frame.pack()
monthly_expenses_label = ctk.CTkLabel(monthly_expenses_frame, text = "Monthly Expenses")
monthly_expenses_label.pack()

# "Property Taxes" frame, label, and entry #
property_taxes_frame = ctk.CTkFrame(monthly_expenses_frame)
property_taxes_frame.pack()
property_taxes_label = ctk.CTkLabel(property_taxes_frame, text = "Property Taxes")
property_taxes_label.pack()
property_taxes_entry = ctk.CTkEntry(property_taxes_frame, placeholder_text = "$")
property_taxes_entry.pack()

# "Insurance" frame, label, and entry #
insurance_frame = ctk.CTkFrame(monthly_expenses_frame)
insurance_frame.pack()
insurance_label = ctk.CTkLabel(insurance_frame, text = "Insurance")
insurance_label.pack()
insurance_entry = ctk.CTkEntry(insurance_frame, placeholder_text = "$")
insurance_entry.pack()

# "HOA" frame, label, and entry #
hoa_frame = ctk.CTkFrame(monthly_expenses_frame)
hoa_frame.pack()
hoa_label = ctk.CTkLabel(hoa_frame, text = "HOA")
hoa_label.pack()
hoa_entry = ctk.CTkEntry(hoa_frame, placeholder_text = "$")
hoa_entry.pack()

# "Maintenance" frame, label, and entry #
maintenance_frame = ctk.CTkFrame(monthly_expenses_frame)
maintenance_frame.pack()
maintenance_label = ctk.CTkLabel(maintenance_frame, text = "Maintenance")
maintenance_label.pack()
maintenance_entry = ctk.CTkEntry(maintenance_frame, placeholder_text = "%")
maintenance_entry.pack()

# "Pest Control" frame, label, and entry #
pest_control_frame = ctk.CTkFrame(monthly_expenses_frame)
pest_control_frame.pack()
pest_control_label = ctk.CTkLabel(pest_control_frame, text = "Pest Control")
pest_control_label.pack()
pest_control_entry = ctk.CTkEntry(pest_control_frame, placeholder_text = "$")
pest_control_entry.pack()

# "Property Management" frame, label, and entry #
property_management_frame = ctk.CTkFrame(monthly_expenses_frame)
property_management_frame.pack()
property_management_label = ctk.CTkLabel(property_management_frame, text = "Property Management")
property_management_label.pack()
property_management_entry = ctk.CTkEntry(property_management_frame, placeholder_text = "%")
property_management_entry.pack()

# "Additional Expenses" frame, label, and entry #
additional_expenses_frame = ctk.CTkFrame(monthly_expenses_frame)
additional_expenses_frame.pack()
additional_expenses_label = ctk.CTkLabel(additional_expenses_frame, text = "Additional Expenses")
additional_expenses_label.pack()
additional_expenses_entry = ctk.CTkEntry(additional_expenses_frame, placeholder_text = "$")
additional_expenses_entry.pack()


#######################################################################
# Always include this to actually make the desktop app window pop up. #
#######################################################################
root.mainloop()
