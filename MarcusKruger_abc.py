
# This ABC classification model is used to categorize inventory items based on their demand
# It uses the pareto principle to classify these items whereby item classified in A are your most
# valuable items and c is youre least valuable items. This model uses the demand and cost
# for each item to determine the value of each SKU. 
#



#Represent your SKU data
skus = [
 {"sku": "BRK-100", "demand": 2000, "cost": 45},
 {"sku": "GSK-220", "demand": 1500, "cost": 30},
 {"sku": "BLT-010", "demand": 10000, "cost": 2},
 {"sku": "BRG-330", "demand": 800, "cost": 60},
 {"sku": "SEAL-500","demand": 3000, "cost": 5},
 {"sku": "MTR-700", "demand": 50, "cost": 800},
 {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
 {"sku": "CBL-900", "demand": 400, "cost": 25},
]

#Calculate usage value per SKU

def usage_value(demand, cost):
    return demand * cost
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])


 #Sort descending by value

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)


#Calculate cumulative percentage

total_value = sum(item["value"] for item in skus_sorted)
running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100


 #Assign a tier

def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])


#Print the classification report

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])



#Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)

print("--------------------------------------------------")

#Try it myself

skus = [
 {"sku": "BRK-100", "demand": 2000, "cost": 45},
 {"sku": "GSK-220", "demand": 1500, "cost": 30},
 {"sku": "BLT-010", "demand": 10000, "cost": 2},
 {"sku": "BRG-330", "demand": 800, "cost": 60},
 {"sku": "SEAL-500","demand": 3000, "cost": 5},
 {"sku": "MTR-700", "demand": 50, "cost": 800},
 {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
 {"sku": "CBL-900", "demand": 400, "cost": 25},
 {"sku": "NUT-200", "demand": 500000, "cost": 1},
 {"sku": "PIN-300", "demand": 10000, "cost": 10},
]

#Calculate usage value per SKU

def usage_value(demand, cost):
    return demand * cost
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])


 #Sort descending by value

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)


#Calculate cumulative percentage

total_value = sum(item["value"] for item in skus_sorted)
running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100


 #Assign a tier

def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])


#Print the classification report

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])



#Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)



# Try it yourself

# 1) Changing number of SKUs and adding two more, doesnt change the 
#    tier counts, but it does change the cumulative percentages and values 
#    of each SKU. The new SKUs added are "NUT-200" and "PIN-300",
#    they affect the overall distribution of value among the SKUs. So basically
#    the tier counts remain the same however the type of SKUs in each tier may change.

# 2) Changing the tier thresholds to 70% for A, 90% for B, and 100% for C, results in a 
#    different distribution of SKUs across the tiers. The number of SKUs in each tier 
#    changes, as some SKUs that were previously classified as A may now fall into B or C.
#    Therefore there is now more SKUs in tier B and C compared to A, which has fewer SKUs.
#    Making the threshold for A lower.

# 3) 
print("--------------------------------------------------")


def classify_inventory(skus):
    # Calculate usage value per SKU
    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])

    # Sort descending by value
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

    # Calculate cumulative percentage
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

    # Assign a tier
    for item in skus_sorted:
        item["tier"] = assign_tier(item["cum_pct"])


    return skus_sorted


for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"])

tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)
