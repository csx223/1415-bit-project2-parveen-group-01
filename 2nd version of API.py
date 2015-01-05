import urllib
import urllib2
import json
import csv
import thread
import time

IncomeStatementCSV = csv.writer(open("Income Statement.csv", "wb"))
FinancialPositionCSV = csv.writer(open("Financial Position.csv", "wb"))

financial_position_url = "http://dev.c0l.in:5984/financial_positions/_all_docs"
financial_request = urllib2.urlopen(financial_position_url).read()
financial_response = json.loads(financial_request)

income_statement_url = "http://dev.c0l.in:5984/income_statements/_all_docs"
income_statement_request = urllib2.urlopen(income_statement_url).read()
income_response = json.loads(income_statement_request)

        
def financial_position_fn():
    count = 0
    user_input2 = raw_input('Which sector would you like to iterate through in Financial Position?: ')
    for item in financial_response['rows']:
        fp_url = "http://dev.c0l.in:5984/financial_positions/" + item['id']
        fp_request = urllib2.urlopen(fp_url).read()
        fp_response = json.loads(fp_request)
        if fp_response.get('sector', None) == user_input2:
            count += 1
            FinancialPositionCSV.writerow([
             fp_response['company']['name'],
             fp_response['company']['non_current_assets'],
             fp_response['company']['current_assets'],
             fp_response['company']['equity'],
             fp_response['company']['non_current_liabilities'],
             fp_response['company']['current_liabilities']])
            print ("Printing DATA")
    print ("Done. Your data is stored in Financial Position.csv file. It contains '%s' entries.") % (count)


            
def income_statement_fn():
    count = 0
    user_input3 = raw_input("Which sector would you like to iterate through in Income Statement?: ")
    for item in income_response['rows']:
        is_url = "http://dev.c0l.in:5984/income_statements/" + item['id']
        is_request = urllib2.urlopen(is_url).read()
        is_response = json.loads(is_request)
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
    print ("Done. Your data is stored in Financial Position.csv file. It contains '%s' entries.") % (count)




def user_input1():
    user_input = raw_input('What financial statement would you like to examine?: ')
    if user_input == ("financial position") or user_input ==("financial"):
            financial_position_fn()
    elif user_input == ("income statement") or user_input ==("income"):
            income_statement_fn()

            
user_input1()
