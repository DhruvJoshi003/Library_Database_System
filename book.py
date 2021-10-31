#module for books

import mysql.connector as m

db=m.connect(host='localhost',user='root',passwd='dhruv')

if db.is_connected():
    print('Connection established')
    c=db.cursor()
    c.execute('use LIBRARY')
    asdfgh='create table if not exists books(Id int(9) primary key,Name varchar(60) not null,Author varchar(30) not null,Genre varchar(60) not null,Publisher varchar(60),Status char(1));'
    c.execute(asdfgh)

    def INS():                                                    #To Insert A Row
        try: 
            print('')
            k=int(input('Enter the no. of rows you want to add: '))
            print('')
            
            for i in range(0,k):
                print('NOTE for inserting record:')
                print('Id once entered,cannot be changed')
                print('')
                Id=str(input("Enter the book Id: "))
                na=str(input("Enter the Name: "))
                au=str(input("Enter the Author: "))
                ge=str(input("Enter the Genre: "))
                pu=str(input("Enter the Publisher: "))
                print('')
                print('NOTE for Status: (A= Available ; B= Borrowed)')
                print('')
                st=str(input('Enter the Status of project: '))
                
                queryb="insert into books values('"+Id+"','"+na+"','"+au+"','"+ge+"','"+pu+"','"+st+"')"

                c.execute(queryb)

                db.commit()

                print('')
                print('Data Inserted :)')
                print('')

        except :
            print('')
            print('An error occured')
            print('The ID you gave may already exist or it is not an integer value')
            print('')
            
    def DEL():                                      #To delete a row
        print('')
        k=int(input('Enter the no. of rows you want to Delete: '))
        print('')
        
        for i in range(0,k):
            Id=str(input('Enter the book Id: '))
            q="delete from books where Id='"+Id+"'"
            c.execute(q)
            db.commit()
            x=c.rowcount
            
                    
            if x==0:
                print('')
                print('An error occured')
                print('ID you gave does not exist :( ')
                print('')

            else:
                query2="Id '"+Id+"' is kicked out of the table "
                print('')
                print(query2)
                print('')
                        

    def DIS():                                    #To display the table
        c.execute('select * from books')
        ans=c.fetchall()
        print('')
        for i in ans:
            print(i)
            print('')
        print('')
            

    def SEA():              #To search for a book
        Id=str(input('Enter the book Id: '))
        query="Select * from books where Id='"+Id+"'"
        c.execute(query)
        x=c.rowcount

        if x==0:
            print('')
            print('An error occurred')
            print('ID you gave does not exist :( ')
            print('')

        else:
            ans=c.fetchall()
            print('')
            for i in ans:
                print(i)
            print('')

    def SEA_N():
        n=str(input('Enter the name of the book: '))
        name='%'+n+'%'
        NAME=name
        query="select * from books where Name like '"+NAME+"' "
        c.execute(query)
        x=c.rowcount

        ans=c.fetchall()
        
        if len(ans)>0:
            print('')
            for i in ans:
                print(i)
            print('')

        else:
            print('')
            print('An error occurred')
            print('Name you gave does not exist :( ')
            print('')        

        
    def SA():
        s='A'
        query="Select * from books where Status='"+s+"'"
        c.execute(query)
        ans=c.fetchall()
        print('')
        for i in ans:
            print(i)
        print('')


    def UPD():  
        DIS()
        Id=str(input("Enter the book Id: "))

        IDfinal='%'+Id+'%'
        IDforSQL=IDfinal
        query1="select * from books where Id like '"+IDforSQL+"' "
        c.execute(query1)

        ans=c.fetchall()
        
        if len(ans)==0:
            print('')
            print('An error occured due to input of no existing ID')
            print('Please try again')
            print('')
        
        else:   
            print('')
            print("Enter 1 to update the Name: ")
            print("Enter 2 to update the Author: ")
            print("Enter 3 to update the Genre: ")
            print("Enter 4 to update the Publisher: ")
            print('Enter 5 to update the Status: ')
            print('')
            colno=str(input('So, what will it be?: '))
            print('')

            if int(colno)==1:
                Name=str(input('Enter the updated Name: '))
                query="update books set Name='"+Name+"' where Id='"+Id+"'"
               
                
            elif int(colno)==2:
                Author=str(input('Enter the updated Author: '))
                query="update books set Author='"+Author+"' where Id='"+Id+"'"
              

            elif int(colno)==3:
                Genre=str(input('Enter the updated Genre: '))
                query="update books set Genre='"+Genre+"' where Id='"+Id+"'"
                

            elif int(colno)==4:
                Publisher=str(input('Enter the updated Publisher: '))
                query="update books set Publisher='"+Publisher+"' where Id='"+Id+"'"

            elif int(colno)==5:
                Status=str(input('Enter the updated Status: '))
                query="update books set Status='"+Status+"' where Id='"+Id+"'"

            else:
                print('The entered value is incorrect,please try again')
                

            c.execute(query)
            db.commit()
            print('')
            print('Updated :)')
            print('')

else:
    print('Unable to establish Connectivity ')
