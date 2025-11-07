#get revenue
revenue = input("wieviel hast du umsatz gemacht?")
try:
    revenue = float(revenue)
except ValueError:
    print("Keine Zahl!")
    
costs = input("Deine Kosten")
try:
    costs = float(costs)
except ValueError:
    print("Gib ne richtige Zahl!")
#calculate profit
profit = revenue - costs
#calc margin
margin = (profit/revenue)*100

if profit < 0:
    print("Bruder du bist broke")

print(f"Revenue: {profit}")
print(f"Margin: {margin}")
