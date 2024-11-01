print("Note: if a word has '' around it (like 'yes') then that word is one of the options for input.")
player_dmg = 25
player_hp = 100
max_hp = 100

enemy1_name = "Ice Knight"
enemy1_dmg = 15
enemy1_hp = 100

enemy2_name = "Dark Mage"
enemy2_dmg = 34
enemy2_hp = 150

boss_name = "Scorching Demon"
boss_dmg = 50
boss_hp = 200

heals = []
def heal(max_HP):
    global player_hp
    global heals
    if heals != []:
        print("\nThese are your heals:")
        for heal in heals:
            print(heal + ",")
        hc = input("\nWhich heal do you want to use? (type '1' for small, '2' for normal, and '3' for a big) ")
        print("\n")
        if hc == "1":
            hc = "Small HP Potion"
            heals.remove("Small HP Potion(heals 25 health)")
            player_hp += 25
            if player_hp <= max_HP:
                return f"You health is now: {player_hp}.\n"
            elif player_hp > max_HP:
                player_hp -= (player_hp-max_HP)
                return f"You health is now: {player_hp}.\n"
            else:
                return f"You health is now: {player_hp}.\n"
        elif hc == "2":
            hc = "HP Potion"
            heals.remove("HP Potion(heals 50 health)")
            player_hp += 50
            if player_hp <= max_HP:
                return f"You health is now: {player_hp}.\n"
            elif player_hp > max_HP:
                player_hp -= (player_hp-max_HP)
                return f"You health is now: {player_hp}.\n"
            else:
                return f"You health is now: {player_hp}.\n"
        elif hc == "3":
            hc = "Big HP Potion"
            heals.remove("Big HP Potion(heals 100 health)")
            player_hp += 100
            if player_hp <= max_HP:
                return f"You health is now: {player_hp}.\n"
            elif player_hp > max_HP:
                player_hp -= (player_hp-player_HP)
                return f"You health is now: {player_hp}.\n"
            else:
                return f"You health is now: {player_hp}.\n"
    elif heals == []:
        return "\nYou don't have any heal potions.\n"

def combat(player_DMG, max_HP, enemy_name, enemy_dmg, enemy_hp):
    global player_hp
    count = 0
    print(f"\nYou find a {enemy_name} with {enemy_dmg} damage and {enemy_hp} health.\n")
    print(f"You have {player_DMG} damage and {player_hp} health.\n")
    while True:
        if count % 2 == 0:
            turn = input(f"Do you 'attack' the {enemy_name}, or 'heal' yourself? ")
            if turn == "attack":
                enemy_hp -= player_DMG
                print(f"\nYou dealt {player_DMG} to the {enemy_name}. They now have {enemy_hp} health.")
                count += 1
                if enemy_hp <= 0:
                    print(f"\nYou deafeated the {enemy_name}.\n")
                    combat_end = input("Do you want to heal?('yes' or 'no') ")
                    if combat_end == "yes":
                        print(heal(max_HP))
                    return True
                    break
            elif turn == "heal": 
                count += 1
                print(heal(max_HP))
        elif count % 2 != 0:
            player_hp -= enemy_dmg
            print(f"The {enemy_name} attacked you for {enemy_dmg}. Your health is now {player_hp}.\n")
            if player_hp <= 0:
                return "You lost all your health. Game Over.\n"
            count += 1
        
