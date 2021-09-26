import sqlite3

con = sqlite3.connect('dorkx.db')

cur = con.cursor()

#for i in cur.execute('SELECT * FROM Operator_Description'):
 #   print(i)

def insertion(input_name,description): #Pour inserer dans Operator_Description 
    cur.execute(f"INSERT INTO Operator_Description VALUES ('{input_name}','{description}','{none}')")
    con.commit()
    for i in cur.execute('SELECT * FROM Operator_Description'):
        print(i)

'''  Fonction pour Inserer dans la Table Operator_Description
name= str(input('input_name?'))
desc = str(input('input_desc?'))
none = None
print(name,desc)

insertion(name,desc) 
'''

con.close()


