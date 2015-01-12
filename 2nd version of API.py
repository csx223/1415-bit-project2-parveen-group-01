import urllib
import urllib2
import json
import csv

#Income statement and Financial position CSV writer
IncomeStatementCSV = csv.writer(open("Income Statement.csv", "wb"))
FinancialPositionCSV = csv.writer(open("Financial Position.csv", "wb"))

#Financial position data fetched from API
financial_position_url = "http://dev.c0l.in:5984/financial_positions/_all_docs"
financial_request = urllib2.urlopen(financial_position_url).read()
financial_response = json.loads(financial_request)

#Income statement data fetched from API
income_statement_url = "http://dev.c0l.in:5984/income_statements/_all_docs"
income_statement_request = urllib2.urlopen(income_statement_url).read()
income_response = json.loads(income_statement_request)

def help():
        print ("")
        print ("Possible sectors:")
        print ("Technology")
        print ("Healthcare")
        print ("Industrial goods")
        print ("Financial")
        print ("Utilities")
        print ("Basic materials")
        print ("Services")
        print ("")
        print ("All possible keys for Financial Position:")
        print ("Name")
        print ("Non current assets")
        print ("Current assets")
        print ("Equity")
        print ("Non current liabilities")
        print ("Current liabilities")
        print ("")
        print ("All possible keys for Income Statement:")
        print ("Name")
        print ("Sales")
        print ("Opening stock")
        print ("Pusrchases")
        print ("Closing stock")
        print ("Expenses")
        print ("Interest payble")
        print ("Interest recivable")
        print ("")
        


        
def user_input1():
    #User is asked to input which statement he would like to examine and then he is sent to next function
    user_input = raw_input('What financial statement would you like to examine?: ')
    if user_input == ("financial position") or user_input ==("financial"):
        financial_position_fn()
    elif user_input == ("income statement") or user_input ==("income"):
        income_statement_fn()
    elif user_input == "help":
        help()
        user_input1()
    else:
        user_input = raw_input("Please enter FINANCIAL POSITION either INCOME STATEMENT: ")
        user_input1()

def financialSector():
    #User inputs sector of interest, afterwards CSV writer writes headlines
    ask = raw_input("Would you like to sort data by particular key?: ")
    if ask == "help":
        help()
        financialSector()
    elif ask == ("yes") or ask == ("y"):
        key = raw_input("What is the key you would like to sort?: ")
    elif ask == "no" or ask == "n":
        key = 'sector'
        print "Proceeding without filter"
    FinancialPositionCSV.writerow([
                'Name',
                'Non current assets',
                'Current assets',
                'Equity',
                'Non current liabilities',
                'Current liabilities'])
    
    #This segment of code asigns iteration key 'sector'
    for item in financial_response['rows']:
        fp_url = "http://dev.c0l.in:5984/financial_positions/" + item['id']
        fp_request = urllib2.urlopen(fp_url).read()
        fp_response = json.loads(fp_request)
        
        #After user inputs sector of interest, IF function prints all the data asignet to that specific sector into CSV file
        if fp_response.get(key, None) == key:
            count += 1
            FinancialPositionCSV.writerow([
             fp_response['company']['name'],
             fp_response['company']['non_current_assets'],
             fp_response['company']['current_assets'],
             fp_response['company']['equity'],
             fp_response['company']['non_current_liabilities'],
             fp_response['company']['current_liabilities']])
            print ("Printing DATA")
        
def incomeSector():
    #User inputs sector of interest, afterwards CSV writer writes headlines
    user_input3 = raw_input("Which sector would you like to iterate through in Income Statement?: ")
    if user_input3 == "help":
        help()
        incomeSector()
    IncomeStatementCSV.writerow([
                'Name',
                'Sales',
                'Opening stock',
                'Pusrchases',
                'Closing stock',
                'Expenses',
                'Interest payble',
                'Interest recivable'])
    
    #This segment of code asigns iteration key 'sector'
    for item in income_response['rows']:
        is_url = "http://dev.c0l.in:5984/income_statements/" + item['id']
        is_request = urllib2.urlopen(is_url).read()
        is_response = json.loads(is_request)

        #After user inputs sector of interest, IF function prints all the data asignet to that specific sector into CSV file
        if is_response.get('sector', None) == user_input3:
            count += 1                            
            IncomeStatementCSV.writerow([
             is_response['company']['name'],
             is_response['company']['sales'],
             is_response['company']['opening_stock'],
             is_response['company']['purchases'],
             is_response['company']['closing_stock'],
             is_response['company']['expenses'],
             is_response['company']['interest_payable'],
             is_response['company']['interest_receivable']])
            print ("Printing DATA")

#Counts how many entries were printed to CSV file
def financial_position_fn():
    count = 0
    financialSector()
    print ("Done. Your data is stored in Financial Position.csv file. It contains '%s' entries.") % (count)

#Counts how many entries were printed to CSV file          
def income_statement_fn():
    count = 0
    incomeSector()
    print ("Done. Your data is stored in Income Statement.csv file. It contains '%s' entries.") % (count)

print ('If you need some help, type HELP. It works no matter where you type it in.')
print ("")
user_input1()
