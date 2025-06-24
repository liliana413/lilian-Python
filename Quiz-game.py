print("welcome to my computer quiz")

playing = input("Do you want to play? ")

print("playing:", playing)
if playing.lower() != "yes":
    quit()

print ("okay! let's play :)")
score = 0

answer = input("what does GPU stand for? ")
print("answer:", answer)
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("what does RAM stand for? ")
print("answer:", answer)
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

print("You got " + str(score) + " questions correct out of 4.")
