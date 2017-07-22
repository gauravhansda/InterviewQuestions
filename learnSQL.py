import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE shoppingList(ItemType VARCHAR not null, ItemName VARCHAR, ItemPrice REAL)")


def enter_data():
    """

    :rtype: Nothing
    """
    c.execute("INSERT INTO shoppingList VALUES('Food','Egg',3.99)")
    c.execute("INSERT INTO shoppingList VALUES('Drink','Wine',11.99)")
    c.execute("INSERT INTO shoppingList VALUES('Electronics','headphone',15.99)")
    conn.commit()


def enter_dynamic_data():
    itemtype = raw_input("Type of item? ")
    itemname = raw_input("Name: ")
    itemprice = float(input("Price: "))

    c.execute("INSERT INTO shoppingList (ItemType, ItemName, ItemPrice) VALUES (?, ?, ?)",
              (itemtype, itemname, itemprice))

    conn.commit()

def read_from_database():
    sql = "SELECT * FROM shoppingList"
    print("Current list of items in the table: \n")
    for row in c.execute(sql):
        print row

    what_type = str(raw_input("What type of Item looking for? "))
    what_name = str(raw_input("What is the name? "))
    sql1 = 'SELECT * FROM shoppingList WHERE ItemType = ? AND ItemName = ?'
    for row in c.execute(sql1, [(what_type),(what_name)]):
        print("Required item details are: {}".format(row))


# create_table()
# enter_data()

enter_dynamic_data()
read_from_database()
conn.close()