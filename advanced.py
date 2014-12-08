import urllib2
import json
import csv

c = csv.writer(open("analysis output.csv", "wb"))

urlIncomeStatement = 'http://dev.c0l.in:8888'
apiIncomeStatement = urllib2.urlopen(urlIncomeStatement)
dataIncomeStatement = json.load(apiIncomeStatement)

urlFinancialPosition = 'http://dev.c0l.in:9999'
apiFinancialPosition = urllib2.urlopen(urlFinancialPosition)
dataFinancialPosition = json.load(apiFinancialPosition)

print "Printing Income Statements for technology companies: "

for item in dataIncomeStatement:
    
    name = item['company']['name']
    cost_of_sales = int(item['company']['opening_stock'] + item['company']['purchases'] - item['company']['closing_stock'])
    gross_profit = int(item['company']['sales'] - cost_of_sales )
    net_profit = int(gross_profit - item['company']['expenses'])
    profit_for_the_period = int(net_profit - item['company']['interest_payable'] + item['company']['interest_receivable'])

    if item['sector'] == 'technology':
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

for item in dataFinancialPosition:

    totalEquityAndLiabilities = int(item['company']['equity'] + item['company']['non_current_liabilities'] + item['company']['current_liabilities'])
    totalAssets = int(item['company']['current_liabilities'] + item['company']['non_current_liabilities'] + item['company']['equity'])

    if item['sector'] == 'technology':
        c.writerow([name,
                    str(item['company']['current_liabilities']),
                    str(item['company']['non_current_liabilities']),
                    str(item['company']['equity']),
                    str(item['company']['non_current_assets']),
                    str(totalEquityAndLiabilities),
                    str(totalAssets)])

print "Done printing Financial Positions for technology companies."
