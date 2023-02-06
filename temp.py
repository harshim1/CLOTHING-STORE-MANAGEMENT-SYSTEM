import mysql.connector as my 
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db=my.connection(host="local host", user="root", password="spps", database="clothingstore")
mycursor=db.cursor
print("connection successfull") 

def instoredata():
    mycursor.execute("select start,totalsales from instore_Sales_weekly")
    result = mycursor.fetchall
    start=[]
    totalsales=[]
    for i in mycursor:
        start.append(i[0])
        totalsales.append(i[1])
        print("Start of the week = ", start)
        print("Total amount of sales = ", totalsales)
    plt.bar(start, totalsales)
    plt.ylim(0,5)
    plt.xlabel("week")
    plt.ylabel("total sales")
    plt.title("total sales weekly instore")
    plt.show()

def instorebybrand():
    mycursor.execute("select start, bestsellar_brand from instore_Sales_weekly")
    result = mycursor.fetchall
    start=[]
    bestsellar_brand=[]
    for i in mycursor:
        start.append(i[0])
        bestsellar_brand.append(i[1])
        print("Start of the week = ", start)
        print("weekly brand with the most sales = ", bestsellar_brand)
    plt.bar(start, bestsellar_brand)
    plt.ylim(0,5)
    plt.xlabel("week")
    plt.ylabel("bestsellar_brand")
    plt.title("weekly bestsellar brand ")
    plt.show()

def instorebyitem():
    mycursor.execute("select start, bestsellar_item from instore_Sales_weekly")
    result = mycursor.fetchall
    start=[]
    bestsellar_item=[]
    for i in mycursor:
        start.append(i[0])
        bestsellar_item.append(i[1])
        print("Start of the week = ", start)
        print("weekly item with the most sales = ", bestsellar_item)
    plt.bar(start, bestsellar_item)
    plt.ylim(0,5)
    plt.xlabel("week")
    plt.ylabel("bestsellar_item")
    plt.title("weekly bestsellar item ")
    plt.show()
    
    
def onlinedata():
    mycursor.execute("select start,totalsales from online_sales_Weekly")
    result = mycursor.fetchall
    start=[]
    totalsales=[]
    for i in mycursor:
        start.append(i[0])
        totalsales.append(i[1])
        print("Start of the week = ", start)
        print("Total amount of sales = ", totalsales)
    plt.bar(start, totalsales)
    plt.ylim(0,5)
    plt.xlabel("week")
    plt.ylabel("total sales")
    plt.title("total sales weekly online")
    plt.show()

def onlinebybrand():
    mycursor.execute("select start, bestsellar_brand from online_sales_Weekly")
    result = mycursor.fetchall
    start=[]
    bestsellar_brand=[]
    for i in mycursor:
        start.append(i[0])
        bestsellar_brand.append(i[1])
        print("Start of the week = ", start)
        print("weekly brand with the most sales = ", bestsellar_brand)
    plt.bar(start, bestsellar_brand)
    plt.ylim(0,5)
    plt.xlabel("week")
    plt.ylabel("bestsellar_brand")
    plt.title("weekly bestsellar brand ")
    plt.show()

def onlinebyitem():
    mycursor.execute("select start, bestsellar_item from online_sales_Weekly")
    result = mycursor.fetchall
    start=[]
    bestsellar_item=[]
    for i in mycursor:
        start.append(i[0])
        bestsellar_item.append(i[1])
        print("Start of the week = ", start)
        print("weekly item with the most sales = ", bestsellar_item)
    plt.bar(start, bestsellar_item)
    plt.ylim(0,5)
    plt.xlabel("week")
    plt.ylabel("bestsellar_item")
    plt.title("weekly bestsellar item ")
    plt.show()

