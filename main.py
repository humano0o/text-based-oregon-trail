import random
import time
import math

# Setting important global variables

day = 0
distanceTraveled = 0
money = 150
food = 300
bullets = 10
healthTotal = 10
health = healthTotal

dysentery = False

# Helper function, decrements health

def healthRemove():
    global health
    health -= 1

# Helper function, randomly rolls for a chance that a catastrophe occurs, chance increases with each passing day 

def catastrophe():
  global food
  chanceFoodLoss = random.random()
  if chanceFoodLoss < math.log(day*0.01, 10000):
      foodlost = 0
      if food > 50:
          foodLost = 20
      elif food <= 50:
          foodLost = round(food * 0.2)
      food -= foodLost
      catastrophes = ["A wild animal rummaged through your food supplies.\n"
                      f"You've lost {foodLost} food.", 
                      "A wildfire came through and miraculously, you surived. Not all your food did though.\n"
                      f"You've lost {foodLost} food.",
                      "Bandits picked you clean last night.\n"
                      f"You've lost {foodLost} food."]
      print(random.choice(catastrophes))

# Called every day, used to perform actions that must occur every new day

def dayCheck():
  global food, dysentery
  if day == 10:
      print("Welcome to Wiltshire! You're in town today. You can access it by saying \"town.\"\n")
  elif day == 20:
      print("Welcome to Chandler! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 30:
      print("Welcome to Hoxington! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 40:
      print("Welcome to Lowville! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 50:
      print("Welcome to Arlington! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 60:
      print("Welcome to White Bridge! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 70:
      print("Welcome to Haling Cove! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 80:
      print("Welcome to Bryxton Town! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 90:
      print("Welcome to Franklin! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 100:
      print("Welcome to Dover! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 110:
      print("Welcome to Rochester! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 120:
      print("Welcome to Oakland! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 130:
      print("Welcome to Milton! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 140:
      print("Welcome to Springfield! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 150:
      print("Welcome to Georgetown! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 160:
      print("Welcome to Hudson! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 170:
      print("Welcome to Lexington! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 180:
      print("Welcome to Cleveland! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 190:
      print("Welcome to Kingston! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day % 10 != 0:
      catastrophe()
  if day % 10 != 0:
      print()
  x = random.random()
  if x < math.log(day*0.2, 100000000000) and dysentery == False:
      dysentery = True
      print(f"You have dysentery. Rest for a day to get rid of it. You've lost one health. You have {health} health remaining.\n")
      healthRemove()
  elif dysentery == True:
      healthRemove()
      print(f"You have dysentery. Rest for a day to get rid of it. You've lost one health. You have {health} health remaining.\n")
  if food <= 0:
      food = 0
      healthRemove()
      print("You have run out of food. You've lost one health.\n")
  print("--------------------\n")

# Same as previous function, but dysentery has no chance of being assigned to true
    
def dayCheckNoDysentery():
  global food
  if day == 10:
      print("Welcome to Wiltshire! You're in town today. You can access it by saying \"town.\"\n")
  elif day == 20:
      print("Welcome to Chandler! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 30:
      print("Welcome to Hoxington! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 40:
      print("Welcome to Lowville! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 50:
      print("Welcome to Arlington! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 60:
      print("Welcome to White Bridge! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 70:
      print("Welcome to Haling Cove! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 80:
      print("Welcome to Bryxton Town! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 90:
      print("Welcome to Franklin! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 100:
      print("Welcome to Dover! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 110:
      print("Welcome to Rochester! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 120:
      print("Welcome to Oakland! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 130:
      print("Welcome to Milton! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 140:
      print("Welcome to Springfield! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 150:
      print("Welcome to Georgetown! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 160:
      print("Welcome to Hudson! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 170:
      print("Welcome to Lexington! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 180:
      print("Welcome to Cleveland! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day == 190:
      print("Welcome to Kingston! You're in town today. You can access the shop by saying \"town.\"\n")
  elif day % 10 != 0:
      catastrophe()
  if day % 10 != 0:
      print()
  if food <= 0:
    food = 0
    healthRemove()
    print("You have run out of food. You've lost one health.\n")
  print("--------------------\n")

# Called to increment day and decrement food by 5, calls dayCheck() 
    
def dayMove():
    global day, food
    time.sleep(0)
    food -= 5
    day += 1
    print(f"It's been {day} days. You have {200-day} days left until winter.")
    dayCheck()

# Same as previous, but calls dayCheckNoDysentery(), dysentery has no chance of being assigned

def dayMoveNoDysentery():
    global day, food
    time.sleep(0)
    food -= 5
    day += 1
    print(f"It's been {day} days. You have {200-day} days left until winter.")
    dayCheckNoDysentery()

# Prints stats of current game session

def status():
    print(# f"\nDays: {day}\n"
          f"\nDays Left: {200 - day}\n"
          # f"Distance Traveled: {distanceTraveled} miles\n"
          f"Distance left: {2000 - distanceTraveled}\n"
          f"Food: {food}\n"
          f"Bullets: {bullets}\n"
          f"Money: ${money}\n"
          f"Health: {health}\n")
    if dysentery == True:
        print("You have dysentery\n")

# Prints commands that the player can execute

def help():
    print("\nStatus: Prints stats.\n"
          "Help: Prints this menu.\n"
          "Hunt: Hunts animals, gives a random amount of food, costs 1 bullet.\n"
          "Town: Enters town, only works every 10 days.\n"
          "Rest: Health increases by one, gets rid of dysentery, one day passes.\n"
          "Travel: Move a random number of miles.\n")

# Uses 1 bullet each time, returns random amount of food depending on how the player rolls 

def hunt():
    # Average food per hunt is 13.5
    global food
    huntChance = random.randint(1, 100)
    print("\nGoing on a hunt.")
    time.sleep(1)
    if huntChance > 90:
        huntFood = random.randint(40, 50)
        print(f"The hunt was extremely well! You got {huntFood} food.")
        food += huntFood
    elif huntChance < 21:
        print("The hunt was unsuccessful. You did not get any food.")
    elif huntChance < 26:
        huntFood = random.randint(10, 20)
        print(f"The hunt was catastrophic. You lost {huntFood} food.")
        food -= huntFood
    else:
        huntFood = random.randint(10, 20)
        print(f"The hunt was successful. You got {huntFood} food.")
        food += huntFood
    dayMove()

# Player rests, passing 1 day, healing one health or getting rid of dysentery

def rest():
    global health, day, dysentery, food
    if dysentery:
        food -= 5
        x = random.randint(1,3)
        if x == 2 or x == 3:
            dysentery = False
            print("\nYou no longer have dysentery.\n")
            dayMoveNoDysentery()
        if x == 1:
            print("\nYou still have dysentery.\n")
            dayMove()
    elif health < healthTotal:
        print("\nYou have rested, a day has gone by and health has gone up by one.\n")
        health = health + 1
        food -= 5
        dayMove()
    elif health == healthTotal:
        print("\nYour health is already full\n")

# Player travels an average of 15 miles towards oregon

def travel():
    # Average distance traveled per day is 15
    global day, distanceTraveled
    x = random.randint(10,30)
    distanceTraveled = distanceTraveled + x
    print(f"\nYou traveled {x} miles today. You've traveled a total of {distanceTraveled} miles.")
    dayMove()

# Defines functions of a town, including hospital and store

def town():
    global bullets, dysenteryCost, food, health, money, dysentery
    priceFood = random.randint(10, 15)
    priceBullet = random.randint(10, 15)
    if day == 200:
        print("\nThere is no town here.\n")
    elif day % 10 != 0:
        print("\nYou can only access a town every 10 days.\n")
        return
    elif day % 10 == 0 and day != 200:
        j = input("\nWelcome to town! Type help to see options.\n\n").lower()
        while j != "leave":
            if j == "help":
                print("\nType shop to access shop.\n"
                      "Type hospital to heal your health. $20 per health.\n"
                      "Type leave to leave town.\n")
            elif j == "shop":
                print(f"\nPurchase options:\n"
                      f"5 Food for ${priceFood}\n"
                      f"1 Bullet for ${priceBullet}\n")
                k = input("What would you like to buy? Type leave to return.\n\n").lower()
                while True:
                    if k == "leave":
                        print("\nYou've left the shop.\n")
                        break
                    if k == "food":
                        if money >= priceFood:
                            food += 5
                            money -= priceFood
                            print(f"\nYou've bought 5 food for ${priceFood}. You have ${money} left.")
                        elif money < priceFood:
                            print("You don't have enough money for that.")
                    if k == "bullet":
                        if money >= priceBullet:
                            bullets += 1
                            money -= priceBullet
                            print(f"\nYou've bought 1 bullet for ${priceBullet}. You have ${money} left.")
                        elif money < priceBullet:
                            print("\nYou don't have aenough money for that.")
                    if k == "status":
                        status()
                    print("\nEnter 'food', 'bullet', or 'leave'\n")
                    k = input().lower()
            elif j == "hospital":
                if dysentery:
                    dysenteryCost = 10
                else:
                    dysenteryCost = 0
                if health == 5:
                    print("\nYou have full health already.\n")
                else:
                    print(f"\nYou have {health} health. Would you like to fill your\n"
                          f"health for ${10*(5 - health) + dysenteryCost}? Yes or no.\n")
                    p = input().lower()
                    while True:
                        if p == "yes" and money >= (10*(healthTotal - health) + dysenteryCost):
                            health = 5
                            money = money - 10*(healthTotal - health)
                            dysentery = False
                            print(f"\nHealth filled. You have ${money} left. Leaving the hospital.\n")
                            break
                        elif p == "yes" and money < (10*(healthTotal - health) + dysenteryCost):
                            print("\nYou don't have enough money for that. Leaving the hospital.\n")
                            break
                        elif p == "no":
                            print("\nLeaving the hospital.\n")
                            break
                        else:
                            print("\nSay 'yes', 'no', or 'leave'\n")
            elif j == "status":
                status()
            else:
                print("\nType help to see options.\n")
            j = input()
        print("\nYou've left town. Type town to go back in or move on.\n")


print("\nWelcome to the Oregon Trail, you have 200 days to accomplish a"
      " 2000 miles trek\nacross the country. Type help for help. Good luck.\n"
      "At the moment, you're in town. You can buy provisions.\n")

# Main game loop

global i
while day < 200 and distanceTraveled <= 2000 and health > 0:
    global i
    i = input("").lower()
    if i == "quit":
        break
    elif i == "status":
        status()
    elif i == "help":
        help()
    elif i == "rest":
        rest()
    elif i == "travel":
        travel()
    elif i == "town":
        town()
    elif i == "hunt":
        hunt()
    else:
        print("\nType help to see options.\n")

# Win/lose conditions

if i == "quit":
    print("You quit!")
elif day >= 200:
    print("You lost! Winter arrived and you died.")
elif health < 1:
    print("You lost! You ran out of health and died.")
else:
    print("Good game! You made it to Oregon.")

