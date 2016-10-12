
directory = {"Nick":100, "eve":20, "ethan":1555}
def search(name):
    print(directory[name])
def add(name, grade):
    directory[name] = grade
def delete(name):
    del directory[name]
    print(directory)
    
answer = input("what do you want to do? ")
if answer == "search":
   answer = input("who do you want to search for? ")
   search(answer)
    
elif answer == "add":
     anwser1 = input("who do you want to add? ")
     anwser2 = input("what is their grade? ")
     add(anwser1, anwser2)

elif answer == "delete":
     answer = input("who do you want to delete")
     delete(anwser)


else:
    print("function not MEOW") 
                    
        
