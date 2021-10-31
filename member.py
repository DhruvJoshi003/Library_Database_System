#module for members

import mysql.connector as m

db=m.connect(host='localhost',user='root',passwd='dhruv')

if db.is_connected():
    
    print('Connection established')
    c=db.cursor()
    c.execute('use LIBRARY')
    qwerty=('create table if not exists members(Mid int(9) primary key,Mname varchar(30) not null,MembershipType varchar(30) not null,BorrowedBook varchar(60),BorrowDate date,ReturnDate date,Id int,foreign key(Id) references books(Id));')
    c.execute(qwerty)

    def INS():                       #To Insert A Row
        try: 
            print('')
            k=int(input('Enter the no. of rows you want to add: '))
            print('')
            
            for i in range(0,k):
                print('NOTE for inserting record:')
                print('Member Id once entered,cannot be changed')
                print('')
                mid=str(input("Enter the Member Id: "))
                mn=str(input("Enter the Member Name: "))
                mt=str(input("Enter the Membership Type: "))
                bb=str(input("Enter the Name of Borrowed Book(Enter null if not borrwed): ")) 
                bd=str(input("Enter the Borrow Date(Enter null if not borrwed): "))
                rd=str(input('Enter the Return Date(Enter null if not borrwed): '))
                ID=str(input('Enter the Book Id(Enter null if not borrwed): '))

                if ID=='null':
                    querym="insert into members values('"+mid+"','"+mn+"','"+mt+"',null,null,null,null)"

                else:
                    querym="insert into members values('"+mid+"','"+mn+"','"+mt+"','"+bb+"','"+bd+"','"+rd+"','"+ID+"')"

                c.execute(querym)

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
            mid=str(input('Enter the Member id: '))
            q="delete from members where Mid='"+mid+"'"
            c.execute(q)
            db.commit()
            x=c.rowcount
            
                    
            if x==0:
                print('')
                print('An error occured')
                print('Member id you gave does not exist :( ')
                print('')

            else:
                query2="Mid '"+mid+"' is kicked out of the table "
                print('')
                print(query2)
                print('')
                        

    def DIS():                                    #To display the table
        c.execute('select * from members')
        ans=c.fetchall()
        print('')
        for i in ans:
            print(i)
            print('')
        print('')
            

    def SEA():              #To search for a book
        mid=str(input('Enter the Member id: '))
        query="Select * from members where Mid='"+mid+"'"
        c.execute(query)
        x=c.rowcount

        if x==0:
            print('')
            print('An error occured')
            print('Member id you gave does not exist :( ')
            print('')

        else:
            ans=c.fetchall()
            print('')
            for i in ans:
                print(i)
            print('')

    def SEA_N():
        n=str(input('Enter the name of the Member: '))
        name='%'+n+'%'
        NAME=name
        query="select * from members where Mname like '"+NAME+"' "
        c.execute(query)

        ans=c.fetchall()
        
        if len(ans)>0:
            print('')
            for i in ans:
                print(i)
            print('')

        else:
            print('')
            print('An error occured')
            print('Member Name you gave does not exist :( ')
            print('')



        

    def UPD():
        
        DIS()
        mid=str(input("Enter the book Member id: "))

        IDfinal='%'+mid+'%'
        IDforSQL=IDfinal
        query1="select * from members where Mid like '"+IDforSQL+"' "
        c.execute(query1)

        ans=c.fetchall()
        
        if len(ans)==0:
            print('')
            print('An error occured due to input of no existing ID')
            print('Please try again')
            print('')

        else:
            print('')
            print("Enter 1 to update the Member Name: ")
            print("Enter 2 to update the Member Name: ")
            print("Enter 3 to update the Borrowed Book: ")
            print("Enter 4 to update the Borrow Date: ")
            print('Enter 5 to update the Return Date: ')
            print('')
            colno=str(input('So, what will it be?: '))
            print('')

            if int(colno)==1:
                mn=str(input('Enter the updated Member Name: '))
                query="update members set Mname='"+mn+"' where Mid='"+mid+"'"
                
            elif int(colno)==2:
                mt=str(input('Enter the updated Membership Type: '))
                query="update members set MembershipType='"+mt+"' where Mid='"+mid+"'"

            elif int(colno)==3:
                bb=str(input('Enter the updated Borrowed Book: '))
                query="update members set BorrowedBook='"+bb+"' where Mid='"+mid+"'"
               
            elif int(colno)==4:
                bd=str(input('Enter the updated Borrow Date: '))
                query="update members set BorrowDate='"+bd+"' where Mid='"+mid+"'"

            elif int(colno)==5:
                rd=str(input('Enter the updated Return Date: '))
                query="update members set ReturnDate='"+rd+"' where Mid='"+mid+"'"
                
            else:
                print('The entered value is incorrect,please try again')
                

            
            c.execute(query)
            db.commit()
            print('')
            print('Updated :)')
            print('')



else:
    print('Unable to establish Connectivity ')
