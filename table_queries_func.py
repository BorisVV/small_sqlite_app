import sqlite3
import chainsaw_record_holders as ch
import func_options as fu

display_print = "Enter the full name of the record holder."

def select_everything_query(table):
    ''' Get everything from table, and print each row including the row id.'''
    rows = ch.c.execute('''SELECT * FROM %s''' % table)
    for row in rows:
        print(row)

def everythyng_query_return(table):
    rows = ch.c.execute('SELECT * FROM %s' % table)
    return rows

def search_record_by_name():
    while True:
        print(display_print)
        # Get the name from user.
        fullname = fu.get_input_alpha()

        if fullname != None:
            row = ch.c.execute('''SELECT * FROM recordtable WHERE name = ?''', (fullname,)).fetchone()
            if row == None:
                print("Not found.")
            else: print(row)

            print("Do you want to search again? y/n")
            yes_no = fu.user_input_yes_no()
            if yes_no == False: break # if input == yes or y the loop continues.
        else: break
    return ch.main()

def add_new_record():
        print("Let's add some records")

        # While the user wants to keep adding more names/record holders
        while True:
            print(display_print)
            # Ask to enter fullname, country and number of catches.
            fullname = fu.get_input_alpha()
            if fullname == None:
                break

            inTable = False
            # Check to see if name is in table.
            nameIn = everythyng_query_return('recordtable')
            for name in nameIn:
                if fullname in name:
                    inTable = True
                    break

            if inTable == True:
                print("Name is already in data base, Enter other than %s " % fullname)
                continue

            print('Enter the country for', fullname)
            country = fu.get_input_alpha()
            if country == None:
                break

            # Get number of catches with int validator.
            print("Enter the number of catches for", fullname )
            numberOfCatches = fu.get_int()

            # collect data entered by user.
            # To store the data entered by the user.
            try:
                ch.c.execute('INSERT INTO recordtable VALUES(?,?,?)', (fullname, country, numberOfCatches))
                ch.conn.commit()
            except:
                ch.conn.rollback()
                print('A problem ocurred.')  # TODO:

            print("Do you want to add more? 'yes' to continue, or press 'Enter' to exit:")
            yes_more = fu.user_input_yes_no()
            if yes_more == False:
                break
        return ch.main()

def update_table():
    rowId = None
    while True:
        print(display_print)
        # Get the full name from user, if None, return to ch.main().
        fullname = fu.get_input_alpha()
        if fullname == None: break
        else:
            # Check to see if name is in tablea, else except, continue loop.
            try:
                getId = ch.c.execute("SELECT rowid, * FROM recordtable WHERE name = ?", (fullname,))
                rowId = getId.fetchone()[0]
            except:
                print("Your name was not found, check spelling!")
                continue

            # Make suere user only select from one of the options provided.
            print("What would you like to UPDATE? \nEnter a number from one of the options below;")
            options = '1 : "name", \n2 : "country", \n3 : "catches", "\n0 : TO EXIT \nType a number:"'
            print(options)

            while True:
                choosen = fu.get_int()
                if choosen in range(0, 4):
                    break
                else:
                    print("Number entered is not in options")

            # Update name only.
            if choosen == 1:
                print("Enter new full name")
                new_fullname = fu.get_input_alpha()
                if new_fullname == None: continue
                else:
                    ch.c.execute('''UPDATE recordtable SET name = ? WHERE rowid = ?''', (new_fullname, rowId))
                    ch.conn.commit()

            # Update country only.
            elif choosen == 2:
                print("Enter the new country for", fullname)
                new_country = fu.get_input_alpha()
                if new_country == None: continue
                else:
                    ch.c.execute('''UPDATE recordtable SET country = ? WHERE rowid = ?''', (new_country, rowId))
                    ch.conn.commit()

            # Update number of catches.
            elif choosen == 3:
                print("Enter the new record for", fullname)
                new_record = fu.get_int()
                if new_record == None: continue
                else:
                    ch.c.execute('''UPDATE recordtable SET catches = ? WHERE rowid = ?''', (new_record, rowId))
                    ch.conn.commit()

        # Option to update another record.
        print("Do you want to update a diferent record?" +
        "\n'yes' to continue or press 'Enter' to exists:")
        yesUpdate = fu.user_input_yes_no()
        if yesUpdate == False: break

    return ch.main()

def delete_row():
    print("What record would you like to delete?")
    while True:
        print("Enter the full name: ")
        fullname = fu.get_input_alpha()
        if fullname == None: break
        else:
            print("Are you sure to delete", fullname)
            yes_true = fu.user_input_yes_no()
            if yes_true:
                try:
                    ch.c.execute('''DELETE FROM recordtable WHERE name = ?''', (fullname,))
                    ch.conn.commit()
                except:
                    print("Name not found. Try again?")
                    ch.conn.rollback()
                    continue

        print("Would you like to the delete a different record? y/n")
        yes_no = fu.user_input_yes_no()
        if yes_no == False: break

    return ch.main()
