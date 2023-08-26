# database
import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable

try:
    conn=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="Raj@1234"
                                    )
    
except Error as e:
    print("Error:",e)

cursor = conn.cursor()

#CREATING TABLE FOR USER INFORMATION        

try:
    sql = '''create database if not exists food'''
    cursor.execute(sql)
    sql1 = '''use food'''
    cursor.execute(sql1)
    conn.commit()
except Error as e:
    print("Error:",e)


try:

    sql="""create table if not exists user_info(
        id int auto_increment primary key,
        name varchar(20) not null,
        email varchar(50) not null unique,
        contact bigint not null unique,
        address varchar(50) not null,
        password varchar(15)
        )"""
    cursor.execute(sql)
    conn.commit()
except Error as e:
    print("Error",e)

#CREATING TABLE FOR ADMIN LOGIN                          2
try:
    sql='''create table if not exists admin(admin_id varchar(20) unique not null,
    admin_password varchar(20) not null)'''
    cursor.execute(sql)
    conn.commit()
except Error as e:
    print("error",e)


#CREATING TABLE FOR MENU CARD                              3
try:
    query = '''create table if not exists menu(id int auto_increment primary key ,
      Item_Name varchar(100)
        unique not null ,
        Price int not null,
        Food_Type varchar(20)) ;'''
    cursor.execute(query)

except Error as e:
    print("error",e)

try:
    sql12 = '''create table if not exists DP(id int auto_increment primary key,name varchar(20) not null,contact bigint null,d_password varchar(8) not null)'''
    cursor.execute(sql12)
    conn.commit()

except:
    print("NOT OK")


#CREATING TABLE FOR ORDER HISTORY                           4
try:
    sql = '''create table if not exists order_history(id int auto_increment not null primary key,
    food_name varchar(100),
    quentity varchar(50) not null,
    total_bill int not null,
    email_id varchar(40) not null,
    contact bigint not null,
    status varchar(20) null default "Pending",
    entry datetime null,
    otp int null,
    Location varchar(50) not null,
    dperson int null
    
   

    )'''
    # FOREIGN KEY(dperson) REFERENCES dp(id)
    
    cursor.execute(sql)
    



except Error as e:
    print("Errro",e)

#create table for delivery Person







#===========< User Section >==========================================================================


def add_user(name,email,contact,address,pass2):
    try:
        
        sql ='''insert into user_info(name,email,contact,address,password) values (%s,%s,%s,%s,%s)'''
        
        cursor.execute(sql,(name,email,contact,address,pass2))
        conn.commit()
        return "<---------- Registration successfull ---------->"
    except:
        return "not register"
    


def User_Login(email,password):
    sql='''select email,password from user_info where email = %s && password = %s;'''
    cursor.execute(sql,(email,password))
    s=cursor.fetchone()

    try :
        if s[0] == email:
            if s[1] == password :
                return True
        
    except :
        return "Invalid Email-Id Or Password"
    
#delete account for admin
def delete_account(Email):
    sql = '''delete from User_Info where email=%s'''
    data = (Email,)
    cursor.execute(sql,data)
    conn.commit()
    return False




    
#========< Admin Section >===========================================================================  


def admin_login(admin_id,admin_password):
    sql='''select admin_id,admin_password from admin where admin_id = %s && admin_password = %s;'''
    cursor.execute(sql,(admin_id,admin_password))
    s=cursor.fetchone()
    try :
        if s[0] == admin_id:
            if s[1] == admin_password :
                return True
        
    except :
        return "Invalid Id Or Password"
    

    
def Add_Item(name,price,ftype):
    try:
        sql = '''insert into menu(Item_Name,Price,Food_Type) values(%s,%s,%s)'''
        cursor.execute(sql,(name,price,ftype))
        conn.commit()
        return "\nItem inserted succcesfullly\n"
    except:
        return "\nInvalid Details or Food Present In Menu\n"
    

def remove_item(name):
    #validation required
    try:
        sql = '''delete from menu where Item_name=%s'''
        data = (name,)
        cursor.execute(sql,data)
        conn.commit()
    
        return f"{name} Remove successfully\n"
    except:
        return"\n food not deleted\n"
    

def update_item(rs,oldname,newname):
    try:
        sql = '''update menu set Item_name=%s,Price=%s where Item_name=%s '''
        cursor.execute(sql,(newname,rs,oldname))
        conn.commit()
        print("FOOD Updated\n ")
        Show_Item()
    except:
        print("Food not Updated")


