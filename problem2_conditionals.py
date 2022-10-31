angry = True
bored = True
hungry = False
tired = False
# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
if angry==True and hungry==True and bored==True:
    print("he will eat the Triceratops!")

# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
elif tired==True and hungry==True:
    print("he will eat the Iguanadon")

# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
elif tired==True and bored==True:
    print("he will ear the Stegasaurus")

# Otherwise if T-Rex is tired, he goes to sleep.
elif tired==True:
    print("he goes to sleep")

 # Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
elif angry==True and bored==True:
    print("he will fight witht he Velociraptor")

# Otherwise if T-Rex is angry or bored, he roars.
elif angry==True or bored==True:
    print("he roars")

# Otherwise T-Rex gives a toothy smile.
else:
    print("T-rex gives a toothy smile")
