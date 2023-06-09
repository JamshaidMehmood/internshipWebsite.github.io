import pymysql

class DB:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user = user
        self.password=password
        self.database=database

    def searchCustomer(self,data):
        # v=View()
        mydb = None
        mydbCursor=None
        found = False
        results=""
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql1="select * from customer where email=%s and name =%s"
            args1=(data[0],data[1])
            mydbCursor.execute(sql1, args1)
            results = mydbCursor.fetchall()
            if results !=None:
                found=True

        except Exception as e:
            print(e)
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
    
            return  found,results
    
    def transferMoney(self,data):
        mydb = None
        mydbCursor=None
        transfered = False
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            sql1="select * from customer where email=%s"
            args1=(data[0])
            mydbCursor.execute(sql1, args1)
            results = mydbCursor.fetchone()
            print(results)
            if results !=None:
                dummy=0
                sql1="update customer set current_balance =%s where email =%s"
                
                dummy=results[2]
                print(dummy)
                dummy=dummy+int(data[2])
                print(dummy)
                args1=(dummy,data[0])
                mydbCursor.execute(sql1, args1)
                mydb.commit()
                transfered=True
        
        except Exception as e:
            print(e)
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
    
            return  transfered
