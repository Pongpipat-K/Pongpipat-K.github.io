price=[]
menu=[]
option_p = ["ชำระเงิน []","กลับเมนูหลัก []"]
def option ():
    option_m = ["อาหารจานหลัก ","ของทานเล่น ","เครื่องดื่ม ","ของหวาน","ชำระเงิน","ออกจากโปรแกรม "]
    print("Select Option")
    for i in range(len(option_m)):
        print (i+1, option_m[i])
    print("------------------------------------------")

def main_cause () :
    Main_cause = {"สเต็กเนื้อออสเตรเลีย" : 350 ,"นาโช่ อบชีส" : 150,"สเต๊กซี่โครงแกะ" : 379,"อกเป็ดราดซอสส้ม" : 274,"โทมาฮอว์ค" : 400,"กุ้งมังกรทอดพริกเกลือ" : 1200,}
    i = 1
    for name in Main_cause:
        print(i, name, Main_cause[name],"บาท")
        i +=1
    while True :
        ls = []
        for name in Main_cause.keys() :
            ls.append(name)
        choose=int(input("โปรดเลือกเมนู (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.append(ls[choose-1])
            price.append(Main_cause[ls[choose-1]])
    ch=str(input("ต้องการเมนูอื่นเพิ่มเติม ? (Y/N) :"))
    if ch == "Y" or ch =="y" :
        main_cause()
        return 1
    elif ch == "n" or ch == "N" :
        return 0
    else :
        print("\n\n\n----------------------------------------\nโปรดระบุให้ถูกต้อง\n----------------------------------------")
        main_cause()
    print("------------------------------------------")
def snack() :
    Snack={"นักเก็ต":59,"เฟรนช์ฟรายส์":49,"ครัวซองต์":59,"มันอบเนยชีส":79,"ซีซ่าร์สลัด":169,"เบคอนม้วนไส้กรอกปิ้งเครื่องลาบ":69,"สลัดแซลมอน":89,"ไก่ป็อป":69}
    ls = []
    i=1
    for name in Snack.keys() :
            print(i,name,Snack[name],"บาท")
            ls.append(name)
            i+=1
    while True :
        choose=int(input("โปรดเลือกเมนู (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.append(ls[choose-1])
            price.append(Snack[ls[choose-1]])
    ch=str(input("ต้องการเมนูอื่นเพิ่มเติม ? (Y/N) :"))
    if ch == "Y" or ch =="y" :
        snack()
        return 1
    elif ch == "n" or ch == "N" :
        return 0 
    else :
        print("\n\n\n----------------------------------------\nโปรดระบุให้ถูกต้อง\n----------------------------------------")
        snack()   
def snk():
    dessert = {   "chocolate cake":40,
            "banana Cake":45,
            "pancake":35,
            "cookie":30,
            "muffin":25,
            "brownie":25,
            "waffle":25,
            "toast":35,
        } 
    i = 1
    for name in dessert :
        print(i,name,":",dessert[name],"บาท")
        i += 1
    while True :
        ls = []
        for name in dessert.keys() :
            ls.append(name)
        choose=int(input("โปรดเลือกเมนู (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.append(ls[choose-1])
            price.append(dessert[ls[choose-1]])
    ch=str(input("ต้องการเมนูอื่นเพิ่มเติม ? (Y/N) :"))
    if ch == "Y" or ch =="y" :
        snk()
        return 1
    elif ch == "n" or ch == "N" :
        return 0
    else :
        print("\n\n\n----------------------------------------\nโปรดระบุให้ถูกต้อง\n----------------------------------------")
        snk()
    print("------------------------------------------")
   
def show_cof():
    coffe = {   "latte":150,
            "frappuccino":125,
            "macchiato":160,
            "espresso":100,
            "cafe mocha":100,
            "cafe cahi":95
        } 

    i = 1
    for cof_com in coffe :
        print(i,cof_com,":",coffe[cof_com],"บาท")
        i += 1
    while True :
        ls = []
        for name in coffe.keys() :
            ls.append(name)
        choose=int(input("โปรดเลือกเมนู (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.append(ls[choose-1])
            price.append(coffe[ls[choose-1]])
    ch=str(input("ต้องการเมนูอื่นเพิ่มเติม ? (Y/N) :"))
    if ch == "Y" or ch =="y" :
        show_cof()
        return 1
    elif ch == "n" or ch == "N" :
        return 0   
    else :
        print("\n\n\n----------------------------------------\nโปรดระบุให้ถูกต้อง\n----------------------------------------")
        show_cof() 
def show_t():
    tea = {   "macha":80,
            "oofong":85,
            "berry bomb":90,
            "thai tea":80,
            "cocoa caramel":85
        } 

    i = 1
    for t_com in tea :
        print(i,t_com,tea[t_com],"บาท")
        i += 1     
    while True :
        ls = []
        for name in tea.keys() :
            ls.append(name)
        choose=int(input("โปรดเลือกเมนู (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.append(ls[choose-1])
            price.append(tea[ls[choose-1]])
    ch=str(input("ต้องการเมนูอื่นเพิ่มเติม ? (Y/N) :"))
    if ch == "Y" or ch =="y" :
        show_t()
        return 1
    elif ch == "n" or ch == "N" :
        return 0
    else :
        print("\n\n\n----------------------------------------\nโปรดระบุให้ถูกต้อง\n----------------------------------------")
        show_t()   
def show_j():
    juice = {   "mango sahke":85,
            "banana shake":85,
            "orange shake":85,
            "grape shake":85,
            "guava shake":85,
            "kiwi shake":85
        } 

    i = 1
    for j_com in juice :
        print(i,j_com,juice[j_com],"บาท")
        i += 1
    while True :
        ls = []
        for name in juice.keys() :
            ls.append(name)
        choose=int(input("โปรดเลือกเมนู (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.append(ls[choose-1])
            price.append(juice[ls[choose-1]])
    ch=str(input("ต้องการเมนูอื่นเพิ่มเติม ? (Y/N) :"))
    if ch == "Y" or ch =="y" :
        show_j()
        return 1
    elif ch == "n" or ch == "N" :
        return 0
    else :
        print("\n\n\n----------------------------------------\nโปรดระบุให้ถูกต้อง\n----------------------------------------")
        show_j()
def payment() :
    total=0
    for i in range(len(menu)) :
        print(i+1,menu[i],price[i],"บาท")
        total+=price[i]
    print("ผลรวม :",total,"บาท")
    while True :
        choose=int(input("โปรดเลิอกเมนูที่ต้องการลบ (0 = เพื่อยกเลิกการสั่ง) : "))
        if choose == 0 :
            break
        else :
            menu.pop(choose-1)
            price.pop(choose-1)
        total=0
        for i in range(len(menu)) :
            print(i+1,menu[i],price[i],"บาท")
            total+=price[i]
        print("ผลรวม :",total,"บาท")   
    total=0
    for i in range(len(menu)) :
        print(i+1,menu[i],price[i],"บาท")
        total+=price[i]
    print("ผลรวม :",total,"บาท")    
    money = int(input("โปรดระบุยอดที่ต้องการชำระ:"))
    while total > money :
        money = int(input("ยอดชำระไม่เพียงพอกรุณาระบุใหม่:"))
    submit = money-total
    print(f"เงินทอน={submit}บาท ขอบคุณที่ใช้บริการ :)")
        

    

 #main program
#option ()
while True :
    try :
            option()
            num = int(input("Enter option: "))
            if num == 1 :
                main_cause ()
            elif num == 2  :
                snack()
            elif num == 3 :
                print("1.Coffee\n2.Tea\n3.Juice shake")
                d=int(input("โปรดเลือกเมนูน้ำ"))
                if d == 1 :
                    show_cof()
                elif d == 2 :
                    show_t()
                elif d == 3 :
                    show_j()
            elif num == 4 :
                snk()
            elif num == 5 :
                payment()
                break
            elif num == 6 :
                print("ขอบคุณที่ใช้บริการ :)")
                break
            else :
                print("โปรดเลือกออฟชั่นตามที่กำหนดให้")
                pass
    except ValueError :
            print("\n\n--------------------------------\nโปรดระบุเป็นตัวเลขเท่านั้น\n--------------------------------")
#select_option ()
