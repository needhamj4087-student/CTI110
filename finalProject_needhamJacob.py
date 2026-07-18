#Jacob Needham
#07/16/2026
#finalProject for CTI110
#A text based python game

"""
=========================================================
            GOBLIN ADVENTURE
            Single File Python Game
=========================================================

Requirements Met:
- Single .py file
- main() function
- random library
- time library
- Goblin player
- 5 blue slimes
- Sword
- Shield
- Bow + 5 arrows
- Player HP = 5
- Slime HP = 3
- Inventory changes during gameplay
- Clear spacing and comments

=========================================================
"""

import random
import time


# =========================================================
#                      CONSTANTS
# =========================================================

GOBLIN = "🧌"          # Change to "👺" or "🟢" if preferred
SLIME = "🔵"

PLAYER_MAX_HP = 5
SLIME_HP = 3
NUMBER_OF_SLIMES = 5


# =========================================================
#                      PLAYER DATA
# =========================================================

player = {
    "name": "Mighty Goblin",
    "icon": GOBLIN,

    "hp": PLAYER_MAX_HP,

    "inventory": [],

    "sword": False,
    "shield": False,
    "bow": False,

    "arrows": 0,

    "slimes_defeated": 0,

    "progress": 0 

}


# =========================================================
#                 RESET PLAYER
# =========================================================

def reset_player():

    player["hp"] = PLAYER_MAX_HP

    player["inventory"] = []

    player["sword"] = False

    player["shield"] = False

    player["bow"] = False

    player["arrows"] = 0

    player["slimes_defeated"] = 0

    player["progress"] = 0


# =========================================================
#                  ENEMY CREATION
# =========================================================

def create_slimes():
    """
    Creates all five slimes.
    """

    slimes = []

    for i in range(NUMBER_OF_SLIMES):

        slime = {
            "name": f"Blue Slime {i+1}",
            "icon": SLIME,
            "hp": SLIME_HP,
            "alive": True
        }

        slimes.append(slime)

    return slimes


# =========================================================
#                 DISPLAY PLAYER
# =========================================================

def show_player():

    print("\n----------------------------------------")
    print(f"{player['icon']}  {player['name']}")
    print("----------------------------------------")

    print("HP:", player["hp"])

    print("Inventory:", player["inventory"])

    print("Sword:", player["sword"])
    print("Shield:", player["shield"])
    print("Bow:", player["bow"])
    print("Arrows:", player["arrows"])

    print("Slimes Defeated:", player["slimes_defeated"])

    print("----------------------------------------\n")




# =========================================================
#                 SHOW PROGRESS
# =========================================================

def show_progress(route):

    forest = [
        "START",
        "🗡",
        "🔵",
        "🛡",
        "🔵",
        "🏹",
        "🔵",
        "🏆"
    ]

    mountain = [
        "START",
        "🏹",
        "🔵",
        "🗡",
        "🔵",
        "🛡",
        "🔵",
        "🏆"
    ]

    if route == "forest":
        path = forest
        title = "FOREST TRAIL"

    else:
        path = mountain
        title = "MOUNTAIN PASS"

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    for i, place in enumerate(path):

        if i == player["progress"]:
            print("🧌", end=" ")

        print(place, end=" ")

        if i < len(path)-1:
            print("---->", end=" ")

    print("\n")

    




# =========================================================
#                  PAUSE GAME
# =========================================================

def pause():

    input("\nPress ENTER to continue...")


# =========================================================
#                   PICKUP ITEMS
# =========================================================

def pickup_item(item):

    print(f"\nYou found a discarded {item}!")

    time.sleep(1)

    if item == "Sword":
        player["sword"] = True

    elif item == "Shield":
        player["shield"] = True

    elif item == "Bow":
        player["bow"] = True
        player["arrows"] = 5

    player["inventory"].append(item)

    print(f"A {item} has been added to inventory!")

    time.sleep(1)

    show_player()

    pause()



# =========================================================
#                    SLIME ATTACK
# =========================================================

def slime_attack():

    damage = random.randint(0, 2)

    if player["shield"]:
        damage = max(0, damage - 1)

    player["hp"] -= damage

    print(f"\nThe slime attacks!")

    time.sleep(.8)

    print(f"You lose {damage} HP!")

    time.sleep(.8)


# =========================================================
#                 SLIME ENCOUNTER
# =========================================================

def encounter_slime(slime):

    print()

    print("\n" + "=" * 45)

    print("You hear something in the bushes.....")

    time.sleep(1.5)

    print()
    print("Enter Wild Blue Slime")
    print(f"  {slime['icon']}  A {slime['name']} appears, What will you do?!")
    print("=" * 45)

    print(f"Enemy HP: {slime['hp']}")
    print(f"Your HP : {player['hp']}")

    time.sleep(2)

    pause()

    player_attack(slime)


# =========================================================
#                 PLAYER ATTACK
# =========================================================

