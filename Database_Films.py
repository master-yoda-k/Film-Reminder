import sqlite3
import Colors

clr = Colors.bcolors

class Film():

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


    def __str__(self):

        return ("""
                Hey there!
                
                {} released today!

                Here is some information below:

                Release Date: {}

                Formats: {}

                Total Time: {}

                Genre: {}

                Score: {}

                Age Rate: {}

                Summary: {}

                Would you want to get ticket for it? Here is the link below to do so!

                Link: {}

                """).format(clr.BOLD + clr.OKBLUE + self.Film_Name + clr.ENDC,
                            clr.BOLD + clr.YELLOW + self.Film_Release_Date + clr.ENDC,
                            clr.BOLD + self.Film_Formats + clr.ENDC, clr.BOLD + clr.OKGREEN + self.Film_Time + clr.ENDC,
                            clr.BOLD + clr.MAGENTA + self.Film_Genre + clr.ENDC, clr.BOLD + self.Film_Score + clr.ENDC,
                            clr.BOLD + clr.RED + self.Film_Age_Rate + clr.ENDC, clr.BOLD + self.Film_Summary + clr.ENDC,
                            self.Film_Link)
        



    def text_of_mail(self,en_name,tr_name):

        if (en_name != "Not Found"):
            name = en_name
        else:
            name = tr_name

        return ("Hey there!\n\n{} released today!\n\nHere is some information below:\n\nRelease Date: {}\n\nFormats: {}\n\n"
         "Total Time: {}\n\nGenre: {}\n\nScore: {}\n\nAge Rate: {}\n\nSummary: {}\n\n"
         "Would you want to get ticket for it? Here is the link below to do so!\n\n"
         "Link: {}"
         "".format(name, self.Film_Release_Date, self.Film_Formats, self.Film_Time, self.Film_Genre,
                   self.Film_Score,
                   self.Film_Age_Rate, self.Film_Summary, self.Film_Link))


class Film_Database():

    def __init__(self):

        self.connect_databse()

    def connect_databse(self):

        self.connection = sqlite3.connect("Cinemaximum.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists Tbl_Film (" \
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


    def print_movies(self):

        query = "select * from tbl_film"
        self.cursor.execute(query)
        films = self.cursor.fetchall()

        if (len(films) != 0):

            for i in films:
                film = Film(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
                print(film)

        else:
            print("No film found on databse.")


    def add_movie(self,film):

        query = "insert into tbl_film values (@p1,@p2,@p3,@p4,@p5,@p6,@p7,@p8,@p9,@p10)"
        self.cursor.execute(query,(film.Film_Name,film.Film_Link,film.Film_Release_Date,film.Film_Time,film.Film_Genre,film.Film_Score,film.Film_Summary,film.Film_Age_Rate,film.Film_EN_Name,film.Film_Formats))
        self.connection.commit()

    def delete_movie(self,name_of_film):

        query = "delete from tbl_film where film_name = @p1"
        self.cursor.execute(query, (name_of_film,))
        self.connection.commit()

    def check_if_film_exists(self,name):

        query = "select * from tbl_film where film_name = @p1"
        self.cursor.execute(query,(name,))
        film = self.cursor.fetchall()

        if (len(film) == 0):
            return 0
        else:
            return 1

    def get_movie_info(self):

        query = "select * from tbl_film"
        self.cursor.execute(query)
        films = self.cursor.fetchall()
        return films