def Show_Item():
    sql = '''select * from menu'''
    cursor.execute(sql)
    data = cursor.fetchall()
    myTable = PrettyTable(["CODE", "FOOD","PRICE","FOOD TYPE"])
    for i in data:
        myTable.add_row([i[0],i[1],i[2],i[3]])
    print(myTable)

        
def search_contact(email):
    try:
        sql = '''select contact from user_info where email='%s';'''
        data = (email,)
        x = cursor.execute(sql,data)
        return x
    except:
        print("Invalid Email")

def search_food(food_name):
    sql='''select Item_Name from menu where Item_Name=%s'''
    cursor.execute(sql,(food_name,))
    x = cursor.fetchone()
    
    if x == None:
        return True
    else:
        return False
    
def check_price(price):
    if price < 2000:
        return False
    else:
        return True
    
'''create table if not exists DP(id int auto_increment Primary key,name varchar(20) not null,contact bigint null,d_password varchar(8) not null)'''
def add_dperson(name,contact,d_password):
    try:
        sql = '''insert into DP(name,contact,d_password) values(%s,%s,%s)'''
        cursor.execute(sql,(name,contact,d_password))
        conn.commit()
        return True
    except:
        print("Person alerday exists")

def remove_dperson(id):
    try:
        sql = '''select id from dp where id=%s'''
        cursor.execute(sql,(id,))
        x = cursor.fetchone()
        if x != None:
            for i in x:
    
                if i == id:
                    try:
                        sql0 = '''delete from dp where id=%s'''
                        cursor.execute(sql0,(id,))
                        conn.commit()
                        return 'Person Remove Successfully\n'
                    except:
                        ("Error")
                
        else:
            return "\nID Not Found"
                
    except:
        return "ID Not Found"

def view_dperson():
    try:
        sql = '''select * from dp'''
        cursor.execute(sql)
        x = cursor.fetchall()
        return x
    
    except Error as e:
        print('Error:',e)




    

#==================< ORDER SECTION >===================#



        
def show_order(st):
    try:
        for i in st:
            sql = '''select item_name from menu where id=%s'''
            data = (i,)
            cursor.execute(sql,data)
            x = cursor.fetchone()
        
            yield x
    except:
        print("----Invalid Item Code----")


def add_history(food_name,quentity,bill,email,contact,otp,add):
    try:
        sql = 'insert into order_history(food_name,quentity,total_bill,email_id,contact,entry,otp,Location) values(%s,%s,%s,%s,%s,now(),%s,%s);'
        data = (food_name,quentity,bill,email,contact,otp,add)
        cursor.execute(sql,data)
        conn.commit()
        return "order Get successfully"
    except Error as e:
        print("Error:",e)


def show_orders():
    try:
        sql='''select * from order_history'''
        cursor.execute(sql)
        x=cursor.fetchall()
        yield x
    except Error as e:
        print("Error:",e)


def order_h(email):
    sql='''select * from order_history where  email_id=%s'''
    data = (email,)
    cursor.execute(sql,data)
    x = cursor.fetchall()
    return x


def Cancle_Order(id,email):
    try:
        sql = '''select id,email_id,status from order_history where id=%s && email_id=%s;'''
        data =(id,email)
        cursor.execute(sql,data)
        x = cursor.fetchone()
        
        try:
            if x[0] == id:
                if x[1] == email:
                    if x[2] == "Pending" or x[2] == "In Process":
                        
                        try:
                            sql1 = '''delete from order_history where id=%s'''
                            cursor.execute(sql1,(id,))
                            conn.commit()
                            return "< - - Order Cancelled Successfully - - >"
                        except Error as e:
                            print("Error:",e)
                    
                    else:
                        return "Your Order Aleredy Placed"
                    
            else:
                return  "Enter Your order ID"
        except:
            return "\nEnter correct Order ID"
    except Error as e:
        print(e)
#&& otp=%s

def confirm_order_admin(order_id,person_id):
    try:
        sql = '''select id,status from order_history where id=%s'''
        cursor.execute(sql,(order_id,))
        x = cursor.fetchone()
        if x == None:
            print("Invalid Order ID")
        else:
            try:
                if x[0] == order_id:
                    if x[1] == 'Pending':
                        try:
                            try:
                                sql3 = '''select name from dp where id=%s'''
                                cursor.execute(sql3,(person_id,))
                                z = cursor.fetchone()
                                conn.commit()
                                if z != None:       
                                    sql1 = '''update order_history set dperson=%s where id=%s'''
                                    cursor.execute(sql1,(person_id,order_id))
                                    conn.commit()

                                    sql2 = '''update order_history set status="In Process" where id=%s'''
                                    cursor.execute(sql2,(order_id,))
                                    return z
                                else:
                                    return z
                            except:
                                pass

                        #sql3 = '''select name from dp where id=%s'''
                       # cursor.execute(sql3,(person_id,))
                        #z = cursor.fetchone()
                        #conn.commit()
                            return z       
                        except Error as e:
                            print(e)
                    else:
                        return "< Order Alerday forworded >"
                
            except Error as e:
                print(e)

    
    except Error as e:
        print(e)







