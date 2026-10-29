
# Amarie Rivera
# answer 10 questions to find out your spirit animal


# functions used in the quiz
def get_answer(question_number):
    # ask for an answer and check that it is one of the choices
    answer = input("Enter A, B, C, or D: ").strip().upper()
    # ask again if they type something other than A, B, C, or D
    while answer not in ("A", "B", "C", "D"):
        print("Invalid answer for question", question_number)
        answer = input("Please enter A, B, C, or D: ").strip().upper()
    return answer


def show_result(player_name, animal):
    # elephant and owl sound better with an instead of a
    if animal == "Elephant" or animal == "Owl":
        article = "an"
    else:
        article = "a"
    print(player_name + " Your spirit animal is " + article + " " + animal + "!")


def start_quiz(player_name):
    # show a different message if no name was entered
    if player_name != "" and player_name.strip() != "":
        print("Good luck,", player_name + "!")
    else:
        print("Good luck, player!")
    # countdown before the first question
    for number in range(3, 0, -1):
        print("Starting in", number)


def show_score_message(points):
    # show how many points the matching animal got
    if points > 0:
        print("You earned", points, "points toward your result!")
    # a little extra message depending on the score
    if points >= 6:
        print("This animal was a strong match!")
    elif points >= 3:
        print("This animal matched several of your answers.")


#welcome message 
print("Welcome", end=" ")
print("to the spirit animal quiz!")
print("Find out what spirit animal you are!")
# using * to find out number of answer choices
print("This quiz contains", 10*4 ,"possible answer choices!")
# using division to show one out of eight animal types
print("One animal represents ", 1/8 , " of the eight possible animal types")
print("This quiz can be divided into" , 10//3, "complete groups of 3 questions",
      "There would be", 10%3, " question left over")
#number of animals that you could get one from using 2 to the power of three
2 ** 3
# some animals need to be repeated or only used once per question to make the scoring as even as possible since 10 questions - 8 animals doesnt equal each other
10 - 8 

name = input ("What's your name?")
start_quiz(name)

# start each animal with zero points
capybara_score = 0 
bunny_score = 0
elephant_score = 0 
owl_score = 0 
bear_score = 0 
hyrax_score = 0 
kitty_score = 0 
hedgehog_score = 0 


#question 1
print("Question 1: What's your favorite hobby?", 
      "A. Going outside, exploring, enjoying nature", 
      "B. Drawing, crafting, being creative",
      "C. Focusing on academics/getting ahead in your classes or learning something new", 
      "D. Hanging out with friends doing absolute nonsense", 
      sep="\n")

#question 1 scoring
answer_1 = get_answer(1)
if answer_1 == "A":
    capybara_score += 1
    kitty_score += 1

elif  answer_1 == "B" : 
    bunny_score += 1 
    hedgehog_score += 1

elif answer_1 == "C" : 
    owl_score += 1
    elephant_score += 1

else: # Question 1: all other answers have been validated as D 
    hyrax_score += 1 
    kitty_score += 1 

print("-" * 30)
#question 2 
print("Question 2: Which snack sounds the best?", 
      "A. Fruits or something sweet", 
      "B. Snack plate with a little bit of everything", 
      "C. Eating all you can until it's gone", 
      "D. Whatever snack is closest to me",
      sep="\n")

#question 2 scoring 
answer_2 = get_answer(2)
if answer_2 == "A" : 
    bunny_score += 1 
    elephant_score += 1 
elif answer_2 == "B" : 
    kitty_score += 1
    hyrax_score += 1 
elif answer_2 == "C" : 
    capybara_score += 1 
    bear_score += 1 
elif answer_2 == "D" : 
    hedgehog_score += 1 
    kitty_score += 1 

#string making a divider between questions
print("-" * 30)

#question 3 
print("Question 3: You just got invited to a party. What's the game plan?",
      "A. I regret accepting this invitation", 
      "B. YES, I'LL SEE EVERYONE THERE", 
      "C. I'll go but find somewhere comfortable to just vibe",
      "D. I'll mostly hangout with the people i already know",
      sep="\n" )

