# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
# set1.difference(set2)
#set.intersection()<-- the similarities between sets
both_airlines=our_routes.intersection(competitor_routes)
print(f"Destinations that both airlines fly to:{both_airlines}")

only_our_airline = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline:{only_our_airline}")


neither_airlines =our_routes.symmetric_difference(competitor_routes)
print(f"Destinations neither airline fly to:{neither_airlines}")

# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:

# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome:
# A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

new_customer_ids= set(customer_ids)
print(f"New set of unique customer ID's with no duplicates: {new_customer_ids}")