import sqlite3

class User():

    def __init__(self,mail,stat):

        self.mail = mail
        self.stat = stat

    def __str__(self):

        return "\nMail: {}\nStat: {}\n------------".format(self.mail,self.stat)


class Mail_Database():

    def __init__(self):

        self.connect_databse()

    def connect_databse(self):

        self.connection = sqlite3.connect("Cinemaximum.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists Tbl_Mail_Database (" \
                "User_mail text," \
                "Status boolean default True)"

        self.cursor.execute(query)
        self.connection.commit()

    def show_users(self):

        query = "select * from Tbl_Mail_Database"
        self.cursor.execute(query)

        user = self.cursor.fetchall()

        if (len(user) != 0):

            for i in user:
                info = User(i[0],i[1])
                print(info)

        else:
            return 0

    def add_user(self,user):

        query = "insert into Tbl_Mail_Database values (@p1,@p2)"
        self.cursor.execute(query,(user.mail,user.stat))
        self.connection.commit()

    def delete_user(self,user_mail):

        query = "delete from Tbl_Mail_Database where user_mail = @p1"
        self.cursor.execute(query, (user_mail,))
        self.connection.commit()

    def update_user_status_and_mail(self,user_mail,stat,new_mail):

        query_one = "select user_mail from tbl_mail_database"
        self.cursor.execute(query_one)
        user = self.cursor.fetchall()

        if (len(user) != 0):

            query_two = "update Tbl_Mail_Database set user_mail = @p1 ,Status = @p2 where user_mail = @p3"
            self.cursor.execute(query_two, (new_mail, stat, user_mail))
            self.connection.commit()

        else:
            print("No mail found as {}.".format(user_mail))


    def get_user_mail(self):

        query = "select * from tbl_mail_database where status = 1"
        self.cursor.execute(query)
        user_list = self.cursor.fetchall()
        return user_list

    def check_if_user_exsits(self,mail):

        query = "select * from tbl_mail_database where user_mail = @p1"
        self.cursor.execute(query,(mail,))
        user = self.cursor.fetchall()

        if (len(user) == 0):
            return 0
        else:
            return 1

    def any_user(self):

        query = "select * from Tbl_Mail_Database"
        self.cursor.execute(query)

        user = self.cursor.fetchall()

        if (len(user) != 0):

            return 1

        else:
            return 0
        asdasdsasadadadad
