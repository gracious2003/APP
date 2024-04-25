import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('user_data.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS user_info
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   email TEXT)''')
conn.commit()

# Function to insert information into the database
def insert_information(name, age, email):
    cursor.execute('''INSERT INTO user_info (name, age, email)
                      VALUES (?, ?, ?)''', (name, age, email))
    conn.commit()
    print("Information saved successfully.")

# Main program loop
while True:
    print("\nEnter information (or type 'quit' to exit):")
    name = input("Name: ")
    if name.lower() == 'quit':
        break
    age = int(input("Age: "))
    email = input("Email: ")

    # Call function to insert information into the database
    insert_information(name, age, email)

# Close the database connection
conn.close()