def EditEmp():     
    empno=input("Enter Employee number to be edited : ")     
    sql="select * from employee where empno=%s"     
    ed=(empno,)     
    mycursor.execute(sql,ed)     
    res=mycursor.fetchall()     
    for x in res:         
        print(x)     
        print("")     
        fld=input("Enter the field which you want to edit : ")     
        val=input("Enter the value you want to set : ")
        sql="Update employee set " + fld +"='" + val + "' empno='" + empno + "'"      
        sq=sql     
        mycursor.execute(sql)     
        print("Editing Done : ")     
        print("After correction the record is  : ")     
        sql="select * from employee where empno=%s"     
        ed=(empno,)     
        mycursor.execute(sql,ed)     
        res=mycursor.fetchall()     
        for x in res:         
            print(x)     
            db.commit()

def AddEmp():     
    L=[]     
    stk=[]     
    empno=input("Enter the Employee Number : ")     
    L.append(empno)     
    emp_name=input("Enter the Employee Name : ")     
    L.append(emp_name)     
    deptno=input("Enter the Department Number : ")     
    L.append(deptno)     
    dept_name=input("Enter the Department Name : ")     
    L.append(dept_name)
    hiredate=input("Enter the Hire Date :  ")     
    L.append(hiredate)     
    salary=input("Enter employee Salary : ")     
    L.append(salary)     
    contact=int(input("Enter employee contact :"))     
    L.append(contact)  
    email=input("Enter employee email :")     
    L.append(email)
    employee=(L)     
    sql="Insert into employee (empno, emp_name, deptno, dept_name, hiredate, salary, contact, email);)values(%s,%s,%s,%s,%s,%s,%s,%s)"     
    mycursor.execute(sql,employee)     
    db.commit()     
    stk.append(empno)     
    stk.append(0)     
    stk.append("No")     
    st=(stk)     
    db.commit()     
    print("Employee added succesfully! ") 

def employees():
    print("Display Menu: Select the category to display the employee")     
    print("1. All Details")     
    print("2. Employee Name:")     
    print("3. Department Name : ")     
    print("4. Hire Date ")     
    print("5. Salary ")     
    print("6. Contact ")     
    x=0     
    ch=int(input("Enter your choice to display : "))     
    if ch==1: 
        sql="select * from employee "         
        mycursor.execute(sql)         
        res=mycursor.fetchall()         
        for x in res:             
            print(x)         
            x=1 
    elif ch==2:           
        var='emp_name'           
        val=input("Enter name of employee : ")     
    elif ch==3:           
        var='dept_name'           
        val=input("Enter the name of department : ")     
    elif ch==4:           
        var='hiredate'           
        val=input("Enter employee's hire date")     
    elif ch==5:           
        var='salary'           
        val=input("Enter employee's salary")     
    elif ch==6:           
        var='contact'           
        val=input("Enter employee's contact ")                 
    if x==0:         
        sql="select * from employee where " + var + " = %s"     
        sq=sql         
        tp=(val,)         
        mycursor.execute(sq,tp)         
        res=mycursor.fetchall()         
        for x in res:             
            print(x) 
            
def customers():
    sql="select * from customerdata"         
    mycursor.execute(sql)         
    res=mycursor.fetchall()         
    for x in res:             
        print(x)         
        x=1 
        
def AddCust():     
    L=[]     
    stk=[]     
    custno=input("Enter the Customer Number : ")     
    L.append(custno)     
    cust_name=input("Enter the Customer Name : ")     
    L.append(cust_name)     
    cust_address=input("Enter the Customer Address : ")     
    L.append(cust_address)     
    cust_postcalcode=input("Enter the Customer Postal Code : ")     
    L.append(cust_postcalcode)
    cust_contact=input("Enter the Customer Contact :  ")     
    L.append(cust_contact)     
    cust_email=input("Enter the Customer Email : ")     
    L.append(cust_email)     
    num_of_items=int(input("Enter the Number of Items :"))     
    L.append(num_of_items)  
    itemcode=input("Enter the Item code :")     
    L.append(itemcode)
    discount=int(input("Enter discount given :"))     
    L.append(discount)
    billing_amt=int(input("Enter the billing amount :"))     
    L.append(billing_amt)  
    payment_mode=input("Enter payment mode :")     
    L.append(payment_mode)
    delivery=input("Delivery status :")     
    L.append(delivery)
    customerdata=(L)     
    sql="Insert into customerdata (custno, cust_name, cust_address, cust_postalcode, cust_contact, cust_email, num_of_items, itemcode, discount, billing_amt, payment_mode, delivery);)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"     
    mycursor.execute(sql,customerdata)     
    db.commit()     
    stk.append(custno)     
    stk.append(0)     
    stk.append("No")     
    st=(stk)     
    db.commit()     
    print("Customer added succesfully! ") 