def player_attack(slime):

    while slime["hp"] > 0 and player["hp"] > 0:

        print("\nChoose your next attack")

        print("1 - Sword")

        if player["bow"] and player["arrows"] > 0:
            print("2 - Bow")

        choice = input("> ")

        print()

        # ------------------------------
        # Sword Attack
        # ------------------------------

        if choice == "1":

            if not player["sword"]:

                print("You don't yet have a sword!")

                continue

            damage = random.randint(1, 2)

            slime["hp"] -= damage

            print(f"You slashed it for {damage} damage!")

        # ------------------------------
        # Bow Attack
        # ------------------------------

        elif choice == "2":

            if not player["bow"]:

                print("You don't have a bow yet.")

                continue

            if player["arrows"] <= 0:

                print("No more arrows remaining, too bad!")

                continue

            player["arrows"] -= 1

            damage = random.randint(1, 3)

            slime["hp"] -= damage

            print(f"You shoot an arrow, sighted at the Enemy!")

            print(f"Damage: {damage}")

            print(f"Arrows left: {player['arrows']} Be Careful you save them for when you need them.")

        else:

            print("Invalid choice. Try again.")

            continue

        time.sleep(1)

        # ------------------------------

        if slime["hp"] <= 0:

            slime["alive"] = False

            player["slimes_defeated"] += 1

            print(f"\n{slime['name']}  has been defeated!")

            print("You may now continue on your way.")

            pause()

            break

        # ------------------------------

        slime_attack()

        if player["hp"] <= 0:
            print("\nYou have fallen in this battle ...")
            pause()
            return

        print(f"Player HP: {player['hp']}")

        print(f"{slime['name']} HP: {slime['hp']}")

        time.sleep(1)


# =========================================================
#                   GAME PATH
# =========================================================

def forest_route(slimes):

    pickup_item("Sword")

    player["progress"] += 1

    show_progress("forest")

    print("\nThe Forest grows Restless as you wonder on....")
    print("darkness closes in...")
    pause()

    encounter_slime(slimes[0])

    if player["hp"] <= 0:
        return


    player["progress"] += 1

    show_progress("forest")

    print("\nAs you Wipe the Slime from your sword and walk on...")
    pause()


    encounter_slime(slimes[1])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("forest")


    print("\nYou discover a chest by the wayside ...")
    pickup_item("Shield")

    show_progress("forest")

    encounter_slime(slimes[2])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("forest")

    print("Yet another foe slain this day.")
    pause()

    encounter_slime(slimes[3])

    if player["hp"] <= 0:
        return


    print("\nHanging from the branch of a tree you spy....what?...")
    pause()

    pickup_item("Bow")

    player["progress"] += 1

    show_progress("forest")

    encounter_slime(slimes[4])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("forest")

def mountain_route(slimes):

    print("\nHanging from the branch of a tree you spy....what?...")
    pause()

    pickup_item("Bow")

    player["progress"] += 1

    show_progress("mountain")

    encounter_slime(slimes[0])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("mountain")

    print("\nAs you check your quiver and walk on you think on your journey of life ...")
    pause()

    encounter_slime(slimes[1])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("mountain")

    pickup_item("Sword")

    player["progress"] += 1

    show_progress("mountain")

    print("\nThe Mountain Stirs all around ye as you wonder on....")
    pause()

    encounter_slime(slimes[2])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("mountain")

    print("\nAs you Wipe the Slime from your sword and walk on pondering your path ....")
    pause()

    encounter_slime(slimes[3])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("mountain")

    print("Yet another foe slain this day.")
    pause()


    print("\nYou discover a chest by the wayside hidden from under a bush ....")  
    pickup_item("Shield")

    player["progress"] += 1

    show_progress("mountain")

    encounter_slime(slimes[4])

    if player["hp"] <= 0:
        return

    player["progress"] += 1

    show_progress("mountain")    



# =========================================================
#                  GAME ENDING
# =========================================================

def ending():

    print()

    print("=" * 45)

    if player["hp"] > 0:

        print("\nCONGRATULATIONS! You've completed this journey.")
        print("\nOur Goblin friend has made it home to the tribe, with fresh meat to be had.")

        print()

        print("The Mighty Goblin defeated all five slimes!")

        print()

        print("Final HP:", player["hp"])

        print("Your Remaining Arrows:", player["arrows"])

        print()

        print("An Inventoryfull of:")

        for item in player["inventory"]:

            print("-", item)

    else:

        print("GAME OVER")

    print("=" * 45)


# =========================================================
#                    MAIN FUNCTION
# =========================================================

def main():

    while True:

        reset_player()

        slimes = create_slimes()


        print("=" * 45)

        print("GOBLIN ADVENTURE")

        print("=" * 45)

        print()

        print("A Mighty Goblin begins with no weapon for defense...")
        print("\nYou must Journey home by way of The Forest Trail or over The Mountain Pass")
        print("\nWith a fresh kill on your shoulders and a broken bow, will you make it home?")

        time.sleep(2)

        show_player()

        print("\nChoose your path wisely!")

        print("1 - Forest Trail")
        print("2 - Mountain Pass")

        route = input("> ")

        if route == "1":

            forest_route(slimes)

        elif route == "2":

             mountain_route(slimes)

        else:

            print("Invalid choice.")

            return

        if player["hp"] <= 0:
            

            print("\nYou have perished .....")
            print()

            print("Restarting game .....")
            print()
            print()

            time.sleep(3)

            continue
        
        break

    ending()


# =========================================================
#               PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()