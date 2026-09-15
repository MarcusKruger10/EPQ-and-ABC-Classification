# This model is used to calculate the optimal EPQ (economic production quantity).
#  It takes into account the annual demand, setup cost, holding cost, daily demand rate,
#  and daily production rate to determine the optimal production quantity that
#  minimizes total costs. It optomizes the production runs per year, length of each run,
#  and maximum inventory level. This is done becuase holding cost is the most difficult to
#  calculate and is also very expensive for the business.
#



import math


#Define your inputs

annual_demand = 12000 # units per year
setup_cost = 50 # cost per production run, in Rand
holding_cost = 2 # cost per unit per year, in Rand
daily_demand_rate = 40 # units produced/sold per day
daily_production_rate = 100 # units your process can make per day

# Write the EPQ function

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
epq = calculate_epq(annual_demand, setup_cost, holding_cost,
 daily_demand_rate, daily_production_rate)
print("Optimal production quantity:", round(epq, 2))


#Calculate production runs per year and run length

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))


#Calculate maximum inventory level

max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))


print("--------------------------------------------------")

#Put it all together
import math
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
annual_demand = 12000
setup_cost = 50
holding_cost = 2
daily_demand_rate = 40
daily_production_rate = 100000

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
 daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))


print("--------------------------------------------------")


# EOQ model
import math
def calculate_eoq(demand, order_cost, hold_cost):
    return math.sqrt((2 * demand * order_cost) / hold_cost)
def total_annual_cost(demand, order_cost, hold_cost, order_qty):
    ordering = (demand / order_qty) * order_cost
    holding = (order_qty / 2) * hold_cost
    return ordering + holding

annual_demand = 12000
ordering_cost = 50
holding_cost = 2

eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)
orders_per_year = annual_demand / eoq
days_between_orders = 365 / orders_per_year
cost_at_eoq = total_annual_cost(annual_demand, ordering_cost, holding_cost, eoq)

print("Optimal order quantity:", round(eoq, 2))
print("Orders per year:", round(orders_per_year, 2))
print("Days between orders:", round(days_between_orders, 1))
print("Total annual cost at EOQ:", round(cost_at_eoq, 2))



# Try it yourself 
# 1) The EPQ decreases as the daily production rate increases. 
#    This is because a higher production rate allows for more units to be produced
#    in a shorter amount of time, reducing the need for larger production runs.

# 2) EOQ assumes that the entire batch arrives instantaeously, whereas the EPQ 
#    model assumes that the batch is produced over time. This means that the EPQ
#    model takes into account the production rate and the demand rate, while the EOQ    
#    model does not. Therefore, (1 - d/p) is included in the EPQ formula to account
#    for the consumption of inventory during the production process. And therefore if
#    p is much larger than d, the EPQ will be closer to the EOQ. So if you can produce the 
#    entire batch almost instantly the demand wont draw down the inventory in a noticable way.