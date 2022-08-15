# import sqlite3, csv

# connection = sqlite3.connect("db.sqlite3", timeout=10)

# cursor = connection.cursor()

# with open('users_city.csv','r') as file:
#     no_records = 0
#     for row in file:
#         cursor.execute("INSERT OR IGNORE INTO users_city VALUES (?,?,?)", row.split(","))
#         connection.commit()
#         no_records += 1
# connection.close()