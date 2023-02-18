import random
import mysql.connector
import pickle
import csv
import datetime
from urllib import request
import webbrowser
import smtplib

def check(id,password):
    f=open("existingcustomers.dat","ab+")
    f.seek(0,0)
    
    record=pickle.load(f)
    if record[id]==password:
        return "Login Successful!"
    elif record[id]!=password:
        passwor=input("Incorrect!! enter correct password:  ")
        check(id,passwor)
        
    menu()
    f.close()

def signup():
    f=open("existingcustomers.dat","ab+")
    f.seek(0,0)
    record2=pickle.load(f)
    name=input("Enter name:  ")
       
    DOB=input("Enter DOB in the format ‘yyyy-mm-dd’ :  ")
    new_id=random.randint(100,200000)
    if new_id in record2:
        new_id=random.randint(100,200000)
    f.close()
    while True:
        pw=input("Enter a password over 5 characters with one special case character:  ")
        pw2=input("Re-enter password:  ")
       
        if pw==pw2:
            ft=open("existingcustomers.dat","wb+")
            
            record2[new_id]=pw
            
            print("Your customer id is:  ",   new_id)
            ft.seek(0,0)
            pickle.dump(record2,ft)
            ft.seek(0,0)
            
            
            ft.close()
            print()
            print("SIGNUP SUCCESSFUL")
            break
    
        else:
           print()
           print("Wrong password entered please enter again:  ")
           continue
    mydb=mysql.connector.connect(host="localhost",username="root",password="sairam123",database="MedStat")
    mycursor=mydb.cursor()
    currentdate=datetime.date.today()
    sql="insert into customers values(%s,%s,%s,%s)"
    val=[(new_id,name,currentdate,DOB)]
    mycursor.executemany(sql,val)
    mydb.commit()
    file1=open("points and rewards.dat","rb+")
    data=pickle.load(file1)
    dic={}
    for a in data:
        dic[a]=data[a]
    
    dic[new_id]=0
    file1.seek(0,0)
    pickle.dump(dic,file1)
    file1.flush()
    file1.close()
    
    

   
        
    menu()
def menu():
    print()
    print()
    print()
    customer_id=int(input("Enter your customer ID to proceed:  "))
    print()
    while True:
        print("""                        Enter 1 to place an order
                        Enter 2 to cancel order
                        Enter 3 to view products and prices
                        Enter 4 to view the MedStat Website
                        Enter 5 to view points
                        Enter 6 to give FeedBack
                        Enter 7 to logout""")
        print()
       
        input2=int(input("Enter your choice: "))
        print()
        print()
        if input2==7:
            print()
            print("THANK YOU FOR SHOPPING WITH MEDSTAT!")
            break
        elif input2==6:
