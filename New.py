person = input("Enter Your Name? ")
age = input("How Old Are You? ")

if age > "18":
    print("Hello", person, "You are authorised to purchase alcohol today!")

if age < "18":
    print("Hello", person, "I am afraid you are not authorised to purchase alcohol today.")