def EditCust():     
    custno=input("Enter customer number to be edited : ")     
    sql="select * from customerdata where custno=%s"     
    ed=(custno,)     
    mycursor.execute(sql,ed)     
    res=mycursor.fetchall()     
    for x in res:         
        print(x)     
        print("")     
        fld=input("Enter the field which you want to edit : ")     
        val=input("Enter the value you want to set : ")
        sql="Update customerdata set " + fld +"='" + val + "' custno='" + custno + "'"      
        sq=sql     
        mycursor.execute(sql)     
        print("Editing Done : ")     
        print("After correction the record is  : ")     
        sql="select * from customerdata where custno=%s"     
        ed=(custno,)     
        res=mycursor.fetchall()     
        mycursor.execute(sql,ed)     
        for x in res:         
            print(x)     
            db.commit()
                        
def showinstoresales():
    print("Display Menu: Select the category to display the sales")     
    print("1. All Details")     
    print("2. Men Sales")     
    print("3. Women Sales")     
    print("4. Total Sales ")     
    print("5. Bestsellar_brand")     
    print("6. Bestsellar_item")     
    x=0     
    ch=int(input("Enter your choice to display : "))     
    if ch==1: 
        sql="select * from instore_Sales_weekly"         
        mycursor.execute(sql)         
        res=mycursor.fetchall()         
        for x in res:             
            print(x)         
            x=1 
    elif ch==2:           
        var='Men Sales'           
        val=input("Enter Men Sales : ")     
    elif ch==3:           
        var='Women Sales'           
        val=input("Enter Women Sales : ")     
    elif ch==4:           
        var='Total Sales'           
        val=input("Enter Total Sales ")     
    elif ch==5:           
        var='Bestsellar_brand'           
        val=input("Enter the Bestsellar brand of a week ")     
    elif ch==6:           
        var='Bestsellar_item'           
        val=input("Enter the Bestsellar item of a week ")                 
    if x==0:         
        sql="select * from instore_Weekly_sales where " + var + " = %s"     
        sq=sql         
        tp=(val,)         
        mycursor.execute(sq,tp)         
        res=mycursor.fetchall()         
        for x in res:             
            print(x) 
            
def showonlinesales():
    print("Display Menu: Select the category to display the sales")     
    print("1. All Details")     
    print("2. Men Sales")     
    print("3. Women Sales")     
    print("4. Total Sales ")     
    print("5. Bestsellar_brand")     
    print("6. Bestsellar_item")     
    x=0     
    ch=int(input("Enter your choice to display : "))     
    if ch==1: 
        sql="select * from online_sales_Weekly"         
        mycursor.execute(sql)         
        res=mycursor.fetchall()         
        for x in res:             
            print(x)         
            x=1 
    elif ch==2:           
        var='Men Sales'           
        val=input("Enter Men Sales : ")     
    elif ch==3:           
        var='Women Sales'           
        val=input("Enter Women Sales : ")     
    elif ch==4:           
        var='Total Sales'           
        val=input("Enter Total Sales ")     
    elif ch==5:           
        var='Bestsellar_brand'           
        val=input("Enter the Bestsellar brand of a week ")     
    elif ch==6:           
        var='Bestsellar_item'           
        val=input("Enter the Bestsellar item of a week ")                 
    if x==0:         
        sql="select * from online_sales_Weekly where " + var + " = %s"     
        sq=sql         
        tp=(val,)         
        mycursor.execute(sq,tp)         
        res=mycursor.fetchall()         
        for x in res:             
            print(x)             

