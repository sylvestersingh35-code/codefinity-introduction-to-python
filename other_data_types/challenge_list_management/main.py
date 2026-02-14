#Initialize Lists:
meat =["Ham" , 3.99 , 50 , "Sliced"]
cheese =["Cheddar" , 5.49 , 100 , "Sharp"] 
condiment =["Mustard" , 1.99 , 75 , "Spicy"]
deli_dept =[meat , cheese , condiment]
#Print Initial Lists.
print("Initial Deli List:" , deli_dept)
#restock item in the meat list.
if meat[2] <100: meat[2] = 100
#Adding seasonal meat to the main deli_dept list.
seasonal_meat =["Turkey" , 4.50 , 100 , "Sliced"]
deli_dept.append(seasonal_meat)
#Removing condiment from th deli_dept
deli_dept.remove(condiment)
#Sorting the list.
deli_dept.sort()
#Printing the updated list after all changes.
print("Updated Deli List:" , deli_dept)
