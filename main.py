students = {"Steve": 84 , "John" : 54 , "louis" : 58 , "jordan" : 79 , "nathan" : 97}
print(students)
average  = students.get("Steve") + students.get("John") + students.get("louis") + students.get("jordan") + students.get("nathan") / 5
print("average score" , average)

highest = students.get("nathan")
lowest = students.get("John")

print("the lowest and highest scores are:", highest , "the highest score" , lowest , "and the lowest score")

pick = input("would you like to chose someone from")

pick = students.get("students","unknown")
print(pick)