r_count = 1
r1 = False
r2 = False
r3 = False
r4 = False
r5 = False
r6 = False
r7 = False
r8 = False
r9 = False
while True:
    if r_count == 1:
        if r1 == False:
            print("You wake up lying in a cold and dark cave. You can hear water dripping in the distance, and the sound eerily echoes throughout many chambers. You slowly get up, joints aching and arms numb, and suddenly you remember just how close you had been to beating the boss and sigh at the prospect of doing it all over again.\n")
        while True:
            go1 = input("There is damp hallway in front of you. Do you proceed?('yes' or 'no') ")
            if go1 == "yes":
                r_count += 1
                r1 = True
                break
            else:
                r1 = True
                continue
        r1 = True
        else:
            print("You've already been in this room.")
    elif r_count == 2:
        if r2 == False:
            c1 = input("\nYou find two Small health Potions in the center of the room. Do you pick them up? ('yes' or 'no') ")
            if c1 == "yes":
                heals.append("Small HP Potion(heals 25 health)")
                heals.append("Small HP Potion(heals 25 health)")
                print("\nTwo Small HP Potions were added to heals inventory.\n")
            c1 = input("You find an old ax next to the potions. Do you pick it up for + 30 damage? ('yes' or 'no') ")
            if c1 == "yes":
                player_dmg = 55
                print(f"\nYour damage is now {player_dmg}.\n")
            r2 = True
        else:
            print("You've alredy been in this room.")
        while True:
            go2 = input("There is a hallway that extends dark tendrils towards you from to the left, and there is a cold hallway to the right. Are you going 'left' or 'right' or 'back'? ")
            if go2 == "left":
                r_count +=1
                break
            elif go2 == "right":
                r_count += 4
                break
            elif go2 == "back":
                r_count -= 1
                break
            else:
                continue 
    elif r_count == 3:
        if r3 == False:
            r3_return = combat(player_dmg, max_hp, enemy2_name, enemy2_dmg, enemy2_hp)
            if r3_return == True:
                c3 = input("\nThe enemy drops a pair of Gaunlets. Do you pick them up for + 75 damage?('yes' or 'no') ")
                if c3 == "yes":
                    print("You replaced your old weapon.")
                    player_dmg = 100
                    print(f"Your damage is now {player_dmg}.\n")
            r3 = True        
        else:
            print("You've alredy been in this room.")
        while True:
            go3 = input("There is a frigid hallway to your left , and there is a dark hallway to the right. Are you going 'left' or 'right' or 'back'? ")
            if go3 == "left":
                r_count +=1
                break
            elif go3 == "right":
                r_count += 2
                break
            elif go3 == " back":
                r_count -= 1
                break
            else:
                continue
    elif r_count == 4:
        if r4 == False:
            r4_return = combat(player_dmg, max_hp, enemy1_name, enemy1_dmg, enemy1_hp)
            r4_return = combat(player_dmg, max_hp, enemy1_name, enemy1_dmg, enemy1_hp)
            if r4_return == True:
                c4 = input("\nThe enemies drop two HP Potions. Do you pick them up? ('yes' or 'no') ")
                if c4 == "yes":
                    heals.append("HP Potion(heals 50 health)")
                    heals.append("HP Potion(heals 50 health)")
                    print("\nTwo HP Potions were added to heals inventory")
            r4 = True
        else:
            print("You've alredy been in this room.")
        while True:
            go4 = input("\nThere is a hallway going forward and then turning right, it is aglow with embers. Do you 'follow' it or go 'back'?('follow' or 'back') ")
            if go4 == "follow":
                r_count +=5
                break
            elif go4 == "back":
                r_count -= 1
                break
            else:
                continue
    elif r_count == 5:
        if r5 == False:
            r5_return = combat(player_dmg, max_hp, enemy2_name, enemy2_dmg, enemy2_hp)
            if r5_return == True:
                c5 = input("\nThe enemy dropped a Red Armor. Do you pick it up for + 100 max health? ('yes' or 'no') ")
                if c5 == "yes":
                    if max_hp == 150:
                        player_hp -= 50
                        player_hp += 100
                        max_hp -= 50
                        max_hp += 100
                        if player_hp > max_hp:
                            player_hp -= (player_hp-max_hp)
                    else:
                        player_hp += 100
                        max_hp += 100
                        if player_hp > max_hp:
                            player_hp -= (player_hp-max_hp)
                    print("\nYour old armor was replaced.")
                    print(f"\nYour max health is now {max_hp} and your health is {player_hp}.")
            r5 = True
        else:
            print("You've alredy been in this room.")
        while True:
            go5 = input("\nStraight in front of you a hallway expels sulfur and heat. Do you 'follow' it or go 'back'?('follow' or 'back') ")
            if go5 == "follow":
                r_count +=4
                break
            elif go5 == "back":
                r_count -= 2
                break
            else:
                continue
    elif r_count == 6:
        if r6 == False:
            r6_return = combat(player_dmg, max_hp, enemy1_name, enemy1_dmg, enemy1_hp)
            if r6_return == True:
                c6 = input("\nThe enemy dropped a blue armor. Do you pick it up for + 50 max health?('yes' or 'no') ")
                if c6 == "yes":
                    if max_hp == 200:
                        player_hp -= 100
                        player_hp += 50
                        max_hp -= 100
                        max_hp += 50
                        if player_hp > max_hp:
                            player_hp -= (player_hp-max_hp)
                else:
                    player_hp += 50
                    max_hp += 50
                    if player_hp > max_hp:
                        player_hp -= (player_hp-max_hp)
                    print("\nYour old armor was replaced.")
                    print(f"\nYour max health is now {max_hp} and your health is {player_hp}.")
            r6 = True
        else:
            print("You've alredy been in this room.")
        while True:
            go6 = input("\nThe hallway to the left is freezing, the one to the right you cannot see. Do you go 'left' or 'right' or 'back'? ")
            if go6 == "left":
                r_count +=1
                break
            elif go6 == "right":
                r_count += 2
                break
            elif go6 == "back":
                r_count -= 4
                break
            else:
                continue
    elif r_count == 7:
        if r7 == False:
            r7_return = combat(player_dmg, max_hp, enemy1_name, enemy1_dmg, enemy1_hp)
            if r7_return == True:
                c7 = input("\nThe enemy dropped a Steel Sword. Do you pick it up for + 45 damage?('yes' or 'no') ")
                if c6 == "yes":
                    player_dmg = 70
                    print("You replaced your old weapon.\n")
                    print(f"Your damage is now {player_dmg}.\n")
            while True:
                go7 = input("\nStraight ahead the hallway has walls with waterfalls of molten lava. Do you 'follow' it or go 'back'? ")
                if go7 == "follow":
                    r_count +=2
                    break
                elif go7 == "back":
                    r_count -= 1
                    break
                else:
                    continue
            r7 = True
        else:
            print("You've alredy been in this room.")
    elif r_count == 8:
        if r8 == False:
            r8_return = combat(player_dmg, max_hp, enemy2_name, enemy2_dmg, enemy2_hp)
            if r8_return == True:
                c8 = input("\nThe enemy drops a Big HP Potion. Do you pick it up?('yes' or 'no') ")
                if c8 == "yes":
                    heals.append("Big HP Potion(heals 100 health)")
                    print("A Big HP Potion was added to heals inventory.")
            while True:
                go8 = input("\nThe hallway in front of you has a glowing river of lava and what seems to be a drawbridge mechanism. Do you 'follow' it or go 'back'? ")
                if go8 == "follow":
                    print("\nYou get to the drawbridge mechanism and spin it. The draw bridge comes down over the lava river.")
                    r_count +=1
                    break
                elif go8 == "back":
                    r_count -= 2
                    break
                else:
                    continue
            r8 = True
        else:
            print("You've alredy been in this room.")
    elif r_count == 9:
        r9_return = combat(player_dmg, max_hp, boss_name, boss_dmg, boss_hp)
        if r9 == True:
            print(f"You defeated the {boss_name}. You win.\n")
            print("The wall behind the boss opens up, and you climb up stairs to freedom from the dungeon.")
            break
