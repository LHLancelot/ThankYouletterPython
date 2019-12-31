# This is a script to automate the writing of a simple thank you letter.
name    = input("Who are you thanking?")
present  = input("Enter the present you received")
usageverb = input("What were you doing with the present e.g. I have enjoyed reading it")
timeperiod = input("Give a time period without the artilce e.g. Month, Week")
action = input("What fun thing have you been doing? e.g. baking, knitting")
reason = input("Why has the present been useful (to the fun thing you have been doing)?")
familygroup = input("Who do you want send your best wishes to e.g. Family, the Thompsons")
sender = input("Your name")

# this is how the letter will look
myletter = "Dear {}, I am writing to thank you for the {}!  I have greatly enjoyed {} with it.  In the past {}, we have been {} and it has been a lot of fun."
myletter2 = "The {} has been very useful, because {}.  We are Looking forward to seeing you soon!"
myletter3 = "Lots of love, and best wishes to the {}"
myletter4 = "{}"
print(myletter.format(name,present,usageverb,timeperiod,action))
print(myletter2.format(present,reason))
print(myletter3.format(familygroup))
print(myletter4.format(name))
