# If the name contains a "u," print out the name plus "U are so Uniquely U!"
#   Otherwise if the name contains an "i," print out the name plus "I bet you're
#   Impressively Intelligent!"
#   Otherwise if the name contains an "o," print out the name plus "O My! How
#   Original!"
Otherwise, print the name plus "Ehh, a's and e's are so ordinary."

disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula",
"scar", "flotsam", "timon"]

for name in disney_characters:
    if "u" in name:
        print(name + " U are so Uniquely U!")

    elif "i" in name:
        print(name + " I bet you're Impressively Intelligent!")

    elif "o" in name:
        print(name + " O My! How Original!")

    else:
        print(name + " Ehh, a's and e's are so ordinary.")
