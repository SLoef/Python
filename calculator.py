# Deze functie telt 2 getallen samen op
def add(x, y):
   return x + y


# Deze functie trekt 2 getallen af
def subtract(x, y):
   return x - y


# Deze functie vermenigvuldig 2 getallen
def multiply(x, y):
   return x * y


# Deze functie deelt 2 getallen
def divide(x, y):
   return x / y


print("Select operation.")
print("1.Plus")
print("2.Min")
print("3.Keer")
print("4.Delen")



# Pak input van de Gebruiker
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Type 1e getal: "))
num2 = int(input("Type 2e getal: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")