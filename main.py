import database as db
from Requirement import validation
from Requirement import logic as l
from prettytable import PrettyTable
import random
import maskpass
hi="-"
j = "*"


# developer Raj Bhoir 
# Modify food Add validation for old food name present or not



print("<     WELCOME TO FOOD ORDERING SYSTEM     >\n".center(160))
while True:

    print("\n1 - Create New Customer Account\n2 - Login Customer Account\n3 - Admin Login\n4 - View menu\n5 - Exit\n6 - Delivery Man login")
    ch = input("\nEnter Your choice:")
#================================================================================================================
    #user new account
    if ch == "1":
        while True:
            name = input ("Enter Your Name:")
            if validation.NameValidation(name):
                break
            else:
                print("Invalid name")
                
        while True:
            contact = input ("Enter Your Contact Number:")
            if validation.ContactValidation(contact):
                break
            else:
                print("invalid contact Number")

        while True:
            email = input("Enter Your email:")
            if validation.EmailValidation(email):
                break
            else:
                print("Invalid Email")
        while True:
            address = input("Enter Your Address:")     #<--------------- validation required
            break
        
        while True:
            pass1 = input("Enter Your Password:")
            pass2 = input("Confirm Your Password:")
            print()
            if validation.PasswordValidation(pass1,pass2):
                
                break
            else:
                print(f"Enter correct password {pass1} and {pass2}")
                
              
        x = db.add_user(name,email,contact,address,pass2)
        print(x)


            
#================================================================================================================    #User Section
    elif ch == "2":
        
        email1 = input ("\nEnter Your Email:")
        password = maskpass.askpass()                               #hiding password using maskpass
        x = db.User_Login(email1,password)  
        if x != True:
            print("Invalid Email-Id Or Password\n")

        else:
            print("login succesfull\n")
            while True:
                print("\n1 -> Show Food Menu\n2 -> Order History \n3 -> Cancel order\n4 -> Log Out\n")
                ch = input("Enter Your Choice:")

                #SHOW MENU
                if ch == "1":
                   
                    x = db.Show_Item()#show menu
                    #print(x)
                    print("\n")
                    order = input("FOR ORDER PRESS 1:")

                    #order Food
                    if order == "1":
                        sum=0
                        st=[]
                        q=[] 
                        
                        while True:
                            f=int(input("ENTER HOW MANY FOOD YOU WANT TO ORDER:"))
                            if f > 20:
                                print("\nwe dosen't allow order food more than 20\n")
                            else:
                                break
                        print()
                        n=f
                        

                        i = 0
                        while i < n:
                            ele = int (input("Enter Item Code OF FOOD:"))

                            f = db.Find_order_id(ele)
                            if f == None:
                                print("Invalid code")
                                n= n-1
                                i = i - 1
                                

                            
                            
                            else:
                                quntity = int (input("Enter Quantity OF FOOD:"))
                                print()
                                if quntity > 100:
                                    print("Please Enter Quantity less than 100")
                                else:
                                    q.append(quntity)# <-----------quentity of food wrt selected food
                                    st.append(ele)
                                a = db.show_order(st)
                                all = list(a)
                                i = i + 1

                        #Total calculation of order
                        x = db.search_item(st)#                         <----------------Return price of food
                        s=list(x)
                        result = []
                        for i,i2 in zip(s,q):
                            result.append(i*i2)
                        bill=0
                        for i in range(0,len(result)):
                            bill = bill + result[i]
                        

                        #showing selected foods
                        if all == "":
                            print("Not Found")
                        else:
                            print("<---------- YOUR ORDER FOOD ----------->")
                            items=[]
                            myTable1 = PrettyTable(["FOOD"])
                            for i in all:
                                for j in i:
                                    myTable1.add_row([j])
                        
                                    items.append(j)
                            print(myTable1)
                            m = l.listToString(items)
                        
                        

                        
                        #showing total bill amount
                        print("\n--- Your Total bill Amount:",bill,"---\n")

                                            
                        #getting leatest contact number
                        
                        while True:
                            cont=input("Enter Your Contact NUMber:")
                            if validation.ContactValidation(cont):
                                break
                            else:
                                print("Invalid contact Number\n")
                                

                        q_string=map(str,q)
                        con = []
                        for i in q_string:
                            con.append(i)
                        con1 = l.listToString(con)
                        add = db.find_address(email1)
                        
                        
                        #OTP
                        otp = random.randint(1000,9999)
                        print("Your Food Order OTP:",otp)
                        #Data insert
                        x = db.add_history(m,con1,bill,email1,cont,otp,add)
                        print(x)
                        
                    
                    elif order == "":
                        pass

            
                    else:
                        print("Not Ordering")
                        continue


                #ORDER HISTORY             
                elif ch == "2":
                        x = db.order_h(email1)
                        print("---- Your Orders ----")
                        myTable = PrettyTable(["ID", "FOOD","quentity","BILL","Email","contact","Status","Entry","OTP"])
                        for i in x:
                            myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
                        print(myTable,"\n")

                
                #Cancel order
                elif ch == "3":
                    order_id = int(input ("Enter order ID to Cancel Order:"))
                    m = db.Find_order_id_for_cancel(order_id,email1)
                    if m == None:
                        print("Order ID Not Found")
                    else:

                        x = db.Cancle_Order(order_id,email1)
                        print(x)

                 #LOGOUT   
                elif ch == "4":
                    print("Log Out \nThank You Visit Again...\n")

                    break

                else:
                    print(j*5,"Wrong Choice",j*5,"\n")

        
            
            
    
    
