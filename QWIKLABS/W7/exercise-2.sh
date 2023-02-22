# Exercise - 2
# Now, use the Python interactive shell to create a dictionary.
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

# Call the sorted function to sort the items in the dictionary.
sorted(fruit.items())

# Output:
# [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

# We'll now sort the dictionary using the item's key. For this use the operator module.

# Pass the function itemgetter() as an argument to the sorted() function. Since the second element of tuple needs to be sorted, pass the argument 0 to the itemgetter function of the operator module.
import operator
sorted(fruit.items(), key=operator.itemgetter(0))

# Output:
# [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

# To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module.
sorted(fruit.items(), key=operator.itemgetter(1))

# Output:
# [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

# Finally, you can also reverse the order of the sort using the reverse parameter. This parameter takes in a boolean argument.

# To sort the fruit object from most to least occurrence, we pass the argument reverse=True.
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)

# Output:
# [('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]

# You can see the fruit object is now sorted from the most to the least number of occurrences.
# Great job practice these skills! You can further practice this by sorting the logs that you would fetch using regular expressions from the previous section.

# Exit the shell using exit().