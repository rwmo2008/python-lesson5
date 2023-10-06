#Print table of Celsius temp. + Fahrenheit temp.

def convert_to_fahrenheit(celsius):
    celsius = 9.0/5.0 * celsius + 32
    return celsius

print("0 Celsius   = 32  Fahrenheit")
print("10 Celsius  = 50  Fahrenheit")
print("20 Celsius  = 68  Fahrenheit")
print("30 Celsius  = 86  Fahrenheit")
print("40 Celsius  = 104 Fahrenheit")
print("50 Celsius  = 122 Fahrenheit")
print("60 Celsius  = 140 Fahrenheit")
print("70 Celsius  = 158 Fahrenheit")
print("80 Celsius  = 176 Fahrenheit")
print("90 Celsius  = 194 Fahrenheit")
print("100 Celsius = 212 Fahrenheit")

print()

celsius = 0
for i in range(0, 101, 10):
    print("Temperature in Celsius:", celsius)
    print("Temperature in Fahrenheit:", convert_to_fahrenheit(celsius))
    celsius = celsius + 10