#question 3 scoring 
answer_3 = get_answer(3)
if answer_3 == "A" : 
    owl_score += 1 
    hedgehog_score += 1 
elif answer_3 == "B" : 
    hyrax_score += 1 
    kitty_score += 1 
elif answer_3 == "C" :
    capybara_score += 1 
    elephant_score += 1 
elif answer_3 == "D" :
    elephant_score += 1 
    bunny_score += 1 

print("-" * 30)

#question 4 
print("Question 4: Your plans suddenly change. What do you do?",
      "A. okay. whatever works.", 
      "B. WHO changed the plan???",
      "C. New plan? even better!",
      "D. That's fine...but i already planned everything", 
      sep="\n")

#question 4 scoring 
answer_4 = get_answer(4)
if answer_4 == "A" : 
    capybara_score += 1 
    bunny_score += 1 
elif answer_4 == "B" :
    owl_score += 1 
    hedgehog_score += 1 
elif answer_4 == "C" : 
    hyrax_score += 1 
    kitty_score += 1 
elif answer_4 == "D" :
    bear_score += 1 
    elephant_score += 1 

print("-" * 30)

# question 5 
print("Question 5: What's your ideal way to relax?",
      "A. Blanket + snacks + favorite show", 
      "B. Absolutely nothing. i would like to become one with the couch.",
      "C. Whatever random thing i feel like doing now",
      "D. Reading, watching something interesting, or learning something new",
      sep="\n")

# question 5 scoring
answer_5 = get_answer(5)
if answer_5 == "A" :
    bunny_score += 1 
    hedgehog_score += 1
elif answer_5 == "B" : 
    capybara_score += 1 
    bear_score += 1 
elif answer_5 == "C" :
    kitty_score += 1 
    hyrax_score += 1
elif answer_5 == "D" : 
    owl_score += 1 
    elephant_score += 1 

print("-" * 30)

#question 6 
print("Question 6: Someone just cut in front of you in line! What do you do?",
      "A. Whatever. I'm not fighting over a sandwich", 
      "B. Stares at them until they realize what they've done", 
      "C. Speak up and let them know where the line starts",
      "D. I say nothing...but they've made a powerful enemy",
      sep="\n")

#question 6 scoring 
answer_6 = get_answer(6)
if answer_6 == "A" : 
    capybara_score += 1
    hedgehog_score += 1 
elif answer_6 == "B" : 
    kitty_score += 1 
    bear_score += 1
elif answer_6 == "C" :
    bunny_score += 1 
    elephant_score += 1 
elif answer_6 == "D" :
    bear_score += 1 
    
print("-" * 30)

#question 7
print("Question 7: How do you recharge after a long, stressful day?",
      "A. Close the door. Turn off my phone; i am no longer available",
     "B. Blanket, snack, show, repeat.",
     "C. Go outside and clear my head.",
     "D. Immediately call/text someone because you must tell them what happened", 
     sep="\n")

#question 7 scoring
answer_7 = get_answer(7)
if answer_7 == "A" : 
    owl_score += 1 
    hedgehog_score += 1
elif answer_7 == "B" :
    bunny_score += 1 
    capybara_score += 1
elif answer_7 == "C" :
    capybara_score += 1
    elephant_score += 1
elif answer_7 == "D" :
    hyrax_score += 1
    kitty_score += 1

print("-" * 30)

#question 8 
print("Question 8: Where would you want to live?",
      "A. A tiny cozy cottage in the woods",
      "B. Somewhere warm near the water",
      "C. A fun apartment in the middle of everything",
      "D. A quiet home somewhere peaceful and far away",
      sep="\n")

#question 8 scoring 
answer_8 = get_answer(8)
if answer_8 == "A" : 
    bunny_score += 1
    hedgehog_score += 1
elif answer_8 == "B" :
    capybara_score += 1
    elephant_score += 1 
elif answer_8 == "C" :
    kitty_score += 1 
    hyrax_score += 1
