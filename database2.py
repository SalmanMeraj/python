import sqlite3

conn=sqlite3.connect('price.db')
#c=conn.cursor()
conn.execute('DROP TABLE IF EXISTS price')
conn.execute("CREATE TABLE price (Product text, Quantity varchar, Price varchar, Season text, Store text)")
conn.execute("INSERT INTO price VALUES ('Orange', '1lb', '$9', 'Summer', 'WalMart')")
conn.execute("INSERT INTO price VALUES ('Apple', '2.5lb', '$8', 'Winter', 'Aldi')")
conn.execute("INSERT INTO price VALUES ('Banana', '5lb', '$5', 'Fall', 'Meijer')")
conn.execute("INSERT INTO price VALUES ('Kiwi', '1.8lb', '$2.5', 'Spring', 'WalMart')")
conn.execute("INSERT INTO price VALUES ('Mango', '2lb', '$5', 'Summer', 'Aldi')")
conn.execute("INSERT INTO price VALUES ('Pineapple', '2lb', '$6', 'Summer', 'Aldi')")
conn.execute("INSERT INTO price VALUES ('Grape', '2lb', '$7', 'Winter', 'WalMart')")
conn.commit()


#result=conn.execute('SELECT * FROM price')
#print(result)
#order=conn.execute('SELECT Price FROM price order by Price')
#for row in order:
    #print(row)

## update 
conn.execute("UPDATE price SET Product='Malta' WHERE Product='Grape'")
conn.commit()

update=conn.execute('SELECT Product FROM price order by Product')
for row in update:
    print(row)