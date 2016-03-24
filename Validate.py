# Ensuring that input Value is an integer / numeric

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
        break

# Validating Club entry age

Clubbing_age = inputNumber ("What is your current Age ?    ")

if ( Clubbing_age < 17):
    print ("It would seem you are under age?")
if ( Clubbing_age >= 18 and Clubbing_age <90  ): # Forced to use a range as multiple staments were unneccessarily validated
    print ("Welcome to the Club Ma'am/ Sir!")
if ( Clubbing_age >= 90 ):
    print ("Unfortunately, we are not able to catter for you!")
