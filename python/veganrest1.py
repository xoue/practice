#veganrest1.py

#Create a restuarant that is completely vegan friendly
food = ""
topping = ""
total = 0

print "Welcome to The Vegan Food Bar."
"""
- - - - - - - - - - - - - - - 
Veggie Burger           $5.00
Cheeseless Pizza        $7.50
Milkless Milkshake      $3.25
Fruit Smoothies         $4.00
Bean Burritos           $3.00
Soy Ice Cream           $2.25
- - - - - - - - - - - - - - -\n""")
while food != "done":
    food= raw_input ("What do you wish to buy? <done to exit and checkout>")
    if food.lower() == "veggie burger":
        size = raw_input ("""What size would you like?
        Large       $8.00
        Medium      $6.75
        Small       $5.00\n""")
        if size.lower() == "large":
            total = total + round(8.0 * 0.14 + 8.0,2)
        elif size.lower() == "medium":
            total = total + round(6.75 * 0.14 + 6.75,2)
        elif size.lower() == "small":
            total = total + round(5.0 * 0.14 + 5.0,2)

    elif food.lower() == "cheeseless pizza":
    while topping != "done":
        topping = raw_input ("""What extra topping would you like?
    Green Pepper    $0.50
    Red Pepper      $0.50
    Carrots         $1.50
    Mushrooms       $2.00
    Garlic          $0.25
    Broccili        $2.00\n""")
        if topping.lower() == "green pepper":
            total = total + round((7.5 * 0.14 + 7.5)+ 0.5,2)
        elif topping.lower() == "red pepper":
            total = total + round((7.5 * 0.14 + 7.5)+ 0.5,2)
        elif topping.lower() == "carrots":
            total = total + round((7.5 * 0.14 + 7.5)+ 1.5,2)
        elif topping.lower() == "mushrooms":
            total = total + round((7.5 * 0.14 + 7.5)+ 2.0,2)
        elif topping.lower() == "garlic":
            total = total + round((7.5 * 0.14 + 7.5)+ 0.25,2)
        elif topping.lower() == "broccili":
            total = total + round((7.5 * 0.14 + 7.5)+ 2.0,2)

elif food.lower() == "milkless milkshake":
    total = total + round(3.25 * 0.14 + 3.25,2)

elif food.lower() == "fruit smoothies":
    total = total + round(4.00 * 0.14 + 4.00,2)

elif food.lower() == "falafal":
    total = total + round(0.50 * 0.14 + 0.50,2)

elif food.lower() == "bean burritos":
    total = total + round(3.00 * 0.14 + 3.00,2)

elif food.lower() == "soy ice cream":
    flavour = raw_input ("""What flavour would you like to buy?
Chocolate
Vanilla
Strawberry
Coconut
Pecan
Cookie Crunch\n""")
    total = total round(2.25 * 0.14 + 2.25,2)

else:
    print "Please try again."
    
print "Thanks for coming to the Vegan Food Bar! Your total is ", total, "dollars with tax."
