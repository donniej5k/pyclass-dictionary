import copy

# Given weekly sales data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# Create a deep copy of weekly_sales
copied_sales = copy.deepcopy(weekly_sales)

# Update the sales figure for "Electronics" in "Week 2" in the copied data
copied_sales["Week 2"]["Electronics"] = 18000

# Print the original and copied sales data to verify the changes
print("Original Sales Data:")
for week, sales in weekly_sales.items():
    print(f"{week}: {sales}")

print("\nCopied Sales Data with Updated Electronics Sales in Week 2:")
for week, sales in copied_sales.items():
    print(f"{week}: {sales}")
