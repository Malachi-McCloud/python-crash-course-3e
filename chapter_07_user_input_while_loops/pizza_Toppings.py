# Pizza Toppings Exercise 7-4

# Write a loop that prompts a user for pizza toppings as they enter each topping a message go until they type quit

prompt = "\nPlease enter your next Pizza Topping."
prompt += "\n(Enter 'quit' when you are finished adding toppings.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I would loove to go for {topping} pizza!")

# Finishing Chapter 7 Here