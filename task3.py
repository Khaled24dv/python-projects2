
### task 3:
## jop eligibilty portal :
proficient = str(input("is the student proficient in python ? enter (yes or no )"))
experience = int(input("how many years of experience does the student have (enter a number)"))
degree = str(input("does the student have a degree ? enter (yes or no)"))
if (proficient=="yes" and (experience>=2 or degree=="yes")):
    print("congratulations! you have been accepted for the interview")
else :
    print("sorry, you current qualifications do not meet our requirement")
