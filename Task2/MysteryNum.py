import random
games=[] 
import json

def diff():
    print("---------------------------------")
    print("Select your difficulty level")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")
    level=int(input("Enter your choice: "))
    print("---------------------------------")
    if level==1:
        difficulty="Easy"
        max_num=100
        max_attempts=10
        base_score=100

    elif level==2:
        difficulty="Medium"
        max_num=300
        max_attempts=7
        base_score=200
        
    elif level==3:
        difficulty="Hard"
        max_num=500
        max_attempts=5
        base_score=300

    else:
        print("Enter a valid choice")
        return 
    
    mystery_num=random.randint(1,max_num)
    attempts=0
    while True:
        num=int(input("Enter a number: "))
        attempts+=1
        score = 0
        if num==mystery_num:
                score = base_score - ((attempts - 1) * 10)
                game={
                         "Difficulty":difficulty,
                         "Result":"Won",
                         "Attempts":attempts,
                         "Score":score
                    }
                games.append(game)
                savegames()
                print(f"Horayyy u won!🎉\n Attempts={attempts} \n Score={score}")
                break
        else:
            if attempts>=max_attempts:
                        print(f"You ran out of attempts! The mystery number was {mystery_num}.")
                        break
            print("Try again")
            if num>mystery_num:
                print("Go low")
            else:
                print("Go high")


def pastgames():
     if not games:
          print("No games history found")
     else:
          for game in games:
               print("------------ MYSTERYNUM ------------")
               print(f"Difficulty: {game['Difficulty']}")
               print(f"Result: {game['Result']}")
               print(f"Attempts: {game['Attempts']}")
               print(f"Score: {game['Score']}")
               print("------------------------------------")
          
def savegames():
     with open ("games.json","w") as file:
          json.dump(games,file)

def loadgames():
      global games
      try:
            with open ("games.json","r") as file:
                  games=json.load(file)
      except FileNotFoundError:
             games=[]

def scores():
     print("------------------------------------")
               
     if not games:
          print("No games palyed yet")
     else:
          easy = 0
          medium = 0
          hard = 0

          for game in games:
            if game["Difficulty"] == "Easy":
                easy += game["Score"]

            elif game["Difficulty"] == "Medium":
                medium += game["Score"]

            elif game["Difficulty"] == "Hard":
                hard += game["Score"]

          print("------------- SCORES ------------")
          print(f"Easy: {easy}")
          print(f"Medium: {medium}")
          print(f"Hard: {hard}")

     print("------------------------------------")
               
          
loadgames()

while True:
    print("\n" )
    print("========== MysteryNum ===========")
    print("1)Difficulty")
    print("2)View past games")
    print("3)View scores")
    print("4)Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        diff()
    elif choice==2:
        pastgames()
    elif choice==3:
        scores()
    elif choice==4:
        print("Thank you for using MysteryNum")
        print("\n" )
        break
    else:
        print("Enter a valid choice")

