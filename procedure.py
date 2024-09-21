import mysql.connector
mydb = mysql.connector.connect(
user="root",
password="dimpu123",
database="demo9"
)
c = mydb.cursor()


def procedure_execute(query):
    c.execute(query)
    if "call" in query.lower():
        return None
    return c.fetchall()