##            feed=open("Feedback.csv","w")
##            w=csv.writer(feed)
##            w.writerow(["Customer_ID","Experience","Delivery Mode","Speed of Delivery","Payment","Range of Products","Additional Comments"])
##            feed.close()
            feed_file=open("Feedback.csv","a+")
            w=csv.writer(feed_file)
            print("1-Excellent")
            print("2-Good")
            print("3-Average")
            print("4-Unsatisfactory")
            print("5- Very Unsatisfactory")
            print()
            exp=int(input("Rate your overall experience with us:  "))
            print()
            mode=int(input("Rate your satisfaction with the facility of Delivery Modes:  "))
            print()
            speed=int(input("Rate your satisfaction with the speed of delivery:  "))
            print()
            pay=int(input("Rate your satisfaction with the ease of payment:  "))
            print()
            prod=int(input("Rate your satisfaction with the Range of Products and Stores available :  "))
            print()
            add=input("Any other comments: ")
            print()
            print("Thank you for your feedback. Your Feedback is very valuable to MedStat.")
            w.writerow([customer_id,exp,mode,speed,pay,prod,add])
            feed_file.close()
        elif input2==1:
            store_dic={1:"Vetson",2:"Guardia",3:"Unified",4:"Medicare",5:"AlwaysStrong",6:"Pop",7:"ArtFriend",8:"Brandink",9:"Mould",10:"Artsy",11:"Stationary4U"}
            print()
            print("                     ~SEARCH AND PLACE AN ORDER~               ")
            print()
            print("""
                  Enter 'medicine' to search for medicine
                  Enter 'stationary' search for stationary""")
            while True:
                print()
                choice=input("Enter your choice from main menu:  ")
                print()

                if choice=="Medicine" or choice=="medicine":
                    print("""Which store do you wish to shop from
                                1. Vetson
                                2. Guardia
                                3. Unified
                                4. Medicare
                                5. AlwaysStrong""")
                    print()
                    choice2=int(input("Enter store number of your choice: "  ))
                    if choice2==1:
                        print()
                        print("Here are the details of all the products in the store Vetson:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(5,12):
                                print(lst[i])
                    if choice2==2:
                        print()
                        print("Here are the details of all the products in the store Guardia:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(15,22):
                                print(lst[i])
                    if choice2==3:
                        print()
                        print("Here are the details of all the products in the store Unified: ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(25,32):
                                print(lst[i])
                    if choice2==4:
                        print("Here are the details of all the products in the store Medicare: ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(35,42):
                                print(lst[i])
                    if choice2==5:
                        print()
                        print("Here are the details of all the products in the store AlwaysStrong:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(45,52):
                                print(lst[i])           
                                
                    
                    

                   
                                
                if choice=="Stationary" or choice=="stationary":
                    print("""which store do you wish to shop from
                                6. Pop
                                7. ArtFriend
                                8. Brandink
                                9. Mould
                                10. Artsy
                                11. Stationary4U""")
                    print()
                    choice2=int(input("Enter store number of your choice: "))
                    if choice2==6:
                        print()
                        print("Here are the details of all the products in the store Pop:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(56,63):
                                print(lst[i])
                    if choice2==7:
                        print()
                        print("Here are the details of all the products in the store ArtFriend:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(66,73):
                                print(lst[i])
                    if choice2==8:
                        print()
                        print("Here are the details of all the products in the store Brandink:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(76,83):
                                print(lst[i])
                    if choice2==9:
                        print()
                        print("Here are the details of all the products in the store Mould:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(86,93):
                                print(lst[i])
                    if choice2==10:
                        print()
                        print("Here are the details of all the products in the store Artsy:   ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(96,103):
                                print(lst[i])

                    if choice2==11:
                        print()
                        print("Here are the details of all the products in the store Stationary4U:  ")
                        print()
                        file=open("products.txt","r")
                        lst=file.readlines()
                        for i in range(106,112):
                                print(lst[i])             
                    else:
                        break
                    
                else: 
                    break




            buy=input("Enter product id to place an order:  ")
            print()

            qty=int(input("Enter Quantity: "))
            list3=[]    
            for i in lst:
                a=i.split("-")
                if len(a)>2:
                    product_id=a[0]
                        
                    if product_id==buy:
                        price=a[2]
                        productname=a[1]
                        print("Product name is:  ",productname, "Price for each is:  ",price)
                        list2=list(price)
                        print()
                       
                       
                        for z in list2:
                            if z.isdigit():
                                list3.append(z)
                        
                        f="".join(list3)            
                  
                        

                    
            TotalAmt=float(f)*qty
            print()
            print("Your total amount is:  ",TotalAmt)
            

            def date():
                a=datetime.datetime.now()
                return(a.date())
            def time():
                c=datetime.datetime.now()
                return(c.time())
            def Invoice(name,customer_id):
                date_invoice=date()
                time_invoice=time()
                Order_id=int(input("Enter your order id:  "))
                print("\t\t\t\t\t\tMEDSTAT")
                print()
                print("\t\t\t\t\t\tINVOICE")
                print()
                print("Date- ",date_invoice,",", "Time- ",time_invoice,)
                print()
                print("Customerid: ",customer_id)
                print()
                print("Name of customer: ",name)
                print()
                print("Current completed orders: ")
                print()
                
                mydb=mysql.connector.connect(host="localhost",username="root",password="sairam123",database="MedStat")
                mycursor=mydb.cursor()
                mycursor.execute("select * from pending_orders where customer_id={""} and Order_id={}".format(customer_id,Order_id))
                myresult=mycursor.fetchall()
                for i in range(len(myresult)):
                    
                    print()
                    print("Order id: ",myresult[i][0])
                    print()
                    print("Medicine or Stationary: ",myresult[i][2])
                    print()
                    print("Store name: ",myresult[i][3])
                    print()
                    print("Product name: ",myresult[i][4])
                    print()
                    print("Quantity: ",myresult[i][5])
                    print()
                    print("Total Cost: ",myresult[i][6])
                mydb.close()
                print()
                print("\t\t\t\t\t\tTHANK YOU")
                print()
                print("\t\t\tFor any other queries, contact us at contactus@medstat.com")
                print()
        
            print()
            name=input("Enter your name: ")
            print()
            
            def update_points():
                file1=open("points and rewards.dat","rb+")
                file1.seek(0,0)
                r=pickle.load(file1)
                
                d={}
                for i in r:   
                    d[i]=r[i]
                file1.close()
                file1=open("points and rewards.dat","wb+")
                d[customer_id]+=TotalAmt
                d[customer_id]+=10
                pickle.dump(d,file1)
                file1.flush()
                
                file1.close()
                Order_id=random.randint(1000,20000)
                print("Your Order ID is:  ",Order_id)
                storename=store_dic[choice2]
                mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
                mycursor=mydb.cursor()
                sql="insert into pending_orders values(%s,%s,%s,%s,%s,%s,%s)"
                val=(Order_id,customer_id,choice,storename,productname,qty,TotalAmt)
                mycursor.execute(sql,val)
                mydb.commit()
                
                  

                
            def Delivery():
                print()
                print("To ensure maximum safety of our customers during this pandemic, MedStat provides the option of contactless delivery")
                print()
                print("Enter 1 for contactless delivery at doorstep.")
                print("Enter 2 for regular delivery.")
                print("Enter 3 for speed post")
                print()
                
                delivery_mode=int(input("Enter your choice"))
                print()
                Address=input("Enter Full Address: ")
                print()
                PostalCode=int(input("Enter Postal code: "))
                print()
                fh=open("Delivery_Customers.csv","a")
                read=csv.reader(fh)
                w=csv.writer(fh)
                dateandtime=datetime.datetime.now()
                if delivery_mode==1:
                    w.writerow([customer_id,"Contactless",Address,PostalCode,dateandtime])
                if delivery_mode==2:
                    w.writerow([customer_id,"Regular",Address,PostalCode,dateandtime])
                if delivery_mode==3:
                    w.writerow([customer_id,"Speed Post",Address,PostalCode,dateandtime])
                fh.close()    
                    

                
            def payment():
                
                file=open("payment.txt","a+")
                string=""
                Delivery()

                print()
                

                name=input("Enter your full name according to passport:  ")
                print()
                Email=input("Enter your email id:  ")
                print()
                Order_id=int(input("Enter your order id:  "))
                print()
                
                payment=int(input("Enter 1 to pay with credit card and 2 to pay with paypal:  "))
                print()
                
                
                if payment==1:
                        cardholder=input("Enter cardholder's name: ")
                        print()
                        cardnumber=int(input("Enter cardnumber: "))
                        print()
                        expirationdate=input("Enter card's expiry date: ")
                        print()
                        cvv=int(input("Enter 3 digit cvv: "))
                        print()
                        string=str(Order_id) + "," + str(customer_id) + "," + name + "," + Email + "," + cardholder + "," + str(cardnumber) + "," + str(expirationdate) + "," + str(cvv) +"\n"
                        file.write(string)
                        print("Payment completed!")
                        print()
                        print("A confirmation email will be sent to your email address")
                        print()
                if payment==2:
                        username=input("Enter username/email id: ")
                        print()
                        password=input("Enter password: ")
                        print()
                        string=str(Order_id) + "," + str(customer_id) + "," + name + "," + Email + "," +  username +"\n"
                        file.write(string)
                        print("Payment completed!")
                        print()
                        print("An email will be sent to your email address")
                        print()
                print("The consignments will be shipped to you within 24 hours")
                file.close()
                print()
                print()
               
                

                
                Invoice(name,customer_id)
                
            def redeem_points():
                
                points=0
                points2=0
                file=open("points and rewards.dat","rb")
                file.seek(0,0)
                rec3=pickle.load(file)
                
                
                
                for i in rec3:
                    
                    if int(i)==customer_id:
                        
                            
                        points=rec3[i]
                        
                        if points//20>=TotalAmt:
                            points2=points-(TotalAmt*20)
                            
                            rec3.update({customer_id:points2 })
                            
                                

                            file.close()
                            fh=open("points and rewards.dat","wb+")
                            pickle.dump(rec3,fh)

                            fh.close()                        
                            print("Your points have been redeemed to make this purchase")
                            print()
                            print("Payment Successful!")
                            print()
                            print("Now you will be directed to choose your mode of delivery!")
                            print()
                            update_points()
                            Delivery()
                            Invoice(name,customer_id)
                            break
                                                        
                        elif points//20<=TotalAmt:
                            print("You do not have enough points")
                            print()
                            print("Now you will be directed towards making your final payment")
                            print()
                            update_points() 
                            payment()
                            break
                    else:
                        print() 
                        print("You do not have any points yet.")
                        print()
                        print("Now you will be directed towards making your final payment")
                        print()
                        update_points()
                        payment()
                        break
                    
                         
                
                
                    
                

            rp=input("Do you wish to redeem your points? Enter yes or no:  ")
            if rp=="yes":

                redeem_points()
            else:
                print("Now you will be directed towards making the final payment!")
                print()
                update_points()
                payment()
                break
                
                
            
        elif  input2==2:
            order_id=int(input("Enter your order id: "))
            print()
            mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
            mycursor=mydb.cursor()
            
            sql="delete from pending_orders where Order_id={} and Customer_id={}".format(order_id,customer_id)
            mycursor.execute(sql)
            mydb.commit()
            print("Your Order has been cancelled. Your refund will be given in 3 to 5 working days.")
            print("Thank you!")

            print()            
            

        elif input2==3:
                fh=open("products.txt")
                r=fh.read()
                print()
                print("This is the list of products available at MedStat: ")
                print() 
                print(r)
                
        elif input2==4:
                
                weburl=request.urlopen("file:///C:/Users/rajes/OneDrive/Desktop/Dheeptha/Dheeptha_school/CS/CS%20Project%2012th%20grade/Html/MedStat%20website.html")
                html=weburl.read()
                url=weburl.geturl()
                hd=weburl.headers
                webbrowser.open_new(url)
                print()
                print()
                
                
        elif input2==5:
                file=open("points and rewards.dat","rb")
                rec3=pickle.load(file)
        
                print()
                print()
                for i in rec3:
                    if int(i)==customer_id:
                        print("\t\t\t~RECEIVE THE CHANCE TO EARN 1 POINT WITH EVERY DOLLAR SPENT WITH MEDSTAT~")
                        print()
                        print("\t\t\t**ENJOY A BONUS OF 10 POINTS WITH EACH PURCHASE**")                       
                        print()
                        print("\t\t\tSTAND A CHANCE TO REBATE $1 FOR EVERY 20 POINTS REDEEMED**")
                        print()
                        
                        print()
                        print("\tYour Customer ID is: ", customer_id)
                        print()
                        print("\tYour existing points are: ", rec3[i])
                        print()
                        break
                        
                        
                                
                
       


print("~.~.~.~WELCOME TO MEDSTAT~.~.~.~")
print()
print('''COVID-19, a war against an invisible enemy has taken a toll on the economy of nations as well as the physical and mental health of its people.
The closure of physical markets has rendered basic necessities like medicine and stationery difficult to obtain for the common public.
It is the need of the hour to improve accessibility to such crucial resources during this period.
MedStat, an online ordering and delivery management system, caters to this very need.
It recognizes the importance of ensuring maximum safety of customers during this pandemic.''')

print()
delivery_dic={"harilalkish28":"mypasswordisthis","calebAsh987":"calebrox007","lucycray67":"lucyspasswd","ashwinkk784":"vamika559","sheetalranjan44":"ranrun240!"}
board_dic={"Amy29":"Rachel28","Ross92":"Mike22","John24":"Harvey11"}

while True:
        print("""                         Enter 1 to login and place an order
                         Enter 2 to sign up
                         Enter 3 to login as employee
                         
                         """)
        print()
        input1=int(input("Enter your choice:  "))
        print()
        if input1==1: 
            id=int(input("Enter customer id: "))
            print()
            password=input("Enter password: ")
            print()
            return1=check(id, password)
            print(return1)
            if return1=="Login Successful!":
                menu()
                break
            
                
        elif input1==2:
            signup()
            break


        elif input1==3:
            print()
            print("Enter 1 if you are currently working at MedStat as a Delivery boy")
            print()
            print("Enter 2 if you are currently part of the MedStat Board of Directors")
            print()
            ch=int(input("Enter choice:  "))
            print()
            if ch==1:
                username_del=input("Enter username:  ")
                password_del=input("Enter password:  ")
                if delivery_dic[username_del]==password_del:
                    print("Login successful!")
                    print()
                    print("Enter yes if order has been completed, no if not")
                    print()
                    ocd=input("Enter your choice:  ")                                                  # where ocd= order completion data
                    if ocd=="yes" or ocd=="Yes":
                        order_id=input("Enter order id:  ")
                        print()
                        print("Order has been completed")
                        print()
                        mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from pending_orders where order_id={}".format(order_id))
                        myresult=mycursor.fetchone()
                        q,w,e,r,t,y,u=myresult
                        sql="insert into completed_orders values(%s,%s,%s,%s,%s,%s,%s)"
                        var=[
                            (q,w,e,r,t,y,u)
                            ]
                        mycursor.executemany(sql,var)
                        mycursor.execute("delete from pending_orders where order_id={}".format(order_id))
                        mydb.commit()
                    else:
                        print("You are logged out.")
                        print()
                        
            if ch==2:
                username_board=input("Enter username: ")
                print()
                password_board=input("Enter password: ")
                print()
                if board_dic[username_board]==password_board:
                    print("Login successful!")
                    print()
                    print()
                    print("                        BACK-END REPORT                      ")
                    print(" ")
                    print("This report entails the data of how many customers we have, Number of orders pending, Number of orders completed and generation of specific data from any table")
                    print(" ")

                    def completed_orders():
                        print()
                        print("To show number and details of all orders that we have completed")
                        print()
                        #to show all the orders we have completed
                        mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from completed_orders")
                        myresult=mycursor.fetchall()
                        
                        print("Orders completed:")
                        print()
                

              
                        d={}

                        print ("{:<10} {:<20} {:<30} {:<20} {:<40} {:<15} {:<20}".format('Order_ID','Customer_ID','Medicine_Stationery','Storename','Product_name','Quantity','Total_price'))

                        for i in myresult:
                            d={i[0]:[i[1],i[2],i[3],i[4],i[5],i[6]]}



                            for k, v in d.items():
                                 Customer_ID,Medicine_Stationery,Storename,Product_name,Quantity,Total_price = v

                            print ("{:<10} {:<20} {:<30} {:<20} {:<40} {:<15} {:<20}".format(k,Customer_ID,Medicine_Stationery,Storename,Product_name,Quantity,Total_price))
   
                    
                       
                       
                       
                        print()
                        print("Total number of orders completed: ",mycursor.rowcount)
                        print()
                        

                    def pending_orders():
                        print()
                        print("To show number and details of all the orders that are pending")
                        print()
                        #to show all the orders that are pending
                        mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from pending_orders")
                        myresult=mycursor.fetchall()
                        print("Orders pending:  ")
                        print()
                        d={}

                        print ("{:<10} {:<20} {:<30} {:<20} {:<40} {:<15} {:<20}".format('Order_ID','Customer_ID','Medicine_Stationery','Storename','Product_name','Quantity','Total_price'))

                        for i in myresult:
                            d={i[0]:[i[1],i[2],i[3],i[4],i[5],i[6]]}



                            for k, v in d.items():
                                 Customer_ID,Medicine_Stationery,Storename,Product_name,Quantity,Total_price = v

                            print ("{:<10} {:<20} {:<30} {:<20} {:<40} {:<15} {:<20}".format(k,Customer_ID,Medicine_Stationery,Storename,Product_name,Quantity,Total_price))
                        print()
                        print("Total number of orders pending:  ",mycursor.rowcount)
                        print()

                    def specific_data():
                        print()
                        print("To retrieve specific data from any table")
                        print()
                        #to get specific data
                        mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
                        mycursor=mydb.cursor()
                        field=input("Enter Field name: ")
                        print()
                        criteria=input("Enter Value for " +field+": " )
                        print()
                        table=input("Enter Table name:  ")
                        print()
                        mycursor.execute("select * from {} where {}='{}'".format(table,field,criteria))
                        myresult=mycursor.fetchall()
                        print()
                        if table=="pending_orders" or table=="completed_orders":
                            d={}

                            print ("{:<10} {:<20} {:<30} {:<20} {:<40} {:<15} {:<20}".format('Order_ID','Customer_ID','Medicine_Stationery','Storename','Product_name','Quantity','Total_price'))

                            for i in myresult:
                                d={i[0]:[i[1],i[2],i[3],i[4],i[5],i[6]]}



                                for k, v in d.items():
                                     Customer_ID,Medicine_Stationery,Storename,Product_name,Quantity,Total_price = v

                                print ("{:<10} {:<20} {:<30} {:<20} {:<40} {:<15} {:<20}".format(k,Customer_ID,Medicine_Stationery,Storename,Product_name,Quantity,Total_price))

                            print()
                            
                        elif table=="customers":
                            d={}

                            print ("{:<30} {:<30} {:<30} {:<20}".format('Customer_ID','Customer_Name','Joining_date','DOB'))

                            for i in myresult:
                                d1=str(i[2])
                                d2=str(i[3])
                                d={i[0]:[i[1],d1,d2]}



                                for k, v in d.items():
                                    Customer_Name,Joining_date,DOB = v

                                print ("{:<30} {:<30} {:<30} {:<20}".format(k,Customer_Name,Joining_date,DOB))
                            print()

                    def customer_details():
                        print()
                        print("To retrieve customer details and the number of customers")
                        print()
                        #to show all details of customers
                     
                        mydb=mysql.connector.connect(host="localhost",user="root",password="sairam123",database="MedStat")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from customers")
                        myresult=mycursor.fetchall()
                        print("Details of customers:  ")
                        print()
                        d={}

                        print ("{:<30} {:<30} {:<30} {:<20}".format('Customer_ID','Customer_Name','Joining_date','DOB'))

                        for i in myresult:
                            d1=str(i[2])
                            d2=str(i[3])
                            d={i[0]:[i[1],d1,d2]}



                            for k, v in d.items():
                                 Customer_Name,Joining_date,DOB = v

                            print ("{:<30} {:<30} {:<30} {:<20}".format(k,Customer_Name,Joining_date,DOB))
                        print()
                        print("Total number of customers:  ",mycursor.rowcount)
                        print()

                    #main
                    print("""Enter:
                            1 for customer details
                            2 for specific data
                            3 for pending orders
                            4 for completed orders
                            5 to quit""")
                    while True:
                        print()
                        dec=int(input("Enter your choice: "))
                        print()
                        if dec==1:
                            customer_details()  
                        elif dec==2:
                            specific_data()
                        elif dec==3:
                            pending_orders()
                        elif dec==4:
                            completed_orders()
                        elif dec==5:
                            break
                        else:
                            print("Invalid input")

                
                


        else:
            print("Invalid input")




##
##def Customers():
##    mydb=mysql.connector.connect(host="localhost",username="root",password="sairam123",database="MedStat")
##    mycursor=mydb.cursor()
##    mycursor.execute("create table customers(Customer_id   integer, Customer_name char(20), Joining_date date)")
##    mydb.commit()
##
##    print("records successfully inserted")
##    mydb.close()
##    mycursor=mydb.cursor()
##    sql="insert into customers values(%s,%s,%s)"
##    val=[
##        ("103","Rachel","2020-02-28"),("406","Phoebe","2020-05-20"),("806","Monica","2020-03-27")
##        ]
##    mycursor.executemany(sql,val)
##    mydb.commit()
##
##    print("records successfully inserted")
##    mydb.close()
##
##
##
##    
##
##
##main
##Customers()    
            
