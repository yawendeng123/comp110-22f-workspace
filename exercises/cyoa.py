"""A Simple, Rough, Text-Driven Escape Adventure Game."""
__author__ = "730607229"


from random import randint


points: int = 0
player: str = ""
achievements: list[str] = []
# memory: list[str] = []
endings: list[str] = []
# backpack: list[str] = []
# I'm sorry I have to subtract some interesting but complex variables due to time limit.
ending_1_reach: int = 0
ending_2_reach: int = 0
ending_3_reach: int = 0
WHITE_HEART: str = "\U0001F90D"
BLACK_HEART: str = "\U0001F5A4"
EXCLAMATION: str = "\U00002757"
THUMBS_UP: str = "\U0001F44D"


def greet() -> None:
    """A welcome messenage with some context to this adventure game, asking the player for their name."""
    global player
    print(f"{WHITE_HEART}=== Welcome to the Adventure Game!!! ==={WHITE_HEART}")
    print("It is a simple text-driven escape adventure game with multiple endings.")
    print("You will play the role of a student interested in the occult and reach different final endings based on your choices.")
    print(f"{EXCLAMATION} This game involves some slightly horror elements. If you feel uncomfortable, please quit the game immediately and take a deep breath.")
    print("Let's begain with your name!")
    player = input("Please enter your name: ")
    print(f"Good luck {WHITE_HEART}, {player}.\n")


read_count_instruction: int = 0
read_count_notes: int = 0


def author_notes() -> None:
    """Some instructions and boring author notes, add a total of 10 points to adventure points as thanks for reading."""
    global points
    global read_count_instruction
    global read_count_notes
    
    print("This is a simple, text-driven adventure game that involves some slightly horror elements. Players proceed to the next step by typing in the characters required by the game, where making choices or reaching achievements increases the number of adventure points.")
    print("Achievements include making a specific choice, or observation, or collecting specific items.")
    print("Different endings are unlocked by the player's choices.") 
    print("Adventure points, achievements, and endings achieved can be found in the menu under View Your Collections.")
    print("Achievements and points are one-time and once you have earned them, you cannot earn them again until you restart the game.")
    # print("Endings can be reached multiple times, and the View Endings page will show the names of the endings reached and the number of times they have been reached.")
    print("The number of adventure points you have accumulated will be displayed when you exit the game.")
    print("Try to unlock different endings!")
    # If player already read once, no more points.
    if read_count_instruction == 0:
        print(f"{player}, thank you for reading instructions. Here's 5 points as a gift.")
        points += 5
        read_count_instruction += 1
        print(f"Your total adventure points are {points}")
    
    print("Do you want to read some boring author notes? (yes/no)")
    choice: str = ""
    choice = input()
    answer: bool = False
    while answer is False:
        if choice == "yes":
            print("This is my first simple text-driven game. I really like Japanese horror RPG games and this game is a little prototype of the game I want to make. I'm sad that I have a lot of ideas but it's written in a simple and messy way due to my insufficient skills. Hopefully, I'll get a chance to refine it later, add some surprises, or make it more complex and turn it into a full-fledged game!")
            answer = True
            if read_count_notes == 0:
                print(f"{player}, thank you for reading these boring author notes. Here's another 5 points as a gift.")
                points += 5
                read_count_notes += 1
                print(f"Your total adventure points are {points}")

        elif choice == "no":
            answer = True
            print("Hope you enjoy the game!")
    
        else:
            choice = input("Please enter a valid option: ")


def collections_menu() -> None:
    print("[1] View Your Adventure Points")
    print("[2] View Your Achievements") 
    # print("[3] View Your Memory")
    print("[3] View Your Endings")   
    print("[0] Go Back to Main Menu")


def collections() -> None:
    """The place to view player's adventure points, items in memory, achievements, and endings."""
    collections_menu()
    choice: str = ""
    choice = input("\nPlease select one of the choices (1/2/3/0): ")

    while choice != "0":
        if choice == "1":
            print(f"\nHere's your accumulated adventure points: {points}")

        elif choice == "2":
            print("\nHere's your achievements.")
            print(achievements)

        elif choice == "3":
            # print("\nHere's the items in your memory.")
            # print(memory)

            # elif choice == "4":
            print("Here's your endings.")
            print(endings)

        else:
            print("\nPlease enter a valid option (1/2/3/0).")

        print()
        collections_menu()
        choice = input("\nPlease select one of the choices (1/2/3/0): ")


intro_achivement: int = 0
end: bool = False


def ending_1() -> None:
    """Ending 1 stories."""
    global ending_1_reach
    print("You reached the normal ending: Ending 1")
    print("After running down the hill, you quickly hopped on a bus and left the place. Although the information about the old family and the shadow of the mansion still haunts you from time to time in the days that follow, you no longer decide to go there.")
    print("You're back to your normal life.")
    ending_1_reach += 1
    if ending_1_reach == 1:
        endings.append("Ending 1: It was over before it started.")


