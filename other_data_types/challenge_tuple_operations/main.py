# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
#Count the number of apples.
apple_count = shelf.count("apples")
print ("Number of Apples:", apple_count)
#Find the index of bananas
banana_index = shelf.index("bananas")
print ("First Banana Index:", banana_index)
#Checking if the numbers of apples are less than 5.
if apple_count < 5:
    print ("Apples need to be restocked.")
else:
    print ("Apples are sufficiently stocked")
#checking if grapes are in the shelf tuple.
grape_count = shelf.count ("grapes")
if grape_count == 1:
    print ("Grapes need to be restocked.")
else:
    print ("Grapes are sufficiently stocked.")
#checking if oranges are in shelf.
if "oranges" in shelf:
    oranges_index = shelf.index ("oranges")
    print ("Oranges are at index:", oranges_index)
else:
    print ("Oranges are out of stock.")

