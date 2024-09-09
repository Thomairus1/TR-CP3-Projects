
player_dmg = 25
player_hp = 100

enemy1_dmg = 15
enemy1_hp = 100

enemy2_dmg = 34
enemy2_hp = 150

enemy3_dmg = 50
enemy3_hp = 200

def combat():
    global player_dmg
    global player_hp

    global enemy1_dmg
    global enemy1_hp

    global enemy2_dmg
    global enemy2_hp

    global enemy3_dmg
    global enemy3_hp

    count = 0
    
    if count % 2 == 0:
        turn = input("")