def AddNewWeekIN():     
    L=[]     
    stk=[]     
    week=input("Enter the Week Code: ")     
    L.append(week)     
    start=input("Date on Monday : ")     
    L.append(start)     
    end=input("Date on Saturday ")     
    L.append(end)     
    mensales=input("Men Sales for the week : ")     
    L.append(mensales)
    womensales=input("Women Sales for the week : ")     
    L.append(womensales)     
    totalsales=input("Total Sales for the week : ")     
    L.append(totalsales)     
    brand=int(input("Bestsellar brand of the week"))     
    L.append(brand)  
    item=int(input("Bestsellar item of the week"))     
    L.append(item)
    instore_Sales_weekly=(L)     
    sql="Insert into instore_Sales_weekly (week, start, end, mensales, womensales, totalsales, betssellar_brand, bestsellar_item) values(%s,%s,%s,%s,%s,%s,%s,%s)"     
    mycursor.execute(sql,instore_Sales_weekly)     
    db.commit()     
    stk.append(week)     
    stk.append(0)     
    stk.append("No")     
    st=(stk)     
    db.commit()     
    print("inserted ")     
        
    
def AddNewWeekON():     
     L=[]     
     stk=[]     
     week=input("Enter the Week Code: ")     
     L.append(week)     
     start=input("Date on Monday : ")     
     L.append(start)     
     end=input("Date on Saturday ")     
     L.append(end)     
     mensales=input("Men Sales for the week : ")     
     L.append(mensales)
     womensales=input("Women Sales for the week : ")     
     L.append(womensales)     
     totalsales=input("Total Sales for the week : ")     
     L.append(totalsales)     
     brand=int(input("Bestsellar brand of the week"))     
     L.append(brand)  
     item=int(input("Bestsellar item of the week"))     
     L.append(item)
     online_sales_Weekly=(L)     
     sql="Insert into online_Sales_Weekly (week, start, end, mensales, womensales, totalsales, betssellar_brand, bestsellar_item) values(%s,%s,%s,%s,%s,%s,%s,%s)"     
     mycursor.execute(sql,online_sales_Weekly)     
     db.commit()     
     stk.append(week)     
     stk.append(0)     
     stk.append("No")     
     st=(stk)     
     db.commit()     
     print("inserted ")     
            

def showstock():
    print(" 1. WOMEN INSTOCK")  
    print(" 2. MEN INSTOCK")
    k=int(input("Women or Men?"))
    if(k==1):
        print("Display Menu: Select the category to display the data")     
        print("1. All Details")     
        print("2. Item Name:")     
        print("3. Item Brand:")     
        print("4. Item Colour")     
        print("5. Item Size")     
        print("6. Item Cost")     
        x=0     
        ch=int(input("Enter your choice to display : "))     
        if ch==1: 
            sql="select * from women_instock"         
            mycursor.execute(sql)         
            res=mycursor.fetchall()         
            for x in res:             
                print(x)         
                x=1 
        elif ch==2:           
            var='item_name'           
            val=input("Enter the name of Item : ")     
        elif ch==3:           
            var='brand_name'           
            val=input("Enter the name of Brand : ")     
        elif ch==4:           
            var='color'           
            val=input("Enter color of item ")     
        elif ch==5:           
            var='size'           
            val=input("Enter the Size of item")     
        elif ch==6:           
            var='cost'           
            val=input("Enter the cost of item")                 
        if x==0:         
            sql="select * from women_instock where " + var + " = %s"     
            sq=sql         
            tp=(val,)         
            mycursor.execute(sq,tp)         
            res=mycursor.fetchall()         
            for x in res:             
                print(x) 
    if(k==1):
        print("Display Menu: Select the category to display the data")     
        print("1. All Details")     
        print("2. Item Name:")     
        print("3. Item Brand:")     
        print("4. Item Colour")     
        print("5. Item Size")     
        print("6. Item Cost")     
        x=0     
        ch=int(input("Enter your choice to display : "))     
        if ch==2: 
            sql="select * from men_instock"         
            mycursor.execute(sql)         
            res=mycursor.fetchall()         
            for x in res:             
                print(x)         
                x=1 
        elif ch==2:           
            var='item_name'           
            val=input("Enter the name of Item : ")     
        elif ch==3:           
            var='brand_name'           
            val=input("Enter the name of Brand : ")     
        elif ch==4:           
            var='color'           
            val=input("Enter color of item ")     
        elif ch==5:           
            var='size'           
            val=input("Enter the Size of item")     
        elif ch==6:           
            var='cost'           
            val=input("Enter the cost of item")                 
        if x==0:         
            sql="select * from men_instock where " + var + " = %s"     
            sq=sql         
            tp=(val,)         
            mycursor.execute(sq,tp)         
            res=mycursor.fetchall()         
            for x in res:             
                print(x) 
                           
