import urllib2
import json

urlIncomeStatement = 'http://dev.c0l.in:8888'
apiIncomeStatement = urllib2.urlopen(urlIncomeStatement)
dataIncomeStatement = json.load(apiIncomeStatement)

urlFinancialPosition = 'http://dev.c0l.in:9999'
apiFinancialPosition = urllib2.urlopen(urlFinancialPosition)
dataFinancialPositiont = json.load(apiFinancialPosition)

for item in dataIncomeStatement:
    if item['sector'] == 'technology':
        print '""""""""""""""""""""""""""""""""""""""""""""""""'
        print item['company']['name']+ "'s interest payable - " + str(item['company']['interest_payable'])
        print item['company']['name']+ "'s interest receivable - " + str(item['company']['interest_receivable'])
        print item['company']['name']+ "'s sales - " + str(item['company']['sales'])
        print item['company']['name']+ "'s expenses - " + str(item['company']['expenses'])
        print item['company']['name']+ "'s opening stock - " + str(item['company']['opening_stock'])
        print item['company']['name']+ "'s closing stock - " + str(item['company']['closing_stock'])
        print '""""""""""""""""""""""""""""""""""""""""""""""""'

for item in dataFinancialPositiont:
    if item['sector'] == 'technology':
        print '""""""""""""""""""""""""""""""""""""""""""""""""'
        print item['company']['name']+ "'s current liabilities - " + str(item['company']['current_liabilities'])
        print item['company']['name']+ "'s non-current liabilities - " + str(item['company']['non_current_liabilities'])
        print item['company']['name']+ "'s equity - " + str(item['company']['equity'])
        print item['company']['name']+ "'s non-current assets - " + str(item['company']['non_current_assets'])
        print '""""""""""""""""""""""""""""""""""""""""""""""""'

purchases = float(item['company']['closing_stock'] in dataIncomeStatement) - float(str(item['company']['opening_stock']) in dataIncomeStatement) + costOfSales
costOfSales = float(str(item['company']['opening_stock']) in dataIncomeStatement) + float(purchases) - float(str(item['company']['closing_stock']) in dataIncomeStatement)
grossProfit = float(str(item['company']['sales']) in dataIncomeStatement) - float(costOfSales)

print purchases
