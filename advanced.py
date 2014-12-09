# libraries script is using
import urllib2
import json
import csv
# CSV writer (creates file called analysis output.csv and makes it writable "wb")
c = csv.writer(open("analysis output.csv", "wb"))
# actual API's url for Income Statements
urlIncomeStatement = 'http://dev.c0l.in:8888'
# urllib2 opens url and extracts data from it
apiIncomeStatement = urllib2.urlopen(urlIncomeStatement)
# json formats extracted data into apropriate format
dataIncomeStatement = json.load(apiIncomeStatement)
# actual API's url for Financial Positions
urlFinancialPosition = 'http://dev.c0l.in:9999'
# urllib2 opens url and extracts data from it
apiFinancialPosition = urllib2.urlopen(urlFinancialPosition)
# json formats extracted data into apropriate format
dataFinancialPosition = json.load(apiFinancialPosition)

print "Printing Income Statements for technology companies: "
# Start of algorith for sorting technology sector in Income Statement API
for item in dataIncomeStatement:
    # defining variables
    name = item['company']['name']
    cost_of_sales = int(item['company']['opening_stock'] + item['company']['purchases'] - item['company']['closing_stock'])
    gross_profit = int(item['company']['sales'] - cost_of_sales )
    net_profit = int(gross_profit - item['company']['expenses'])
    profit_for_the_period = int(net_profit - item['company']['interest_payable'] + item['company']['interest_receivable'])
    # by help of IF command, script is looking only for technology sector
    # and extracts all the data about it
    if item['sector'] == 'technology':
        # calling for CSV writer to export name, purchases, interest payable,
        # sales, expenses, opening stock, closing stok and interest recivable.
        c.writerow([name,
                    str(item['company']['purchases']),
                    str(item['company']['interest_payable']),
                    str(item['company']['sales']),
                    str(item['company']['expenses']),
                    str(item['company']['opening_stock']),
                    str(item['company']['closing_stock']),
                    str(item['company']['interest_receivable']),
                    str(cost_of_sales),
                    str(gross_profit),
                    str(net_profit),
                    str(profit_for_the_period)]),
        
    
print "Done printing Income Statements for technology companies."
print "Printing Financial Positions for technology companies: "
# Start of algorith for sorting technology sector in Financial Position API
for item in dataFinancialPosition:
    # defining variables
    totalEquityAndLiabilities = int(item['company']['equity'] + item['company']['non_current_liabilities'] + item['company']['current_liabilities'])
    totalAssets = int(item['company']['current_liabilities'] + item['company']['non_current_liabilities'] + item['company']['equity'])
    # same IF function 
    if item['sector'] == 'technology':
        # calling for CSV writer to export name, current liabilities, non current
        # liabilities, equity and non current assets
        c.writerow([name,
                    str(item['company']['current_liabilities']),
                    str(item['company']['non_current_liabilities']),
                    str(item['company']['equity']),
                    str(item['company']['non_current_assets']),
                    str(totalEquityAndLiabilities),
                    str(totalAssets)])

print "Done printing Financial Positions for technology companies."
