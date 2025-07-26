movieList = [
    {"id": 1, "name": "Skibidi Toliet", "price": 30, "minAge": 6, "type": "Fantasy"},
    {"id": 2, "name": "Badass Basic Programing", "price": 40, "minAge": 15, "type": "Documentary"},
    {"id": 3, "name": "Robood The Movie", "price": 35, "minAge": 13, "type": "Horror"},
    {"id": 4, "name": "Supersigma", "price": 45, "minAge": 18,  "type": "Action"},
    {"id": 5, "name": "IT Startpack IT31", "price": 30, "minAge": 15,  "type": "Scifi"},
    {"id": 6, "name": "Beasts and the frog", "price": 45, "minAge": 16,  "type": "Romantic"},
    {"id": 7, "name": "Yohane the Parhelion", "price": 50, "minAge": 13,  "type": "Fantasy"},
]


# def movieChoice():
#     movie = int(input("Choose Movie to watching\n>> "))
#     if movie == 1:
#         return(movieList[0])
#     if movie == 2:
#         return(movieList[1])
#     if movie == 3:
#         return(movieList[2])
#     if movie == 4:
#         return(movieList[3])
#     if movie == 5:
#         return (movieList[4])
    

choice = []
# นำเลขหนังที่เลือก จาก movie(int)มาลบกับเลข index ของ movieList ทีแสดงข้อมูลหนังทั้งหมด เพื่อเลือกหนังที่ถูกต้อง
def movieChoice():
    movie = int(input("Choose Movie to watching\n>> "))
    if 1 <= movie <= 7:
        return movieList[movie - 1]
    return None       

def soundtrack():
    st = int(input("Select your sountrack:\n[1] ภาษาไทย (TH)\n[2] English (EN)\n[3] 日本語 (JP)\n>> "))
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
        print("\nNo. | Name                      | Type            | Price")
        print("------------------------------------------------------------")
        for mlist in movieList:
            # เว้นช่องไฟเพื่อความสวยงาม
            print(f"{mlist['id']:>2}  | {mlist['name']:<25} | {mlist['type']:<15} | {mlist['price']}")
        print("\n")

    elif sel == 2:
        selected = movieChoice()
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

        if age >= selected['minAge']:
            final_price = selected['price']
            if selected['type'] == "Fantasy":
                final_price += 50
        
            print(f"[i] You can watch '{selected['name']}'")
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
                print(f"- {c['movie']} (Price: {c['price']}), Sountrack: {c['st']}\n[i] Included add 50 bath charge for Fantasy movie\n\nEnjoy your movie <3")
            else:
                print(f"- {c['movie']} (Price: {c['price']}), Sountrack: {c['st']}\n\nEnjoy your movie <3")
        break 
    else:
        print("Unknown selection Cancelled!")
        break

