import sqlite3

con = sqlite3.connect('dorkx.db')

cur = con.cursor()

#for i in cur.execute('SELECT * FROM Operator_Description'):
 #   print(i)

def insertion(input_name,description): #Pour inserer dans Operator_Description 
    cur.execute(f"INSERT INTO Operator_Description VALUES ('{input_name}','{description}','{None}')")
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
def afficher_description(operator_name=None):
    tab=[]
    desc =[]
    for i in cur.execute(f"SELECT Name,Description FROM Operator_Description ;"):
        tab.append(i)
    print("[Name: ","    ", " Description]")
    print(" ")
    print(" ")
    for j in tab:
        print (j[0],' ',j[1],"\n")
        
    

#operator_name=input("operator ?")
afficher_description()
con.close()


