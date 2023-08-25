import random
import pyttsx3

tries=5
playagain=True

def title():
   title="Welcome to WordFruit Fusion!"
   print("*" * len(title))
   print(title)
   print("*" * len(title))

def ready():
     speaker = pyttsx3.init()
     speaker.say('three , two , one , go')
     speaker.runAndWait()
     



def easylevel():
       print()
       ready()
       print("GAME ON!")
       easyfruits=['apple','peach','melon','grape','guava','mango','lemon','kiwi','cherry','pear','plum']
       random_index=random.randint(0,len(easyfruits)-1)
       fruit=easyfruits[random_index]
       print(f"It's a {len(fruit)} letter fruit ")
       print(f"You have {tries} tries!")
       analysis(fruit)

def hardlevel():
       print()
       ready()
       print("GAME ON!")
       hardfruits=['starfruit','strawberry','cranberry','papaya','avacoda','watermelon','pineapple','lychee','pomegranate','raspberry','jackfruit']
       random_index=random.randint(0,len(hardfruits)-1)
       fruit=hardfruits[random_index]
       print(f"It's a {len(fruit)} letter fruit ")
       print(f"You have {tries} tries!")
       analysis(fruit)
       

def analysis(fruit):
    j=0
    while j<tries:
        guess1=input("Enter your guess:")
        guess=guess1.lower()
        if len(guess)!=len(fruit):
             print(f"IT's a {len(fruit)} letter word ")
             continue
        correct_pos=0
        incorrect_pos=len(fruit)

        for i in range(0,len(guess)):
            if fruit[i]==guess[i]:
               print(guess[i],end='')
               correct_pos=correct_pos+1
               incorrect_pos=incorrect_pos-1
            else:
              print("_",end='')
        if correct_pos==len(guess):
                   print("\nYou got it right!")
                   break
        j=j+1
        print()
        print(f"CORRECT POSITIONS {correct_pos} | INCORRECT POSITIONS {incorrect_pos}")

def funfact():
     fflist=['''Lemon Juice and Ink: Lemon juice can act as invisible ink due to its ability to oxidize and turn brown when heated.''',
              '''Coconuts and the Sea: Coconuts can float long distances across oceans and are sometimes called the "traveling nut" for this reason.''',
              '''Largest Fruit: The jackfruit holds the title for the world's largest fruit. It can weigh up to 80 pounds and grow to be about 36 inches long.''',
              '''Tomatoes Are Fruits: Despite commonly being thought of as vegetables, tomatoes are actually fruits. They're classified as berries because they develop from the ovary of a flower and contain seeds.''',
              '''Apples Float in Water: Apples are about 25% air, which is why they can float in water.''',
              '''Mango Varieties: There are over 1,000 varieties of mangoes, each with its distinctive flavor, size, and color.''',
              '''Strawberry Seeds on the Outside: Strawberries are unique because their seeds are on the exterior,with each seed acting as a separate fruit.''',
                '''Long-Lived Apple Trees: Apple trees can live for more than 100 years and continue to produce fruit throughout their lifespan.''',
            '''Rainbow of Carrots: Carrots come in a variety of colors, including purple, red, yellow, and white, each with its unique flavor profile.''',
            '''Fruit Ripening Gas: Ethylene gas is produced by fruits like bananas, apples, and tomatoes and can help accelerate the ripening of other fruits.''']
     random_fact = random.choice(fflist)
     print(random_fact)



if __name__ == "__main__":
    title()
    while playagain==True:
           
           print('''SELECT LEVEL
1.Easy level (four and five letter fruits)
2.Hard level (more than five letter fruits)''')
           choice = int(input("Enter your choice:"))
           if choice == 1:
              easylevel()
           elif choice == 2:
               hardlevel()
           else:
            print("INVALID OPTION")
           onemore=input("Want to play again?(y/n):")
           if onemore=='y':
                playagain=True
           else:
                playagain=False
                print()
                print("Congratulations! You've completed the Wordle game.")
                print("Here's a fun fruit fact to wrap things up :)")
                funfact()

    

