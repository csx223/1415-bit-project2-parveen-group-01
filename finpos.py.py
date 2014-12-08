import urllib2
import json

urlIncomeStatement = 'http://dev.c0l.in:8888'
apiIncomeStatement = urllib2.urlopen(urlIncomeStatement)
dataIncomeStatement = json.load(apiIncomeStatement)

urlFinancialPosition = 'http://dev.c0l.in:9999'
apiFinancialPosition = urllib2.urlopen(urlFinancialPosition)
dataFinancialPositiont = json.load(apiFinancialPosition)


for item in dataIncomeStatement:
    
    name = item['company']['name']
    interestPayable = item['company']['interest_payable']
    interestReceivable = item['company']['interest_receivable']
    sales = item['company']['interest_receivable']
    expenses = item['company']['expenses']
    openingStock = item['company']['opening_stock']
    closingStock = item['company']['closing_stock']
    
    if item['sector'] == 'technology':
        name + "'s interest payable - " + str(interestPayable)
        name + "'s interest receivable - " + str(interestReceivable)
        name + "'s interest receivable - " + str(sales)
        name + "'s interest receivable - " + str(expenses)
        name + "'s interest receivable - " + str(openingStock)
        name + "'s interest receivable - " + str(closingStock)

for item in dataFinancialPositiont:

    currentLiabilities = item['company']['current_liabilities']
    ncurrentLiabilities = item['company']['non_current_liabilities']
    equity = item['company']['equity']
    ncurrentAssets = item['company']['non_current_assets']
    totalEquityAndLiabilities = equity + ncurrentLiabilities + currentLiabilities
    if item['sector'] == 'technology':
        print "==========================="
        print item['company']['name'] + "'s current liabilities - " + str(currentLiabilities)
        print item['company']['name'] + "'s non-current liabilities - " + str(ncurrentLiabilities)
        print item['company']['name'] + "'s equity - " + str(equity)
        print item['company']['name'] + "'s non-current assets - " + str(ncurrentAssets)
        print item['company']['name'] + "'s total Equity And Liabiliites - " + str(totalEquityAndLiabilities)
