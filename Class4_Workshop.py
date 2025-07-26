movieList = [
    {"id": 1, "name": "Skibidi Toliet", "price": 30, "minAge": 10, "type": "Fantasy"},
    {"id": 2, "name": "Badass Basic Programing", "price": 40, "minAge": "G", "type": "Documentary"},
    {"id": 3, "name": "Robood The Movie", "price": 35, "minAge": 13, "type": "Horror"},
    {"id": 4, "name": "Supersigma", "price": 45, "minAge": 18,  "type": "Action"},
    {"id": 5, "name": "IT Startpack IT31", "price": 30, "minAge": 15,  "type": "Scifi"},
    {"id": 6, "name": "Beasts and the frog", "price": 45, "minAge": 16,  "type": "Romantic"},
    {"id": 7, "name": "Yohane the Parhelion", "price": 50, "minAge": "G",  "type": "Fantasy"},
]
    
# ขอยาดจดไว้กันลืม xD

choice = []
# นำเลขหนังที่เลือก จาก movie(int)มาลบกับเลข index ของ movieList ทีแสดงข้อมูลหนังทั้งหมด เพื่อเลือกหนังที่ถูกต้อง
def movieChoice():
    movie = int(input("Choose Movie to watching (If you dont know what movie we have. Pls visit our movie list first by Press [1] on welcome screen)\n>> "))
    if 1 <= movie <= 7:
        return movieList[movie - 1]
    return None       

def soundtrack():
    st = int(input("\nSelect your sountrack:\n[1] ภาษาไทย (TH)\n[2] English (EN)\n[3] 日本語 (JP)\n>> "))
    if st == 1:
        st = "ภาษาไทย (TH)"
        return st
    
    elif st == 2:
        st = "English (EN)"
        return st
    
    elif st == 3:
        st = "日本語 (JP)"
        return st
    
    return None

def inputAge():
    age = int(input("Input your age: "))
    if age >= 1:
        return age
    return None


while True:

    print("SIT Theather Welcome! - Please select an options\n[1] Show movie list\n[2] Choose Move")
    sel = int(input(">> "))
    if sel == 1:
        print("\nNo. | Name                      | Type            | Price    | Rate")
        print("---------------------------------------------------------------------")
        for mlist in movieList:
            # เว้นช่องไฟเพื่อความสวยงาม
            print(f"{mlist['id']:>2}  | {mlist['name']:<25} | {mlist['type']:<15} | {mlist['price']:<8} | {mlist['minAge']}")
        print("\n")

    elif sel == 2:
        selected = movieChoice()  #รบค่าจาก func และทำตามขั้นตอนต่อ <เก็บข้อมูลหนังที่เลือกมาจากรายการใน Movielist>
        if not selected:
            print("Invalid movie selection.")
            continue

        age = inputAge()
        if age is None:
            print("Invalid age.")
            continue
        
        st = soundtrack()
        if st is None:
            print("invalid soundtrack")
            continue

        if selected['minAge'] == 'G' or age >= selected['minAge']:
            final_price = selected['price']
            if selected['type'] == "Fantasy":
                final_price += 50
        
            print(f"-----------------------------------------------------------------------\n[i] You can watch '{selected['name']}'")
            choice.append({
                "movie": selected['name'],
                "age": age,
                "price": final_price,
                "st": st
            })

        else:
            print(f"[X] Sorry, you're too young for '{selected['name']}' (Min age: {selected['minAge']})\n")


        print("\nYour current choices:")
        for c in choice:
            if selected['type'] == "Fantasy":
                print(f"- {c['movie']} (Price: {c['price']} Bath), Sountrack: {c['st']}\n[i] Included add 50 bath charge for Fantasy movie (from {selected['price']} bath)\n\nEnjoy your movie <3")
            else:
                print(f"- {c['movie']} (Price: {c['price']} Bath), Sountrack: {c['st']}\n\nEnjoy your movie <3")
        break

    else:
        print("Unknown selection Cancelled!")
        break

