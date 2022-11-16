# While the temperature is greater than 75 degrees Fahrenheit, print "The temperature
# is XX — crank the AC!" and subtract 3 degrees from the temperature.
# Once the temperature is cool enough and the loop is done, print "75. Ahh, that's
# better."

temperature = 90

while temperature > 75:
    print("The temperature is ",temperature, " — crank the AC!")
    temperature = temperature - 3

print("75. Ahh, that's better")
