import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select Darbuotojas_ID FROM Darbuotojas")
    for row in cursor:
        print(f'row = {row}')
    print()

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-EGR3M9P8\MSSQLSERVER01;"
    "Database=Knygynas;"
    "Trusted_Connection=yes;"
)

read(conn)

