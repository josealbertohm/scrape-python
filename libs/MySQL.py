import MySQLdb

class MySQL(object):
    dbConn = None

    def __init__(self):
        self._host     = "localhost"
        self._user     = None
        self._passwd   = None
        self._dbname   = None

    @property 
    def host(self):
        return self._host 
    @host.setter
    def host(self, value):
        self._host = value 

    @property 
    def user(self):
        return self._user 
    @user.setter
    def user(self, value):
        self._user = value 

    @property 
    def passwd(self):
        return self._passwd 
    @passwd.setter
    def passwd(self, value):
        self._passwd = value 

    @property 
    def dbname(self):
        return self._dbname 
    @dbname.setter
    def dbname(self, value):
        self._dbname = value 

    def connect(self):
        try:
            # Open database connection
            self.dbConn = MySQLdb.connect(self._host,self._user,self._passwd,self._dbname)

            # prepare a cursor object using cursor() method
            cursor = self.select("SELECT VERSION()")

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            print "Database version : %s " % data
        except:
            print("Error in database connection")

    def close(self):
        if self.dbConn != None:
            try:
                self.dbConn.close()
            except:
                print "Error in database close"

    def select(self, sql):
        # prepare a cursor object using cursor() method
        cursor = self.dbConn.cursor()

        # execute SQL query using execute() method.
        cursor.execute(sql)

        return cursor

    def update(self, sql):
        try:
            # prepare a cursor object using cursor() method
            cursor = self.dbConn.cursor()

            # execute SQL query using execute() method.
            cursor.execute(sql)

        except:
             print "Error updating or deleting records"
        finally:
            cursor.close()           

    def insertMany(self, sql, values):
        try:
            # prepare a cursor object using cursor() method
            cursor = self.dbConn.cursor()

            # execute SQL query using executemany() method.
            cursor.executemany(sql, values)

            self.dbConn.commit()
        except:
            print "Error inserting many records"
        finally:
            cursor.close()