# Adventure Game andrea_young

print("Last night, you went to sleep and dreamt you were somewhere dark, like a cave.")
print("Now, you wake up to find you are actually in a genie bottle.")
print("He will release you from the bottle if you find a gem he has hidden somewhere.") 
print ("Inside the genie bottle you see:")
# The menu function:
def menu(list, question):
  for item in list:
    print(1 + list.index(item), item)
  return int(input(question))

# This is a list of the things you can see:
items = ["pool of water", "stalagtite", "rug", "jar of incense", "an empty shoe", "a satchel", "an envelope"]

import random
gemlocation = random.randint(1,5)
#The key is not found:
gemfound = "no"
loop = 1

#Display the menu until the key is found:
while loop == 1:
  choice = menu(items, "What do you want to inspect?") 
  print("")
  if choice < 7: 
    if choice == gemlocation:
       print("You found a gem in the", items[choice -1])
       gemfound = "Yes"
    else:
       print("You found nothing in the", items [choice -1])
  elif choice == 7:
     if gemfound == "Yes":
         loop = 0
         print("You found a bright sparkly gem!")
     else:
        print("This is piece of coal. It's not a gem. Keep looking.")
  else:
     print("Choose a number less than 8.")
print("You wake up and the genie has released you. Will he give you three wishes now?.")
        
