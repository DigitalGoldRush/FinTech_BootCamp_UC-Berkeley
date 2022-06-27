#Loan Qualifier Application.
#This is a command line application to match applicants with qualifying loans.

import sys
import fire
import questionary
import csv
from pathlib import Path
from tabulate import tabulate

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


#Ask for the file path of the latest bank data & return it as a CSV file

def load_bank_data():
    csvpath = questionary.text("Greetings Earthling. What is the file path of the current loan data you wish to sort from? The latest prices are in loan_qualifier_app/data/daily_rate_sheet.csv:").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


#Initiate dialogue to get applicant's information and then returns it.

def get_applicant_info():
    
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


# To determine which loans the user qualifies for.
# Criteria is based on credit score, loan size, DTI ration, LTV ratio
# Will return a list of banks willing to underwrite the loan

def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


# Saves the qualifying loans to a CSV file.

def save_qualifying_loans(qualifying_loans):
    
#If the applicant does not qualify for any loans, notification will be sent and program will end.

    if (len)(qualifying_loans) ==0:
        print("You do not qualify for any loans. Please try again in a few months.")

    bank_list = []
    header = ["Lender", "MAX Loan AMT", "MAX LTV", "MAX DTI", "MIN Credit Score", "Interest Rate"]
    print(tabulate(qualifying_loans, headers=header, tablefmt="grid"))
    csv_prompt = questionary.confirm("Would you like to save this list of qualified lenders?").ask()

    if csv_prompt == True:
        csv_path = print("What path to the .csv file will you use?").ask()
        csv_path = questionary.path(csv_path)

    else:
        print("Your answer is noted. I will print the results on the screen")

    

def run():
  
    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)