def ending_2() -> None:
    """Ending 2 stories."""
    global ending_2_reach
    print("You reached the bad ending: Ending 2")
    print("You were left forever in the old mansion.")
    print("You've disappeared. People can't find you no matter how hard they look.")
    print("But when people followed the clues to this remote area, they couldn't find the way up the mountain, and they couldn't even inquire about anything useful about the ancient mansion.")
    print("All these things have disappeared.")
    ending_2_reach += 1
    if ending_2_reach == 1:
        endings.append(f"Ending 2: Stay forever {WHITE_HEART}{BLACK_HEART}")


def ending_3() -> None:
    """Ending 3 stories."""
    global ending_3_reach
    print("=== TO BE CONTINUED ===")
    ending_3_reach += 1
    if ending_3_reach == 1:
        endings.append("TO BE CONTINUED")


def intro_scene(point: int) -> int:
    """An intro scene to the adventure."""
    print("You are a student with a passion for history, folklore and the occult.")
    print("Occasionally, you learned about an old family rumored to be connected to curses.")
    print("Somehow, information about this family kept lingering in your mind, and in a trance, you ever felt like someone was watching you or talking to you.")
    print("You decided to visit this old mansion located in a remote mountain forest area.")
    print("You took bus alone to the site of the old mansion...")
    print("......")
    print("You arrive at the old mansion door. This old mansion is very large, with a high fence wall and lots of trees around it, and it seems like you can only enter through the gate.")
    print("The gate is unlocked.")
    print("You decide to:")
    print("[1] Go straight in")
    print("[2] Walk around the perimeter of the mansion and check")
    choice: str = ""
    choice = input("\nPlease select one of the choices (1/2): ")
    answer: bool = False
    while answer is False:
        if choice == "1":
            print("With a creak, you push open the gate door...")
            answer = True
            return point
        
        elif choice == "2":
            print("You were wise to choose to acknowledge your surroundings before entering the gate.")
            global intro_achivement
            if intro_achivement == 0:
                global achievements
                print(f"You reach an achivement {THUMBS_UP}")
                achievements.append("discretion")
                intro_achivement += 1
                point += 10
            print("You walk around the mansion and observe that it is actually much bigger than it looks, and you can't help but wonder how rich this old family was.")
            print("The fence looks very old, but it is quite strong. You try to push it and find that it does not move at all.")
            print("This wall is like a never-ending and very high, normal humans are unable to directly over this wall.")
            print("The surrounding vegetation is getting thicker and thicker, and you can no longer move forward, so you return to the gate and open it...")
            answer = True
            return point

        else:
            choice = input("\nPlease enter a valid option (1/2): ")


scene_1_achivement_a: int = 0
scene_1_achivement_b: int = 0


def scene_1(point: int) -> int:
    """The first scence."""
    global achievements
    print("You open the door. A cold breeze blows on your face. There is a dark corridor in front of you, but you can see a bright light at the end.")
    print("You feel excitement and an inexplicable sense of unease at the same time.")
    print("You decide to:")
    print("[1] Go straight in")
    print("[2] Run away")
    choice: str = ""
    choice = input("\nPlease select one of the choices (1/2): ")
    answer: bool = False
    while answer is False:
        if choice == "1":
            print("You think, there's nothing to be afraid of, and start walking forward.")
            print("You can't see the path under your feet, you walk a little bumpy, and after a while, you successfully reach the inner side of the huge fence wall.")
            global scene_1_achivement_a
            if scene_1_achivement_a == 0:
                print(f"You reach an achivement {THUMBS_UP}")
                achievements.append("grit")
                scene_1_achivement_a += 1
                point += 10
            answer = True
            return point
        
        elif choice == "2":
            print("You feel very uneasy, and after weighing the pros and cons again and again, you run away as fast as you can.")
            global scene_1_achivement_b
            global end
            if scene_1_achivement_b == 0:
                print(f"You reach an achivement {THUMBS_UP}")
                achievements.append("Running away is also a courage.")
                scene_1_achivement_b += 1
                point += 10
            end = True
            ending_1()
            answer = True
            return point

        else:
            choice = input("\nPlease enter a valid option (1/2): ")


scene_2_achivement_a: int = 0
scene_2_achivement_b: int = 0
scene_2_achivement_c: int = 0