#===================================<  Admin Section  >=======================================#
    
    elif ch == "3":

        admin = input("Enter Your Admin id:")
        admin_password = maskpass.askpass()

        log = db.admin_login(admin,admin_password)
        if log==True:
                print("login successfully\n")
        else:
            print("Invalid Email-Id Or Password")

        #ADMIN 
        while log==True:
            print("\n1 -> Add Food\n2 -> Remove Food\n3 -> Modify Food\n4 -> View orders\n5 -> view Menu\n6 -> confirm order\n7 -> Delivery Person\n8 -> Logout\n")
            ch = input("Enter Your Choice -> ")
            print()


            #ADD FOOD
            if ch == "1":
                name=input("Enter Item Name -> ")
                try:
                    price =int( input("Enter Item Price -> "))
                    if db.check_price(price):
                        print("Price Exceed")
                    else:
                        ftype = input("Enter Type of food ->")
                        x = db.Add_Item(name,price,ftype)
                        print(x)
                except:
                    print("Invalid Details")


            #REMOVE FOOD
            elif ch == "2":
                name = input("Enter name to remove item:")
                check = db.search_food(name)
                if check == True:
                    print("Food Not Present In Menu")
                else:
                    x = db.remove_item(name)
                    print(x)


            #UPDATE FOOD
            elif ch == "3":
                
                old_name = input("Enter old Food Name:")
                #check food presence
                x = db.search_food(old_name)
                
                if x == True:
                    print("Food Not Present In Menu")
                else:
                    new_name = input("Enter New Name FOOD:")
                    rs =int(input("Enter to update Price:"))
                    if db.check_price(rs):
                        print("Price Exceed")
                    else:
                        x = db.update_item(rs,old_name,new_name)


            #SHOW ORDERS
            elif ch == "4":
                x = db.show_orders()
                print(hi * 55 ," YOUR ORDERS ",hi*55)
                myTable = PrettyTable(["ID", "FOOD","quentity","BILL","Email","contact","Status","Time","Location","D Person"])
                #x5 = db.view_profile()
                for j in x:
                    for i in j:
                        myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[9],i[10]])
                print(myTable)

                 
            #SHOW FOODS
            elif ch == "5":
                db.Show_Item()


            #confirm order
            elif ch == "6":
                order_id1 = int(input("Enter Order ID:"))
                person_id = int(input("Enter Person ID:"))

                x = db.confirm_order_admin(order_id1,person_id)
                if x == None:
                    print("Delivery Man Not Found")
                else:
                    print("You Forwarded Order To:",x[0])



            #LOG OUT
            elif ch == "7":

                while True:
                    print("\n1 -> Add Person\n2 -> Remove Person\n3 -> View Persons\n4 -> Back To Main Menu\n")
                    ch =input("Enter Choice:")
                    

                    if ch == '1':
                        while True:
                            dname = input("Enter Delivery Person Name:")
                            if validation.NameValidation(dname):
                                break
                            else:
                                print("Invalid Name")
                                
                        while True:
                            dcontact =(input("Enter Delivery Person Contact:"))
                            if validation.ContactValidation(dcontact):
                                break
                            else:
                                print("\nInvalid Contact\n")

                        while True:
                            d1password = input("Enter Password:")
                            d2password = input("Confrim Password:")
                            if validation.PasswordValidation(d1password,d2password):
                                break
                            else:
                                print("Invalid Password")
                                
                        if db.add_dperson(dname,dcontact,d2password):
                            print("\nAdd Successfully")


                    elif ch == '2':
                        id = int(input("Enter Delivery Person Id:"))
                        print(db.remove_dperson(id))


                    elif ch == '3':
                        x = db.view_dperson()
                        dtabel = PrettyTable(["ID","Name","Contact","Password"])
                        for i in x:
                            dtabel.add_row([i[0],i[1],i[2],i[3]])
                        print(dtabel,'\n')


                    elif ch == '4':
                        print("\nBack To Main Menu")
                        break

                    else:
                        print("\nInvalid Input")
                

            elif ch == "8":
                print("LOG OUT...\n")
                log = False

            #wrong input
            else:
                print(j*5,"Invalid Input",j*5)

            
    elif ch == "4":
        db.Show_Item()
        continue

    elif ch == "6":
        while True:
        #id = (int(input("\nEnter Your ID:")))#  validation required
        
        
            id = (int(input("\nEnter Your ID:")))#  validation required
            x9 = db.view_profile(id)
            if x9 == None:
                print("Invalid ID")

            elif x9[0] == id:
                break
        
            else:
                print("Invalid Input")            
                
                
        password1 = maskpass.askpass()   #validation
        dlog = db.dp_login(id,password1)
        if dlog == True:
            print('')
            x6 = db.view_profile(id)
            print("<----- Welcome",x6[1]," ----->")
        else:
            print("Invalid ID or password")
        
        while dlog == True:


            print("\n1 -> Place Order\n2 -> View Orders\n3 -> View Profile\n4 -> Log Out\n")
            ch = input("Enter Your Choice:")
            print()

            #place order
            if ch == "1":
                while True:
                    
                        order_id1 = int(input("Enter Order ID:"))
                        x = db.Find_order_id_for_place(id,order_id1)
                        if x != None:
                            pass
                        else:
                           print("Enter Correct Order ID")
                           break
                
                        otp1 = int(input("Enter OTP:"))
                        x = db.Confirm_Order(order_id1,otp1)
                        print(x)
                        break
                    

            #view order
            elif ch == "2":
                x = db.view_order(id)
                viewtable=PrettyTable(["ID","Food","Bill","Contact","status","Location","Email"])
                #for i in x:
                for j in x:
                    viewtable.add_row([j[0],j[1],j[3],j[5],j[6],j[9],j[4]])
                print(viewtable)

            #view Profile
            elif ch == "3":
                x = db.view_profile(id)
                dptable=PrettyTable(["ID","Name","Contact","Password"])
                dptable.add_row([x[0],x[1],x[2],x[3]])
                print("<-------------- Profile -------------->")
                print(dptable)

            #Log Out
            elif ch == "4":
                print("Log out")
                break


            else:
                print("invalid Input")
    
            

    elif ch == "5":
        print("Thank You")
        break






    #exit
    else:
        print("\nInvalid Input")
        continue
        