def Confirm_Order(order_id1,otp1):
    try:
        sql = '''select id,otp,status from order_history where id=%s && otp=%s;'''
        cursor.execute(sql,(order_id1,otp1))
        x1 = cursor.fetchone()
        if x1 == None:
            return '\nIncorrect OTP'
        else:
            try:
                if x1[0] == order_id1:
                    if x1[1] == otp1:
                        if x1[2] == "In Process":
                            try:
                                sql1 = '''update order_history set status="Deliverd" where id=%s'''
                                cursor.execute(sql1,(order_id1,))
                                conn.commit()
                                return "Order Placed successfull"
                            except:
                                return "database Problem" 
                        else:
                            return "Order Alerady Placed\n"
                    else:
                        return "Incorrect OTP"
                else:
                    return "Order Alerady Placed\n"
            except:
                return "Invalid Order-id or OTP\n"
    except:
        return "INVALID ORDER ID\n"


#----------------------------------------------------------------------------------------------------------------
def Find_order_id(id):
    try:
        sql = 'select id from menu where id like %s'
        cursor.execute(sql,(id,))
        x = cursor.fetchone()
        return x
    except:
        print("NOT FOUND")

    
def Find_order_id_for_cancel(id,email):
    try:
        sql = 'select id from order_history where email_id=%s and id like %s'
        cursor.execute(sql,(email,id))
        x = cursor.fetchone()
        return x
    except:
        print("NOT FOUND")


def find_address(Email):
    try:
        sql = '''select address from user_info where email=%s'''
        cursor.execute(sql,(Email,))
        x = cursor.fetchone()
        
        for i in x:
            return i
        
    except:
        print("Error")

def search_item(st):
    ls=[]
    for i in st:
        sql = '''select * from menu where id=%s'''
        data = (i,)
        cursor.execute(sql,data)
        x = cursor.fetchone()
        yield x[2]




        
#=========================================< Dilivery Person >==========================================

def dp_login(id,pass1):
    sql='''select id,d_password from dp where id = %s && d_password = %s;'''
    cursor.execute(sql,(id,pass1))
    s=cursor.fetchone()
    try :
        if s[0] == id:
            if s[1] == pass1 :
                return True
        
    except :
        return False

def view_order(id):
    sql = '''select * from order_history where dperson=%s'''
    cursor.execute(sql,(id,))
    x = cursor.fetchall()
    return x

def view_profile(id):
    sql = '''select * from dp where id=%s'''
    cursor.execute(sql,(id,))
    x=cursor.fetchone()
    return x

def Find_order_id_for_place(id,order_id):
    try:
        sql = 'select id from order_history where dperson like %s && id=%s'
        cursor.execute(sql,(id,order_id))
        x = cursor.fetchone()
        return x
    except:
        print("NOT FOUND")


#x = find_order_id_for_place(12)
#print(x)

def insert_menu_items():
    sql = '''insert into menu(Item_Name,Price,Food_Type) values('Paneer Tikka',200,'Veg'),('Paneer Malai Tikka',220,'Veg'),('Paneer Garlic Tikka',225,'Veg'),('Tandoori Mashroom',190,'Veg'),('Paneer Tikka Roll',160,'Veg'),('Fresh Veggie Pizza',160,'Veg'),('Peppy Paneer Pizza',150,'Veg'),('Chicken Dominator Pizza',205,'Non-Veg'),('Checken Pepperoni Pizza',260,'Non-Veg'),('Creamy Pasta Pizza',120,'Non-Veg'),('Chiken Tikka',230,'Non-Veg'),('Mutton Tikka',360,'Non-Veg'),('Veg Loaded Pizza',140,'Veg'),('Veg Zinger Burger',80,'Veg'),('Water Bottle 1L',20,'Drink'),('Soda Bottle',25,'Drink'),('Red Bull',110,'Drink'),('Green Salad',80,'Veg');'''
    cursor.execute(sql)
    conn.commit()
    return "Inserted"
   
def insert_admin():
    sql = '''insert into admin values('admin','admin')'''
    cursor.execute(sql)
    conn.commit()
    return "Admin"

#x=insert_menu_items()
#insert_admin()