####################################
# Import the customtkinter library #
####################################
import customtkinter as ctk



###############################################
# Functions that will be needed at some point #
###############################################
def calculate_initial_capital():
    purchase_price = int(purchase_price_entry.get())
    down_payment = int(down_payment_entry.get()) * 0.01 * int(purchase_price_entry.get())
    loan_amount = purchase_price - down_payment
    closing_costs = int(closing_costs_entry.get()) * 0.01 * loan_amount
    mrr_costs = int(mrr_costs_entry.get())
    initial_capital = down_payment + closing_costs + mrr_costs
    calculated_initial_capital_label = ctk.CTkLabel(initial_capital_frame, text = "Initial Capital Investment = " + "$" + str(initial_capital))
    calculated_initial_capital_label.grid(row = 3, column = 0, columnspan = 2)

def calculate_monthly_income():
    rent = int(rent_entry.get())
    additional_income = int(additional_income_entry.get())
    monthly_income = rent + additional_income
    calculated_monthly_income_label = ctk.CTkLabel(monthly_income_frame, text = "Monthly Income = " + "$" + str(monthly_income))
    calculated_monthly_income_label.grid(row = 2, column = 0, columnspan = 2)

def calculate_monthly_expenses():
    rent = int(rent_entry.get())
    property_taxes = int(property_taxes_entry.get())
    insurance = int(insurance_entry.get())
    hoa = int(hoa_entry.get())
    maintenance = int(maintenance_entry.get()) * 0.01 * rent
    pest_control = int(pest_control_entry.get())
    property_management = int(property_management_entry.get()) * 0.01 * rent
    additional_expenses = int(additional_expenses_entry.get())
    monthly_expenses = property_taxes + insurance + hoa + maintenance + pest_control + property_management + additional_expenses
    calculated_monthly_expenses_label = ctk.CTkLabel(monthly_expenses_frame, text = "Monthly Expenses = " + "$" + str(monthly_expenses))
    calculated_monthly_expenses_label.grid(row = 5, column = 0, columnspan = 2)

def show_me_the_money():
    calculate_initial_capital()
    calculate_monthly_income()
    calculate_monthly_expenses()



##############################
### The main widget/window ###
##############################
root = ctk.CTk()
root.geometry('750x450')
root.title("Real Estate Rental Calculator")
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)



########################################
## "Initial Capital Investment" frame ##
########################################
initial_capital_frame = ctk.CTkFrame(root)
initial_capital_frame.grid(row = 0)
initial_capital_frame.rowconfigure(0, weight = 1)
initial_capital_frame.rowconfigure(1, weight = 1)
initial_capital_frame.rowconfigure(2, weight = 1)
initial_capital_frame.rowconfigure(3, weight = 1)
initial_capital_frame.columnconfigure(0, weight = 1)
initial_capital_frame.columnconfigure(1, weight = 1)
initial_capital_label = ctk.CTkLabel(initial_capital_frame, text = "Initial Capital Investment")
initial_capital_label.grid(row = 0, column = 0, columnspan = 2)

# "Purchase Price" frame, label, and entry #
purchase_price_frame = ctk.CTkFrame(initial_capital_frame)
purchase_price_frame.grid(row = 1, column = 0)
purchase_price_label = ctk.CTkLabel(purchase_price_frame, text = "Purchase Price")
purchase_price_label.grid()
purchase_price_entry = ctk.CTkEntry(purchase_price_frame, placeholder_text = "$")
purchase_price_entry.grid()

# "Down Payment" frame, label, and entry #
down_payment_frame = ctk.CTkFrame(initial_capital_frame)
down_payment_frame.grid(row = 1, column = 1)
down_payment_label = ctk.CTkLabel(down_payment_frame, text = "Down Payment")
down_payment_label.grid()
down_payment_entry = ctk.CTkEntry(down_payment_frame, placeholder_text = "%")
down_payment_entry.grid()

# "Closing Costs" frame, label, and entry #
closing_costs_frame = ctk.CTkFrame(initial_capital_frame)
closing_costs_frame.grid(row = 2, column = 0)
closing_costs_label = ctk.CTkLabel(closing_costs_frame, text = "Closing Costs")
closing_costs_label.grid()
closing_costs_entry = ctk.CTkEntry(closing_costs_frame, placeholder_text = "%")
closing_costs_entry.grid()

# "Make-Rent-Ready Costs" frame, label, and entry #
mrr_costs_frame = ctk.CTkFrame(initial_capital_frame)
mrr_costs_frame.grid(row = 2, column = 1)
mrr_costs_label = ctk.CTkLabel(mrr_costs_frame, text = "Make-Rent-Ready Costs")
mrr_costs_label.grid()
mrr_costs_entry = ctk.CTkEntry(mrr_costs_frame, placeholder_text = "$")
mrr_costs_entry.grid()



############################
## "Monthly Income" frame ##
############################
monthly_income_frame = ctk.CTkFrame(root)
monthly_income_frame.grid(row = 1)
monthly_income_frame.rowconfigure(0, weight = 1)
monthly_income_frame.rowconfigure(1, weight = 1)
monthly_income_frame.rowconfigure(2, weight = 1)
monthly_income_frame.columnconfigure(0, weight = 1)
monthly_income_frame.columnconfigure(1, weight = 1)
monthly_income_label = ctk.CTkLabel(monthly_income_frame, text = "Monthly Income")
monthly_income_label.grid(row = 0, column = 0, columnspan = 2)

