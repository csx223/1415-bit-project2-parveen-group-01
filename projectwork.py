# Added interest receivable data
#prints cost of sales, gross profit, net profit and profit for the period figures.

import urllib2
import json

url = 'http://dev.c0l.in:8888'
api = urllib2.urlopen(url)
data = json.load(api)
 
for item in data:
    if item['sector'] == 'technology':
        print item['sector'], item['company']['name'], item['company']['purchases'], item['company']['interest_payable'], item['company']['sales'], item['company']['expenses'], item['company']['opening_stock'], item['company']['closing_stock'], item['company']['interest_receivable']

cost_of_sales = int(item['company']['opening_stock'] + item['company']['purchases'] - item['company']['closing_stock'])
gross_profit = int(item['company']['sales'] - cost_of_sales )
net_profit = int(gross_profit - item['company']['expenses'])
profit_for_the_period = int(net_profit - item['company']['interest_payable'] + item['company']['interest_receivable'])
                            
print(cost_of_sales)
print(gross_profit)
print(net_profit)
print(profit_for_the_period)                    
                            
                            
