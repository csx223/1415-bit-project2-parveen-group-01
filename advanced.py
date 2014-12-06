import urllib2
import json
import csv

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
        print "------------------------------------------"
        print str(item['sector']), name + ":"
        print name + "'s interest purchases - " + str(item['company']['purchases'])
        print name + "'s interest payable - " + str(item['company']['interest_payable'])
        print name + "'s interest sales - " + str(item['company']['sales'])
        print name + "'s interest expenses - " + str(item['company']['expenses'])
        print name + "'s interest opening stock - " + str(item['company']['opening_stock'])
        print name + "'s interest closing stock - " + str(item['company']['closing_stock'])
        print name + "'s interest interest recivables - " + str(item['company']['interest_receivable'])                  
        print name + "'s interest cost of sales - " + str(cost_of_sales)
        print name + "'s interest gross profit - " + str(gross_profit)
        print name + "'s interest net profit - " + str(net_profit)
        print name + "'s interest profit for the period of time - " + str(profit_for_the_period)
        print "-----------------------------------------"

print "Done printing Income Statements for technology companies."
print "Printing Financial Positions for technology companies: "

for item in dataFinancialPosition:

    totalEquityAndLiabilities = int(item['company']['equity'] + item['company']['non_current_liabilities'] + item['company']['current_liabilities'])
    totalAssets = int(item['company']['current_liabilities'] + item['company']['non_current_liabilities'] + item['company']['equity'])

    if item['sector'] == 'technology':
        print "-----------------------------------------"
        print item['company']['name'] + "'s current liabilities - " + str(item['company']['current_liabilities'])
        print item['company']['name'] + "'s non-current liabilities - " + str(item['company']['non_current_liabilities'])
        print item['company']['name'] + "'s equity - " + str(item['company']['equity'])
        print item['company']['name'] + "'s non-current assets - " + str(item['company']['non_current_assets'])
        print item['company']['name'] + "'s total Equity And Liabiliites - " + str(totalEquityAndLiabilities)
        print item['company']['name'] + "'s total Assets - " + str(totalAssets)
        print "-----------------------------------------"

print "Done printing Financial Positions for technology companies."
