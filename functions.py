print("===== THREE SIMULTANEOUS PYTHON FUNCTIONS =====")
print()
#define functions
#first calculator: Body Mass Index Calculator
def BMI_calculator(weight, height):
    return weight / (height * height)
#second calculator: Rectangle Area Calculator
def area_calculator(length, width):
    return length * width
#third calculator: Celsius to Fahrenheit Converter
def fahrenheit_converter(celsius):
    return (celsius * 9 / 5) + 32

#determine user's calculator choice, collect and store user input for calculation/conversion
option_1 = str("BMI")
option_2 = str("Area")
choice = str(input("What would you like to use (BMI/Area/Fahrenheit): "))
print()
#if BMI, ask user to input
if choice == option_1:
    weight = int(input("Enter the weight: "))
    height = int(input("Enter the height: "))
    print()
    print(f"BMI is", BMI_calculator (weight, height))

#elif Area, ask user to input
elif choice == option_2:
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print()
    print(f"Area is", area_calculator (length, width))

#else (that is Fahrenheit), ask user to input
else:
    celsius = int(input("Enter the temperature in Celsius: "))
    print()
    print(f"Fahrenheit equivalent is", fahrenheit_converter (celsius))