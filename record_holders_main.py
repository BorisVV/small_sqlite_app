# BorisVV
# using sqlite3
import sqlite3
import func_options
import table_queries_func as tb_queries

# Connect to the database.
conn = sqlite3.connect("chainsawRecordHolder.db")

# Cursor connection
c = conn.cursor()

# Create table if not in the db.
# This table doesn't have the id integer autoincrement set up. 'rowid' is the id column.
c.execute('''CREATE TABLE if not exists recordtable(name text, country text, catches int)''')


def user_choice():
    ''' Let the user select an option to continue with the program.
        Update options as needed, and the main().
    '''
    options = "Choose one option to continue:\n\
    0. Exit\n\
    1. Add new.\n\
    2. Update.\n\
    3. Delete.\n\
    4. Search by name.\
  \nType a number: "

  # The user must enter a number from above or it will continue to loop.
    while True:
        print(options)
        try:
            user_input = int(input())
            if user_input in range(0, 5):
                return user_input
            else: print('Number no an option, try again.')
        except:
                print('No an option, try again.')


def main():
    # Run program and get the user imput.
    user_input = user_choice()
    # Call the correct function
    if user_input == 1:
        tb_queries.add_new_record()
    elif user_input == 2:
        tb_queries.update_table()
    elif user_input == 3:
        tb_queries.delete_row()
    elif user_input == 4:
        tb_queries.search_record_by_name()


if __name__ == '__main__':
    main()
    conn.close()
