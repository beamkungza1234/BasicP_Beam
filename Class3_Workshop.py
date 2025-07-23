MonsterHP = 100

sword = 10
axe = 20
blaster = 30

try:
    while True:
    
        mode = int(input("Select Action:\n[1] Fight\n[2] Escape\nPlease select action [1/2]: "))

        if mode == 2:
            print("You leave the fight away\n\n")
            break

        elif mode == 1:
            maxAttack = int(input("How much you attack: "))
            while maxAttack > 0:
                maxAttack -= 1
                weapon = int(input(f"----------------------\nSelect Weapon: [{maxAttack} Attack Left]\n[1] Sword (+10)\n[2] Axe (+20)\n[3] Blaster (+30)\nChoose your weapon [1/2/3]: "))
                if weapon == 1:
                    MonsterHP = MonsterHP - sword
                    print(f"----------------------\nAttacking with Sword!\n[>] Monster now have {MonsterHP} HP left\n")

                elif weapon == 2:
                    MonsterHP = MonsterHP - axe
                    print(f"----------------------\nAttacking with Axe!\n[>] Monster now have {MonsterHP} HP left\n") 

                elif weapon == 3:
                    MonsterHP = MonsterHP - blaster
                    print(f"----------------------\nAttacking with Blaster!\n[>] Monster now have {MonsterHP} HP left\n") 
                else:
                    print("[?] Unknow weapon Please try again\n\n")
                    maxAttack = maxAttack + 1

                if MonsterHP == 0:
                    print("[>] You defeat the monster Congrats!\n-------------------------------------------\n\n")
                    break
            
                if MonsterHP < 0:
                    MonsterHP = 20
                    print("[!] Monster got heavily attack! The power of [นกคุมหลี] will revived them and give 20 HP\n    The battle will continue\n")

            if maxAttack == 0 and MonsterHP != 0:
                print("[!] Out off attack! Try again?\n--------------------------------\n\n")
                break
        else:
            print("[?] Unknow Action! Please try again\n\n")

except ValueError:
    print("[?] I don't know what do you type about? Maybe it happened by accident\n\n")
    

        

