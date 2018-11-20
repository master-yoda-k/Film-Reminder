import sqlite3

class Film_Backup():

    def __init__(self,Film_Name,Film_Link,Film_Release_Date,Film_Time,Film_Genre,Film_Score,Film_Summary,Film_Age_Rate,Film_EN_Name,Film_Formats):
        self.Film_Name = Film_Name
        self.Film_Link = Film_Link
        self.Film_Formats = Film_Formats
        self.Film_Time = Film_Time
        self.Film_Genre = Film_Genre
        self.Film_Score = Film_Score
        self.Film_Summary = Film_Summary
        self.Film_Age_Rate = Film_Age_Rate
        self.Film_EN_Name = Film_EN_Name
        self.Film_Release_Date = Film_Release_Date


class Film_Database_Backup():

    def __init__(self):

        self.connect_databse()

    def connect_databse(self):

        self.connection = sqlite3.connect("Cinemaximum.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists Tbl_Film_Backup (" \
                "Film_Name text," \
                "Film_Link text," \
                "Film_Release_Date text," \
                "Film_Time text," \
                "Film_Genre text," \
                "Film_Score text," \
                "Film_Summary text," \
                "Film_Age_Rate text," \
                "Film_EN_Name text," \
                "Film_Formats text)"

        self.cursor.execute(query)
        self.connection.commit()

    def add_movie(self,film):

        query = "insert into tbl_film_backup values (@p1,@p2,@p3,@p4,@p5,@p6,@p7,@p8,@p9,@p10)"
        self.cursor.execute(query,(film.Film_Name,film.Film_Link,film.Film_Release_Date,film.Film_Time,film.Film_Genre,film.Film_Score,film.Film_Summary,film.Film_Age_Rate,film.Film_EN_Name,film.Film_Formats))
        self.connection.commit()


    def update_movie_score(self,score,name):

        query = "update Tbl_Film_Backup set Film_Score = @p1 where Film_Name = @p2"
        self.cursor.execute(query,(score,name))
        self.connection.commit()