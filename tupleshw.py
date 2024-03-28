# The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:

def formated_itinerary(itineraries):
    formated_itineraries=""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination=itinerary
        formated_itinerary= f"Itinerary {i}: {traveler_name} - from {origin} to{destination}"
        formated_itineraries += formated_itinerary
    return formated_itineraries


# 2. 
# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

def add_book(library):
    title=input("Enter the title of the new book: ")
    author=input("Enter the aurthor of the new book: ")
    new_book= (title,author)
    if new_book in library:
        print("This book already exsists in the library.")
    else:
        print("This book has been successfully added to the library.")

