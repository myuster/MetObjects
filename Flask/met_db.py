import csv
import sqlite3



data_filename = open('C:\\Users\\Max\\PycharmProjects\\MetArt\\met_df_clean.csv', 'rt', encoding="utf8")
next(data_filename, None)
reader = csv.reader(data_filename)


sql = sqlite3.connect('C:\\Users\\Max\\PycharmProjects\\MetArt\\Flask\metobjects.db')
cur = sql.cursor()


cur.execute('''DROP TABLE metobjects''')
cur.execute('''CREATE TABLE IF NOT EXISTS metobjects
    (ObjectNumber text, IsHighlight boolean, IsPublicDomain boolean, ObjectID int PRIMARY KEY,
     Department text, ObjectName text, Title text, Culture text, Period text, Dynasty text,
     Reign text, Portfolio text, ArtistRole text, ArtistPrefix text,
     ArtistDisplayName text, ArtistDisplayBio text, ArtistSuffix text,
     ArtistAlphaSort text, ArtistNationality text, ArtistBeginDate text,
     ArtistEndDate text, ObjectDate text, ObjectBeginDate text,
     ObjectEndDate text, Medium text, Dimensions text, CreditLine text,
     GeographyType text, City text, State text, County text, Country text, Region text,
     Subregion text, Locale text, Locus text, Excavation text, River text, Classification text,
     RightsReproduction text, LinkResource text, MetadataDate text,
     Repository text, Tags text, ForeignTitle text)''')


for row in reader:
    cur.execute('''INSERT INTO metobjects VALUES 
                (?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?)''',row)


cur.execute("SELECT * FROM metobjects LIMIT 10")
print("TEST SQL:", cur.fetchall())

data_filename.close()
sql.commit()
sql.close()