elif answer_8 == "D" :
    owl_score += 1 
    bear_score += 1 
    
print("-" * 30)

#question 9 
print("Question 9: What special skill would you want?",
      "A. Know basically everything",
      "B. Become insanely talented at art",
      "C. Make friends with absolutely anyone",
      "D. Fall asleep anywhere, anytime",
      sep="\n")

#question 9 scoring 
answer_9 = get_answer(9)
if answer_9 == "A" : 
    owl_score += 1 
    elephant_score += 1
elif answer_9 == "B" : 
    bunny_score += 1
    kitty_score += 1
elif answer_9 == "C" :
    hyrax_score += 1 
    elephant_score += 1
elif answer_9 == "D" :
    capybara_score += 1 
    hedgehog_score += 1 

print("-" * 30)
    
#question 10
print("Question 10: Pick your favorite weather",
      "A. Rainy and cozy, blanket weather",
      "B. Warm and sunny! I want to be OUTSIDE",
      "C. Cloudy, cool, and peaceful",
      "D. Warm but not too hot. Perfect weather for doing anything",
      sep="\n")

#question 10 scoring
answer_10 = get_answer(10)
if answer_10 == "A" :
    bunny_score += 1
    hedgehog_score += 1
elif answer_10 == "B" :
    hyrax_score += 1
    kitty_score += 1
elif answer_10 == "C" :
    capybara_score += 1
    owl_score += 1
elif answer_10 == "D" :
    bear_score += 1
    elephant_score += 1
    
# compare the scores to find the animal with the most points 
if capybara_score >= bunny_score and capybara_score >= elephant_score and capybara_score >= owl_score and capybara_score >= bear_score and capybara_score >= hyrax_score and capybara_score >= kitty_score and capybara_score >= hedgehog_score:
    show_result(name, "Capybara")
    show_score_message(capybara_score)
elif bunny_score >= capybara_score and bunny_score >= elephant_score and bunny_score >= owl_score and bunny_score >= bear_score and bunny_score >= hyrax_score and bunny_score >= kitty_score and bunny_score >= hedgehog_score:
    show_result(name, "Bunny")
    show_score_message(bunny_score)
elif elephant_score >= capybara_score and elephant_score >= bunny_score and elephant_score >= owl_score and elephant_score >= bear_score and elephant_score >= hyrax_score and elephant_score >= kitty_score and elephant_score >= hedgehog_score:
    show_result(name, "Elephant")
    show_score_message(elephant_score)
elif owl_score >= capybara_score and owl_score >= bunny_score and owl_score >= elephant_score and owl_score >= bear_score and owl_score >= hyrax_score and owl_score >= kitty_score and owl_score >= hedgehog_score:
    show_result(name, "Owl")
    show_score_message(owl_score)
elif bear_score >= capybara_score and bear_score >= bunny_score and bear_score >= elephant_score and bear_score >= owl_score and bear_score >= hyrax_score and bear_score >= kitty_score and bear_score >= hedgehog_score:
    show_result(name, "Bear")
    show_score_message(bear_score)
elif hyrax_score >= capybara_score and hyrax_score >= elephant_score and hyrax_score >= bunny_score and hyrax_score >= bear_score and hyrax_score >= owl_score and hyrax_score >= kitty_score and hyrax_score >= hedgehog_score:
    show_result(name, "Hyrax")
    show_score_message(hyrax_score)
elif kitty_score >= capybara_score and kitty_score >= bunny_score and kitty_score >= elephant_score and kitty_score >= owl_score and kitty_score >= bear_score and kitty_score >= hyrax_score and kitty_score >=hedgehog_score:
    show_result(name, "Kitty")
    show_score_message(kitty_score)
elif hedgehog_score >= capybara_score and hedgehog_score >= bunny_score and hedgehog_score >= elephant_score and hedgehog_score >= owl_score and hedgehog_score >= bear_score and hedgehog_score >= hyrax_score and hedgehog_score >= kitty_score:
    show_result(name, "Hedgehog")
    show_score_message(hedgehog_score)