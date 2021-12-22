#unit 1 challanger 3 Temprature Conversion App
print("Welcome to the Temprature Conversion App/n")

#Get Imperial Temprature
fahrenheit = float(input("What is the given temprature in degrees fahrenheit: "))

#Convert and output
celcius = round((fahrenheit - 32) * 5.0 / 9, 2)
kelvin = round((fahrenheit - 32) * 5.0 / 9 + 273.15, 2)

print(f"Degrees Fahrenheit:    {fahrenheit}")
print(f"Degrees Celcius:       {celcius}")
print(f"Degrees Kelvin:        {kelvin}")