def scene_2(point: int) -> int:
    """The second scene."""
    global achievements
    global end
    global scene_2_achivement_a
    global scene_2_achivement_b
    global scene_2_achivement_c
    print("You walked into the courtyard of the mansion. Quite surprisingly, from the inside, the mansion is not old and has an atmosphere of classical Japanese architecture.")
    print("You're excited about such fascinating cultural history.")
    print("Just as you're about to pull out your notebook and take note of such a rare sighting of the building, a strange sound comes.")
    print("It sounded like flesh ripping and twisting, and the sound seemed to be coming closer this way!!!")
    print("You decide:")
    print("[1] Calm and motionless")
    print("[2] Try to run outside the huge fence wall")
    print("[3] Quickly run inside the mansion")
    print("[4] Curiously go to the direction of the sound")
    choice: str = ""
    choice = input("\nPlease select one of the choices (1/2/3/4): ")
    answer: bool = False
    while answer is False:
        if choice == "1":
            print("You calm down and don't move a muscle, hoping that the source of the strange sound doesn't find you.")
            rolls: int = 0
            rolls = randint(1, 3)
            if rolls == 1:
                print("Fortunately, the source of the sound does not find you.")
                print("You glance away and see the source of the sound is a huge, twisted, horrible monster!!!")
                if scene_2_achivement_a == 0:
                    print(f"You reach an achivement {THUMBS_UP}")
                    achievements.append("lucky!")
                    scene_2_achivement_a += 1
                    point += 10
                print("When the monster is far away, you quickly slip inside the mansion.")
                answer = True
                return point

            else:
                print("Unfortunately, you've been found out!!!")
                print("The giant twisted monster rushes over to you. You pass out.")
                end = True
                ending_2()
                answer = True
                return point
            
        elif choice == "2":
            print("You feel panic and try to escape through the door behind you.")
            print("But the door behind you is somehow locked! The sound of shaking the door has attracted the monster!")
            print("The giant twisted monster rushes over to you. You pass out.")
            end = True
            ending_2()
            answer = True
            return point

        elif choice == "3":
            print("You quickly slip inside the mansion without sound.")
            if scene_2_achivement_b == 0:
                    print(f"You reach an achivement {THUMBS_UP}")
                    achievements.append("decisive!")
                    scene_2_achivement_b += 1
                    point += 10
            print("Hiding in the door inside the mansion, you glance at the source of the sound, and find it is a huge, twisted, horrible monster!!!")
            answer = True
            return point

        elif choice == "4":
            print("You walk curiously towards the source of the sound.")
            print("The source of the sound was found to be a huge, twisted, horrible monster!!!")
            print("The giant twisted monster rushes over to you. You pass out.")
            if scene_2_achivement_c == 0:
                    print(f"You reach an achivement {THUMBS_UP}")
                    achievements.append("Curiosity killed you.")
                    scene_2_achivement_c += 1
                    point += 10
            end = True
            ending_2()
            answer = True
            return point
        
        else:
            choice = input("\nPlease enter a valid option (1/2/3/4): ")


scene_3_achivement_a: int = 0


def scene_3(point:int) -> int:
    """The third scene."""
    global achievements
    global end
    global scene_3_achivement_a
    print("=== TO BE CONTINUED ===")
    print("Or you can donate money to support me ~")
    print("Sorry it's just a joke. Due to time limit, I will try to improve the whole game later.")
    if scene_3_achivement_a == 0:
        print("Thank you for your understanding. Here are some points and achievement.")
        achievements.append("kind")
        scene_3_achivement_a += 1
        point += 10
    end = True
    ending_3()
    return point


def adventure(point: int) -> int:
    """The whole procedure of adventure."""
    global end
    end = False
    if end is False:
        point = intro_scene(points)
        point = scene_1(point)
    if end is False:
        point = scene_2(point)
    if end is False:
        point = scene_3(point)
    return point


def menu() -> None:
    print("=== Menu ===")
    print("[1] New Adventure")
    print("[2] View Your Collections") 
    print("[3] Instructions and Author Notes")
    print("[0] End Game")


def main() -> None:
    """The entrypoint of the program and main game loop."""
    greet()
    global points
    points = 0
    menu()
    choice: str = ""
    choice = input("\nPlease select one of the choices (1/2/3/0): ")
    while choice != "0":
        if choice == "1":
            print("\nLet's start a new adventure!")
            # call adventure function.
            points = adventure(points)
            print(f"Your adventure has ended. Here's your accumulated adventure points: {points}")

        elif choice == "2":
            print("\nHere's the place to view your adventure points, achievements, and endings.")
            collections()

        elif choice == "3":
            print("\nHere's the instructions and some boring author notes:")
            author_notes()

        else:
            print("\nPlease enter a valid option (1/2/3/0).")
        
        print()
        # The updated points are at the end of each branches. So don't need to update them here.
        menu()
        choice = input("\nPlease select one of the choices (1/2/3/0): ")
    
    print("\nThank you for playing!")
    print(f"Sayonara, {player}. We'll meet again soon{WHITE_HEART}")
    # Sayonara means Goodby in Japanese. I just want to substitute Goodby with another word that seems more interesting.
    print(f"Your accumulated adventure points are: {points}")
    quit()


if __name__ == "__main__":
    main()
