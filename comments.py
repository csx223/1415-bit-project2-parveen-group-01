#liabries that are being used
import json
import csv

c = csv.writer(open("analysis output.csv", "wb")) #"wb" makes file writable, also opens analysis output csv

urlIncomeStatement = 'http://dev.c0l.in:8888' #the API URL for the income statement
apiIncomeStatement = urllib2.urlopen(urlIncomeStatement) #opens and then proceeds to extract it
dataIncomeStatement = json.load(apiIncomeStatement) #json will then format the extracted data
@@ -21,21 +23,20 @@ for item in dataIncomeStatement:
    profit_for_the_period = int(net_profit - item['company']['interest_payable'] + item['company']['interest_receivable'])

    if item['sector'] == 'technology': #if the following items are in the technology sector, print the following results
        print "------------------------------------------"
        print str(item['sector']), name + ":"
        print name + "'s interest purchases - " + str(item['company']['purchases']) #prints purchases of certain company
        print name + "'s interest payable - " + str(item['company']['interest_payable']) #prints interest of certain company
        print name + "'s interest sales - " + str(item['company']['sales']) #prints sales of certain company
        print name + "'s interest expenses - " + str(item['company']['expenses']) #prints expenses of certain company
        print name + "'s interest opening stock - " + str(item['company']['opening_stock']) #prints opening stock of certain company
        print name + "'s interest closing stock - " + str(item['company']['closing_stock']) #prints closing stock of certain company
        print name + "'s interest interest recivables - " + str(item['company']['interest_receivable']) #prints interst recivables of certain company                  
        print name + "'s interest cost of sales - " + str 