def AddItemforwomen():     
    L=[]     
    stk=[]     
    item_no=input("Enter the Item Number : ")     
    L.append(item_no)     
    item_name=input("Enter the Item Name : ")     
    L.append(item_name)     
    brand_name=input("Enter the Brand Name : ")     
    L.append(brand_name)     
    brandcode=input("Enter the Brand Number : ")     
    L.append(brandcode)
    quantity=input("Quantity : ")     
    L.append(quantity)     
    sold_out=input("Sold_Out :")     
    L.append(sold_out)     
    cost=int(input("Enter the Cost for Item :"))     
    L.append(cost)  
    color=input("Enter the color for Item :")  
    L.append(color)
    size=int(input("Enter the size for Item :")     
    L.append(size)
    women_instock=(L)     
    sql="Insert into women_instock (item_no,item_name,brand_name,brandcode,quatity,sold_out,cost,size,color)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"     
    mycursor.execute(sql,women_instock)     
    db.commit()     
    stk.append(item_no)     
    stk.append(0)     
    stk.append("No")     
    st=(stk)     
    db.commit()     
    print("One Product inserted ") 
  
def AddItemformen():     
    L=[]     
    stk=[]     
    item_no=input("Enter the Item Number : ")     
    L.append(item_no)     
    item_name=input("Enter the Item Name : ")     
    L.append(item_name)     
    brand_name=input("Enter the Brand Name : ")     
    L.append(brand_name)     
    brandcode=input("Enter the Brand Number : ")     
    L.append(brandcode)
    quantity=input("Quantity : ")     
    L.append(quantity)     
    sold_out=input("Sold_Out :")     
    L.append(sold_out)     
    cost=int(input("Enter the Cost for Item :"))     
    L.append(cost)  
    color=(input("Enter the color for Item :")   
    L.append(color)
    size=input("Enter the size for Item :")     
    L.append(size)
    men_instock=(L)     
    sql="Insert into men_instock (item_no,item_name,brand_name,brandcode,quatity,sold_out,cost,size,color)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"     
    mycursor.execute(sql,men_instock)     
    db.commit()     
    stk.append(item_no)     
    stk.append(0)     
    stk.append("No")     
    st=(stk)     
    db.commit()     
    print("One Product inserted ")     
    
def EditItem_women():     
    item_no=input("Enter Item number to be edited : ")     
    sql="select * from women_instock where item_no=%s"     
    ed=(item_no,)     
    mycursor.execute(sql,ed)     
    res=mycursor.fetchall()     
    for x in res:         
        print(x)     
        print("")     
        fld=input("Enter the field which you want to edit : ")     
        val=input("Enter the value you want to set : ")
        sql="Update women_instock set " + fld +"='" + val + "' item_no='" + item_no + "'"      
        sq=sql     
        mycursor.execute(sql)     
        print("Editing Done : ")     
        print("After correction the record is  : ")     
        sql="select * from women_instock where item_no=%s"     
        ed=(item_no,)     
        mycursor.execute(sql,ed)     
        res=mycursor.fetchall()     
        for x in res:         
            print(x)     
            db.commit()
            
def EditItem_men():     
    item_no=input("Enter Item number to be edited : ")     
    sql="select * from men_instock where item_no=%s"     
    ed=(item_no,)     
    mycursor.execute(sql,ed)     
    res=mycursor.fetchall()     
    for x in res:         
        print(x)     
        print("")     
        fld=input("Enter the field which you want to edit : ")     
        val=input("Enter the value you want to set : ")
        sql="Update men_instock set " + fld +"='" + val + "' item_no='" + item_no + "'"      
        sq=sql     
        mycursor.execute(sql)     
        print("Editing Done : ")     
        print("After correction the record is  : ")     
        sql="select * from men_instock where item_no=%s"     
        ed=(item_no,)     
        mycursor.execute(sql,ed)     
        res=mycursor.fetchall()     
        for x in res:         
            print(x)     
            db.commit()            

def DelProductinwomen():     
    item_no=input("Enter the Item number to be deleted : ")     
    sql="delete from women_instock where item_no=%s"     
    id=(item_no,)     
    mycursor.execute(sql,id)     
    db.commit()         
    print("One Item Deleted")
    
def DelProductinmen():     
    item_no=input("Enter the Item number to be deleted : ")     
    sql="delete from men_instock where item_no=%s"     
    id=(item_no,)     
    mycursor.execute(sql,id)     
    db.commit()         
    print("One Item Deleted")    
    
    
    
def main():
    print("WELCOME TO THE PLEASING CLOTHING STORE MANAGEMENT SYSTEM")
    print("\n 1.Stocks")
    print("\n 2.Sales")
    print("\n 3.Customers") 
    print("\n 4.Employees")
    print("\n 0 Exit")  
    ch=int(input("enter your choice"))
    if(ch==1):
        print("\n 1. View Stocks")
        print("\n 2. Add New Item")
        print("\n 3. Edit An Item")
        print("\n 4. Delete An Item")
        print("\n 0. EXIT")
        a=int(input("Enter a number"))
        if(a==1):
            showstock()
        elif(a==2):
            g=int(input("Men (1) or Women (2)"))
            if(g==1):
                AddItemformen()
            elif(g==2):
                AddItemforwomen()
        elif(a==3):
            g=int(input("Men (1) or Women (2)"))
            if(g==1):
                EditItem_men()
            elif(g==2):
                EditItem_women()
        elif(a==4):
            g=int(input("Men (1) or Women (2)"))
            if(g==1):
                DelProductinmen()
            elif(g==2):
                DelProductinwomen()
        else:
            main()
        
                
    if(ch==2):
        k=int(input("Enter 1 for Instore Sales and 2 for Online Sales : "))
        if(k==1):
            print("\n 1. View Weekly Sales")
            print("\n 2. Add New Week")
            print("\n 3. To Check Variation")
            print("\n 0. EXIT")
            a=int(input("Enter a number"))
            if(a==1):
                showinstoresales()
            elif(a==2):
                AddNewWeekIN()
            elif(a==3):
                instoredata()
                instorebybrand()
                instorebyitem()
            else:
                main()
                
        if(k==2):
            print("\n 1. View Weekly Sales")
            print("\n 2. Add New Week")
            print("\n 3. To Check Variation")
            print("\n 0. EXIT")
            a=int(input("Enter a number"))
            if(a==1):
                showonlinesales()
            elif(a==2):
                AddNewWeekON()
            elif(a==3):
                onlinedata()
                onlinebybrand()
                onlinebyitem()
            else:
                main()
                
    
    if(ch==3):
        print("\n 1.Show All Customers ")
        print("\n 2.Enter New Customer ")
        print("\n 3.Edit for Old Customers ")
        print("\n 0. EXIT")
        m=int(input("Enter choice : "))
        if(m==1):
            customers()
        if(m==2):
            AddCust()
        if(m==3):
            EditCust()
        else:
            main()
    
    if(ch==4):
        print("\n 1.Show All Employees ")
        print("\n 2.Enter New Employee ")
        print("\n 3.Edit for Old Employee")
        print("\n 0. EXIT")
        m=int(input("Enter choice : "))
        if(m==1):
            employees()
        if(m==2):
            AddEmp()
        if(m==3):
            EditEmp()
        else:
            main()
           
    else:
        print("your request cannot be proceeded please try again")
        
        
                
                
      