# "Rent" frame, label, and entry #
rent_frame = ctk.CTkFrame(monthly_income_frame)
rent_frame.grid(row = 1, column = 0)
rent_label = ctk.CTkLabel(rent_frame, text = "Rent")
rent_label.grid()
rent_entry = ctk.CTkEntry(rent_frame, placeholder_text = "$")
rent_entry.grid()

# "Additional Income" frame, label, and entry #
additional_income_frame = ctk.CTkFrame(monthly_income_frame)
additional_income_frame.grid(row = 1, column = 1)
additional_income_label = ctk.CTkLabel(additional_income_frame, text = "Additional Income")
additional_income_label.grid()
additional_income_entry = ctk.CTkEntry(additional_income_frame, placeholder_text = "$")
additional_income_entry.grid()



##############################
## "Monthly Expenses" frame ##
##############################
monthly_expenses_frame = ctk.CTkFrame(root)
monthly_expenses_frame.grid(row = 2)
monthly_expenses_frame.rowconfigure(0, weight = 1)
monthly_expenses_frame.rowconfigure(1, weight = 1)
monthly_expenses_frame.rowconfigure(2, weight = 1)
monthly_expenses_frame.rowconfigure(3, weight = 1)
monthly_expenses_frame.rowconfigure(4, weight = 1)
monthly_expenses_frame.rowconfigure(5, weight = 1)
monthly_expenses_frame.columnconfigure(0, weight = 1)
monthly_expenses_frame.columnconfigure(1, weight = 1)
monthly_expenses_label = ctk.CTkLabel(monthly_expenses_frame, text = "Monthly Expenses")
monthly_expenses_label.grid(row = 0, column = 0, columnspan = 2)

# "Property Taxes" frame, label, and entry #
property_taxes_frame = ctk.CTkFrame(monthly_expenses_frame)
property_taxes_frame.grid(row = 1, column = 0)
property_taxes_label = ctk.CTkLabel(property_taxes_frame, text = "Property Taxes")
property_taxes_label.grid()
property_taxes_entry = ctk.CTkEntry(property_taxes_frame, placeholder_text = "$")
property_taxes_entry.grid()

# "Insurance" frame, label, and entry #
insurance_frame = ctk.CTkFrame(monthly_expenses_frame)
insurance_frame.grid(row = 1, column = 1)
insurance_label = ctk.CTkLabel(insurance_frame, text = "Insurance")
insurance_label.grid()
insurance_entry = ctk.CTkEntry(insurance_frame, placeholder_text = "$")
insurance_entry.grid()

# "HOA" frame, label, and entry #
hoa_frame = ctk.CTkFrame(monthly_expenses_frame)
hoa_frame.grid(row = 2, column = 0)
hoa_label = ctk.CTkLabel(hoa_frame, text = "HOA")
hoa_label.grid()
hoa_entry = ctk.CTkEntry(hoa_frame, placeholder_text = "$")
hoa_entry.grid()

# "Maintenance" frame, label, and entry #
maintenance_frame = ctk.CTkFrame(monthly_expenses_frame)
maintenance_frame.grid(row = 2, column = 1)
maintenance_label = ctk.CTkLabel(maintenance_frame, text = "Maintenance")
maintenance_label.grid()
maintenance_entry = ctk.CTkEntry(maintenance_frame, placeholder_text = "%")
maintenance_entry.grid()

# "Pest Control" frame, label, and entry #
pest_control_frame = ctk.CTkFrame(monthly_expenses_frame)
pest_control_frame.grid(row = 3, column = 0)
pest_control_label = ctk.CTkLabel(pest_control_frame, text = "Pest Control")
pest_control_label.grid()
pest_control_entry = ctk.CTkEntry(pest_control_frame, placeholder_text = "$")
pest_control_entry.grid()

# "Property Management" frame, label, and entry #
property_management_frame = ctk.CTkFrame(monthly_expenses_frame)
property_management_frame.grid(row = 3, column = 1)
property_management_label = ctk.CTkLabel(property_management_frame, text = "Property Management")
property_management_label.grid()
property_management_entry = ctk.CTkEntry(property_management_frame, placeholder_text = "%")
property_management_entry.grid()

# "Additional Expenses" frame, label, and entry #
additional_expenses_frame = ctk.CTkFrame(monthly_expenses_frame)
additional_expenses_frame.grid(row = 4, column = 0, columnspan = 2)
additional_expenses_label = ctk.CTkLabel(additional_expenses_frame, text = "Additional Expenses")
additional_expenses_label.grid()
additional_expenses_entry = ctk.CTkEntry(additional_expenses_frame, placeholder_text = "$")
additional_expenses_entry.grid()



############################################
## Button for performing the calculations ##
############################################
calculate_button = ctk.CTkButton(root, text = "Show me the money!", command = show_me_the_money)
calculate_button.grid(row = 3)



#######################################################################
# Always include this to actually make the desktop app window pop up. #
#######################################################################
root.mainloop()
