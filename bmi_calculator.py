try:
    # Taking user input
    Height = float(input("Please enter your height in CM: "))
    Weight = float(input("Please enter your weight in KG: "))
except ValueError:
    # Validation error.
    print("Please provide valid input.")

else:
    if Height <= 0 or Weight <= 0:
        print("Your input must not be zero or less.")
    else:
        # Calculate BMI
        hm= (Height/100) * (Height/100)
        BMIIndex = round(Weight / hm)

        # Print the output
        print("Your Body Mass Index is: ", BMIIndex)

        if BMIIndex < 18.5:
            print("Underweight.")
        elif BMIIndex >= 18.5 and  BMIIndex<= 25:
            print("Normal.")
        elif BMIIndex > 25 and  BMIIndex<= 30:
            print("Overweight")
        elif BMIIndex > 30 and  BMIIndex<= 35:
            print("Moderate obesity")
        elif BMIIndex > 35 and  BMIIndex<= 40:
            print("Severe obesity")
        elif BMIIndex < 40:
            print("Morbid obesity.")