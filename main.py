# Importing required libraries/modules.
import mysql.connector as sql
from tabulate import tabulate
import random
import datetime
import time


def create_connection():
    """Create and return a connection to the database."""
    con = sql.connect(host = "localhost", username = "root", passwd = "9628", database = "components")
    if not con.is_connected():
        print("Connection to database failed.")
        exit(0)
    return con


def get_columns(cursor, tablename):
    """Fetch and return the column names of the specified table."""
    Query = (f"select column_name from information_schema.columns where table_name = '{tablename}' and table_schema = 'components'")
    cursor.execute(Query)
    data = cursor.fetchall()
    columns =[]
    for i in range(len(data)):
        columns.append((data[i][0]).upper())
    return columns


def ask_to_continue():
    """Ask the user to continue and return True or False based on their input."""
    LoopExit = False
    while True:
        ch = input("Enter(Y/N): ")
        if len(ch) == 1 and ch in 'YyNn':
            if ch.upper() == "N":
                return not(LoopExit)
            else:
                break
        else:
            print("Please Enter only(Y/N).")


def fetch_usernames():
    """Fetch and return all usernames from the database."""
    conn = cursor = None
    try:
        conn = create_connection()
        cursor = conn.cursor(buffered = True) # Buffered = True to get rid of the error - unread result found.
        query = "SELECT username,password FROM users"
        cursor.execute(query)
        usernames = cursor.fetchall()

        usrname = {}
        for i,j in usernames:
            usrname[i] = j

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return usrname


def validate_email(email):
    """To validate an email address."""
    if "@" in email and "." in email:
        if len(email.split("@")[0]) < 4 or len(email.split("@")[1]) < 3:
            return False
        else:
            return True
    else:
        return False
                

def validate_password(passwd):
    '''For passsword validation'''
    l = u = d = s = 0   # lowercase, uppercase, digit, specialchr respectively.
    if len(passwd) <= 8 and len(passwd) >= 20:
        return False
    else:
        for i in passwd:
            if i.isalpha():
                if i.islower():
                    l += 1
                else:
                    u += 1
            elif i.isdigit():
                d += 1
            else:
                s += 1
        
        if l >= 1 and u >= 1 and d >= 1 and s >= 1:
            return True
        else:
            return False


def insert_user_record(name, username, password = None, email = None):
    """Insert user record into the database."""
    conn = cursor = None
    try:
        dt = datetime.datetime.now() # Inserting date and time of users first signup.
        date = dt.strftime("%Y-%m-%d")
        time = dt.strftime("%I:%M %p")
        conn = create_connection()
        cursor = conn.cursor(buffered = True)
        query = f"INSERT INTO Users VALUES('{name}', '{username}', '{password}', '{email}', '{date}', '{time}')"
        cursor.execute(query)
        conn.commit()

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def Guest():
    """To create unique and random guest id."""
    try:
        name = "Guest"
        Gid = random.random()
        Gname = name + str(int(Gid * 1000000))
        nmaes = fetch_usernames()
        while (Gname in nmaes.keys()):
            Gid = random.random()
            Gname = name + str(int(Gid * 1000000))
        insert_user_record(name, Gname)
        return Gname
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")


def SignUp():
    """For sign up of new users."""
    try:
        while True:
            print("==============================")
            name = input("Enter your name: ")

            email = input("Enter your email: ")
            while not validate_email(email):
                print("==============================")
                print("Invalid email! Username must be at least 4 characters and domain must be at least 3 characters.")
                email = input("Enter your email: ")

            username = input("Enter your username: ")
            usrnmaes = fetch_usernames()
            while (username in usrnmaes.keys()):
                print("==============================")
                print("Username already exists! Please choose another one.")
                username = input("Enter your username: ")

            password = input("Create password: ")
            while not validate_password(password):
                print("==============================")
                print("Invalid password! Password must be between 9 and 19 characters long, and contain at least one digit, one uppercase letter, one lowercase letter, and one special character.") 
                password = input("Create password: ")
            else:
                confirm_password = input("Confirm your password: ")
                while password != confirm_password:
                    print("==============================")
                    print("Password do not match!")
                    confirm_password = input("Confirm your password: ")
                else:
                    print("==============================")
                    print("SignUp succesful!")
                    print("Now you can Login.")
                    print("==============================")
                    break

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")

    insert_user_record(name, username, password, email)


def LogIn():
    """For log in of existing users."""
    try:
        LoopExit = False
        while True:
            if LoopExit:
                break
            print("=======WELCOME BACK=======")
            username = input("Enter your username: ")
            usrnmaes = fetch_usernames()
            while not (username in usrnmaes.keys()):
                print("==============================")
                print("Username does not exist!")
                username = input("Enter your username(0 exit): ")
                if username == "0":
                    LoopExit = True
                    break
            else:
                password = input("Enter your password: ")
                if usrnmaes[username] == password:
                    print("==============================")
                    print("LogIn succesful!")
                    return username
                else:
                    print("==============================")
                    print("Wrong password!")
                
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")


def InsertRec():
    """Inserts a new record into the database."""
    conn = create_connection() # Creating connection with the 'create_connection' function.
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to insert record (0 to exit): ")
            if tablename.lower() in ('gpus', 'cpus', 'storages', 'psu', 'memory', 'motherboard'):
                while True:
                    cursor = conn.cursor(buffered = True)# Buffered = True to get rid of the error - unread result found.

                    # Getting columns name of specified table with 'get_columns' function.
                    columns = get_columns(cursor, tablename)

                    # Taking input for differnt column from user.
                    print("==============================")
                    values = []
                    for i in range(len(columns) - 1):
                        column = columns[i]
                        values.append(input(f"Enter {column}: "))
                    values.append(float(input(f"Enter {columns[-1]}: "))) # Assuming last column is a float
                    print("==============================")

                    # To create dynamic query acoording to the number of columns
                    placeholder = (("%s,")*(len(columns)-1))+("%s")
                    query = f"insert into {tablename} values({placeholder})"
                    cursor.execute(query,values)
                    conn.commit()
                    cursor.close()
                    print("RECORD INSERTED SUCCESSFULLY.")
                    
                    print("Do you want to insert more records in this table ?")
                    if ask_to_continue(): # Asking user to continue or not.
                        break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e: # Except statement if any error comes somehow.
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close() # Clsoing the connection.


def UpdateRec():
    """Updates a record in the database."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to update record (0 to exit): ")
            if tablename.lower() in ('gpus', 'cpus', 'storages', 'psu', 'memory', 'motherboard'):
                while True:
                    cursor = conn.cursor(buffered = True)
                    
                    columns = get_columns(cursor, tablename)

                    modeln = input(f"Enter modle number to update from {tablename}: ")
                    # To show user existing record before updating.
                    query = f"select * from {tablename} where model = '{modeln}'"
                    cursor.execute(query)
                    rec = cursor.fetchall()
                    count = cursor.rowcount
                    
                    if count == 0:
                        print("Record not found.")
                        break
                    else:
                        print("=========RECORD FOUND=========")
                        table =  tabulate(rec, headers = columns, tablefmt="psql")
                        print(table)
                        print("==============================")

                        # Taking updated/new values for the record.
                        print("Enter new values for this record.")
                        values = []
                        for i in range(len(columns) - 1):
                            column = columns[i]
                            values.append(input(f"Enter new {column}: "))
                        values.append(float(input(f"Enter {columns[-1]}: "))) 
                        # Assuming last column is a float
                        print("==============================")
                        
                        # To create a dynamic update query according to the table.
                        Q = f"update {tablename} set "
                        for i in columns:
                            if i != columns[-1]:
                                q = i+" = %s, "
                                Q += q
                        query = Q + columns[-1] + "= %s " + (f"where Model = '{modeln}'") # Dynamic update query.

                        cursor.execute(query,values)
                        conn.commit()
                        print("RECORD UPDATED SUCCESSFULLY.")
                        print("==============================")
                    cursor.close()

                    print("Do you want to update more records in this table ?")
                    if ask_to_continue():
                        break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()
    

def DisplayRec():
    """Displays the record from datbase."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table to display records(0 to exit): ")
            if tablename.lower() in ('gpus', 'cpus', 'storages', 'psu', 'memory', 'motherboard'):
                cursor = conn.cursor(buffered = True)

                columns = get_columns(cursor, tablename)

                N = int(input("Enter number of records you want to display(0 for all): "))
                query = f"select * from {tablename}"
                if N == 0:
                    cursor.execute(query)
                    data = cursor.fetchall()
                else:
                    cursor.execute(query)
                    data = cursor.fetchmany(N)

                count = cursor.rowcount
                if count == 0:
                    print("No records found.")
                else:
                    table = tabulate(data, headers = columns, tablefmt = "psql")
                    print("==============================")
                    print(f"TABLE: {tablename.upper()}")
                    print(f"Number of records fetched: {count}")
                    print(table)
                    print("==============================")
                        
                cursor.close()

                print("Do you want to diplay more records ?")
                if ask_to_continue():
                    break

            elif tablename == "0":
                break
            else:
                print("No such table exist.")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def SearchRec():
    """Serarches a record in the database."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to perform search (0 to exit): ")
            if tablename.lower() in ('gpus', 'cpus', 'storages', 'psu', 'memory', 'motherboard'):
                while True:
                    print("==============================")
                    cursor = conn.cursor(buffered = True)

                    columns = get_columns(cursor, tablename)

                    print("Columns of table are:",end = " ")
                    for column in columns:
                        if column == columns[-1]:
                            print(column)
                        else:
                            print(column, end = ", ")
                    
                    colname = input("Enter name of the columns: ")
                    print("==============================")
                    if colname.upper() not in columns:
                        print("Invalid column name.")
                    else:
                        if colname.upper() == columns[-1]:
                            val = float(input(f"Enter {colname} to search: "))
                            query = f"select * from {tablename} where {colname} = {val}"
                        else:
                            val = input(f"Enter {colname} to search: ")
                            query = f"select * from {tablename} where {colname} like '%{val}%'"

                        cursor.execute(query)
                        rec = cursor.fetchall()
                        count = cursor.rowcount
                        if count == 0:
                            print("RECORD NOT FOUND.")
                            print("==============================")
                        else:
                            table = tabulate(rec, headers = columns, tablefmt="psql")
                            print("========Search Results========")
                            print(f"TABLE: {tablename.upper()}")
                            print(f"Number of records found: {count}")
                            print(table)
                            print("==============================")

                    cursor.close()

                    print("Do you want to search more records in this table ?")
                    if ask_to_continue():
                        break
                    
            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def DeleteRec():
    """Deletes the record from the database."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to delete record (0 to exit): ")
            if tablename.lower() in ('gpus', 'cpus', 'storages', 'psu', 'memory', 'motherboard'):
                cursor = conn.cursor(buffered = True)
                
                columns = get_columns(cursor, tablename)

                modeln = input(f"Enter modle number of record to delete from {tablename}: ")
                print("==============================")
                # To show user record before deleteing.
                query = "select * from {} where model = '{}'".format(tablename, modeln)
                cursor.execute(query)
                rec = cursor.fetchall()
                count = cursor.rowcount # To check if there is such record or not.
                if count == 0:
                    print("Record not found.")
                    print("==============================")
                else:
                    print("=========RECORD FOUND=========")
                    table =  tabulate(rec, headers = columns, tablefmt="psql")
                    print(table)
                    print("==============================")
                    # Confirming if user really wants to delete the record.
                    print("Are you sure taht you want to delete this record ?")
                    confirm = not(ask_to_continue())
                    if confirm == True:
                        query = f"delete from {tablename} where model = '{modeln}'"
                        cursor.execute(query)
                        conn.commit()
                        print("========RECORD DELETED========")
                    else:
                        print("==============================")
                        print("Record deletion cancelled..")
                        print("==============================")

                cursor.close()

                print("Do you want to delete more records ?")
                if ask_to_continue():
                    break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def select_cpu():
    """For selecting a cpu from the database"""
    conn = cursor = None
    user_cpu = [] # For storing details of user selected CPU
    while True:
        try:
            print("======STARTING WITH CPUS======")
            print("Select CPU brand.")
            print("Press 1 - AMD")
            print("Press 2 - Intel")
            print("==============================")
            ch = int(input("Enter(1/2): "))
            if ch == 1:
                cpu_brand = "AMD"
            elif ch == 2:
                cpu_brand = "INT"
            else:
                raise ValueError

            # Asking for CPU core and thread
            print("==============================")
            cpu_core = int(input("Enter number of cores: "))
            cpu_thread = int(input("Enter number of threads: "))
            max_cpu_core = cpu_core + 4
            max_cpu_thread = cpu_thread + 8
            print("==============================")
            break
                
        except ValueError:
            print("==============================")
            print("Wrong Input.")
            print("Please Enter only in digit.")
            print("==============================")
    try:
        conn = create_connection()
        cursor = conn.cursor(buffered = True)
        
        cpu_query = f"SELECT * FROM cpus WHERE Model LIKE '%{cpu_brand}%' AND core BETWEEN {cpu_core} AND {max_cpu_core} AND thread BETWEEN {cpu_thread} AND {max_cpu_thread}"
        cursor.execute(cpu_query)
        cpus_data = cursor.fetchall()

        if not cpus_data:
            print("No CPU found matching your criteria.")
            return

        column_names = get_columns(cursor, "cpus")
        table = tabulate(cpus_data, headers = column_names, tablefmt = "psql")
        print("Available CPUs are:")
        print(table)

        ModelNos = []
        for i in cpus_data:
            ModelNos.append(i[5])   
        
        print("==============================")
        user_cpu_model = input("Enter model number of cpu to select: ")
        while not (user_cpu_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_cpu_model = input("Enter model number of cpu to select: ")
            print("==============================")
            
        else:
            for c in cpus_data:
                if c[5] == user_cpu_model.upper():
                    for v in range(len(c)-1):
                        user_cpu.append(c[v])
                    user_cpu.append(float(c[-1]))
                    print("Successfully selceted..")
                    break
            
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        
    return user_cpu

        
def select_gpu():
    """For selecting a graphic card from the database."""
    conn = cursor = None
    user_gpu = [] # For storing details of user selected GPU
    while True:
        try:
            # Selecting GPU brand.
            print("==============================")
            print("=========TIME FOR GPU=========")
            print("Select GPU brand.")
            print("Press 1 - AMD")
            print("Press 2 - NVIDIA")
            print("==============================")
            ch = int(input("Enter(1/2): "))
            if ch == 1:
                gpu_brand = "Radeon"
            elif ch == 2:
                gpu_brand = "GeForce"
            else:
                raise ValueError

            # Asking for minimum VRAM
            vram = int(input("Enter required VRAM(in GB): "))
            req_vram = str(vram)+"Gb"
            print("==============================")
            break
                
        except ValueError:
            print("==============================")
            print("Wrong Input.")
            print("Please Enter only in digit.")
            print("==============================")
    try:
        conn = create_connection()
        cursor = conn.cursor(buffered=True)
        
        column_names = get_columns(cursor, "gpus")
        
        gpu_query = f"SELECT * FROM gpus WHERE prefix = '{gpu_brand}' AND memory LIKE '{req_vram}%'"
        cursor.execute(gpu_query)
        gpus_data = cursor.fetchall()

        if not gpus_data:
            print("No GPUs found matching your criteria.")
            return  # Exit the function if no GPUs are found

        # Display the found GPUs in a table format
        table = tabulate(gpus_data, headers=column_names, tablefmt="psql")
        print("Available GPUs are:")
        print(table)

        ModelNos = []
        for i in gpus_data:
            ModelNos.append(i[3])  # Assuming the model number is at index 4

        print("==============================")
        user_gpu_model = input("Enter model number of gpu to select: ")
        while not (user_gpu_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_gpu_model = input("Enter model number of gpu to select: ")
            print("==============================")
            
        else:
            for c in gpus_data:
                if c[3] == user_gpu_model.upper():
                    for v in range(len(c)-1):
                        user_gpu.append(c[v])
                    user_gpu.append(float(c[-1]))
                    print("Successfully selceted..")
                    break
            
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

    return user_gpu


def select_mb(cpu):
    """For selecting a moherboard based on he cpu from the database."""
    conn = cursor = None
    user_mb = [] # For storing details of user selected Motherboard
    try:
        cpu_socket = cpu[4]

        print("==============================")
        print("======NOW ON MOTHERBOARDS=====")
        print("Available Motherboards for your CPU:")

        conn = create_connection()
        cursor = conn.cursor(buffered=True)

        # Query to find motherboards that match the CPU socket
        mb_query = f"SELECT * FROM motherboard WHERE socket = '{cpu_socket}'"
        cursor.execute(mb_query)
        motherboards_data = cursor.fetchall()

        if not motherboards_data:
            print("No motherboards found matching your CPU socket.")
            return  # Exit the function if no motherboards are found

        # Display the found motherboards in a table format
        column_names = get_columns(cursor, "motherboard")
        table = tabulate(motherboards_data, headers=column_names, tablefmt="psql")
        print(table)

        ModelNos = []
        for i in motherboards_data:
            ModelNos.append(i[4])  # Assuming the model number is at index 4

        print("==============================")
        user_mb_model = input("Enter model number of motherboard to select: ")
        while not (user_mb_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_mb_model = input("Enter model number of motherboard to select: ")
            print("==============================")
        else:
            for c in motherboards_data:
                if c[4] == user_mb_model.upper():
                    for v in range(len(c)-1):
                        user_mb.append(c[v])
                    user_mb.append(float(c[-1]))
                    print("Successfully selceted..")
                    break
            
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        
    return user_mb


def select_mem(mb):
    """For selecting the compatiable RAM from the datbase."""
    conn = cursor = None
    user_mem = []# For storing details of user selected Memory
    try:
        mb_mem_type = mb[3]

        print("==============================")
        print("========TO GET MEMORY=========")
        ram_per_slot = int(input("Enter memory you want per slot (in GB): "))
        module_no = int(input("Enter the number of memory module required: "))
        while not module_no != 0:
            print("Number of memory module can't be zero!")
            module_no = int(input("Enter the number of memory module required: "))
            
        total_ram = ram_per_slot * module_no
        mem_per_slot = str(ram_per_slot)+"Gb"
        print("==============================")

        conn = create_connection()
        cursor = conn.cursor(buffered=True)

        # Query to find memory that match the motherboard memory type
        mem_query = f"SELECT * FROM memory WHERE type LIKE '%{mb_mem_type}%' AND capacity = '{mem_per_slot}'"
        cursor.execute(mem_query)
        memory_data = cursor.fetchall()

        if not memory_data:
            print("No memory found matching your motherboard memory type.")
            return  # Exit the function

        column_names = get_columns(cursor, "memory")
        table = tabulate(memory_data, headers=column_names, tablefmt="psql")
        print("Available Memory modules:")
        print(table)

        ModelNos = []
        for i in memory_data:
            ModelNos.append(i[4])  # Assuming the model number is at index 4

        print("==============================")
        user_mem_model = input("Enter model number of memory to select: ")
        while not (user_mem_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_mem_model = input("Enter model number of memory to select: ")
            print("==============================")
        else:
            for c in memory_data:
                if c[4] == user_mem_model.upper():
                    for v in range(len(c)-1):
                        user_mem.append(c[v])
                    user_mem.append(float(c[-1]))
                    print("Successfully selceted..")
                    break

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        
    return user_mem, module_no


def select_storage():
    """For selecting a storage device from the database."""
    conn = cursor = None
    user_storage = []  # For storing details of user selected storage.
    try:
        print("========TIME FOR STORAGE======")
        print("Select storage type.")
        print("Press 1 - HDD")
        print("Press 2 - SSD")
        print("Press 3 - NVMe M.2")
        print("==============================")
        
        # User input for storage type.
        ch = int(input("Enter(1/2): "))
        if ch == 1:
            storage_type = "HDD"
        elif ch == 2:
            storage_type = "Sata SSD"
        elif ch == 3:
            storage_type = "NVMe M.2"
        else:
            raise ValueError

        # Asking for required storage capacity.
        print("==============================")
        required_capacity = int(input("Enter required storage capacity (in GB): "))
        capacity = str(required_capacity)+"GB"
        print("==============================")

        conn = create_connection()
        cursor = conn.cursor(buffered = True)

        # Query to find storage devices that match the selected type and capacity.
        storage_query = f"SELECT * FROM storages WHERE type = '{storage_type}' AND capacity = '{capacity}'"
        cursor.execute(storage_query)
        storage_data = cursor.fetchall()

        if not storage_data:
            print("No storage devices found matching your criteria.")
            return  # Exit the function if no storage devices are found.

        # Display the found storage devices in a table format.
        column_names = get_columns(cursor, "storages")
        table = tabulate(storage_data, headers=column_names, tablefmt="psql")
        print("Available Storage Devices are:")
        print(table)

        ModelNos = []
        for i in storage_data:
            ModelNos.append(i[4])

        print("==============================")
        user_storage_model = input("Enter model number of storage to select: ")
        while not (user_storage_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_storage_model = input("Enter model number of storage to select: ")
            print("==============================")
        else:
            for c in storage_data:
                if c[4] == user_storage_model.upper():
                    for v in range(len(c)-1):
                        user_storage.append(c[v])
                    user_storage.append(float(c[-1]))
                    print("Successfully selceted..")
                    break

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

    return user_storage


def select_psu(cpu, gpu):
    """For selecting PSU based on other components from the database."""
    conn = cursor = None
    user_psu = [] # For storing details of user selected PSU
    try:
        other_wattage = 300
        cpu_wattage = cpu[-2]
        gpu_wattage = gpu[-2]
        total_wattage = cpu_wattage + gpu_wattage + other_wattage
        max_total_wattage = total_wattage + 200

        conn = create_connection()
        cursor = conn.cursor(buffered = True)

        # Query to find power supplies that match the total wattage
        psu_query = f"SELECT * FROM psu WHERE wattage BETWEEN {total_wattage} AND {max_total_wattage}"
        cursor.execute(psu_query)
        psu_data = cursor.fetchall()

        if not psu_data:
            print("No power supplies found that match the total wattage of the system.")
            return 

        column_names = get_columns(cursor, "psu")
        table = tabulate(psu_data, headers=column_names, tablefmt="psql")
        print("==============================")
        print("Atlast select Power Supply unit from below:")
        print(table)

        ModelNos = []
        for i in psu_data:
            ModelNos.append(i[3])  # Assuming the model number is at index 3

        print("==============================")
        user_psu_model = input("Enter model number of power supply to select: ")
        while not (user_psu_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_psu_model = input("Enter model number of power supply to select: ")
            print("==============================")
        else:
            for c in psu_data:
                if c[3] == user_psu_model.upper():
                    for v in range(len(c)-1):
                        user_psu.append(c[v])
                    user_psu.append(float(c[-1]))
                    print("Successfully selceted..")
                    break
        
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return user_psu


def users_pc(usrname):
    """Insert the selected components of a user in te database."""
    conn = cursor = u_cpu = u_mb = u_mem = u_gpu = u_storage = u_psu = None
    try:
        u_cpu = select_cpu()
        u_mb = select_mb(u_cpu)
        u_mem = select_mem(u_mb)
        u_gpu = select_gpu()
        u_storage = select_storage()
        u_psu = select_psu(u_cpu, u_gpu)

        u_parts = {"CPU": u_cpu, "GPU": u_gpu, "Motherboard": u_mb, "Power supply": u_psu, "Memory Module": u_mem[0]}
        print("==============================")
        
        print("Selected components are:")
        user_parts_list = []
        for x,y in u_parts.items():
            user_parts_list.append(y[0])
            print(x, ":", y[0])
        print(f"Number of Modules : {u_mem[1]}")
        print(f"Storage Device : {u_storage[0]}")
        print(f"Storage Capacity : {u_storage[1]}")
        
        print()
        total_price = u_cpu[-1] + u_gpu[-1] + u_mb[-1] + ((u_mem[0][-1]) * u_mem[1]) + u_psu[-1] + u_storage[-1]
        print(f"Price of all components: approximately is {total_price} inr")
        print("==============================")

        dt = datetime.datetime.now()
        date = dt.strftime("%Y-%m-%d")

        conn = create_connection()
        cursor = conn.cursor(buffered = True)
        query = f"INSERT INTO users_pc VALUES('{usrname}', '{user_parts_list[0]}', '{user_parts_list[1]}', '{user_parts_list[2]}', '{user_parts_list[4]}', '{u_mem[1]}', '{u_storage[1]}', '{user_parts_list[3]}', {total_price}, '{date}')"
        cursor.execute(query)
        conn.commit()
        
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def see_others_pc():
    """Show all the PCs of other users in the database."""
    conn = cursor = None
    try:
        conn = create_connection()
        cursor = conn.cursor(buffered = True)
        column_names = get_columns(cursor, "users_pc")
        req_column_names = column_names[1:9]
        query = "SELECT CPU,GPU,MotherBoard,MemModule,NumberOfModule,StorageCapcity,PSU,TotalPrice FROM users_pc"
        cursor.execute(query)
        data = cursor.fetchall()
        print("==============================")
        print("Other users PC Builts are:")
        table = tabulate(data, headers=req_column_names, tablefmt="psql")
        print(table)
        print("==============================")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def pc_menu(usrname):
    """Show the menu for the user to select their PC build."""
    while True:
        print("==============================")
        print("Press 1 - Create PC")
        print("Press 2 - See Otehrs PC Build")
        print("Press 3 - To Exit")
        print("==============================")
        try:
            Choice = int(input("Enter your choice: "))
            if Choice == 1:
                users_pc(usrname)
            elif Choice  == 2:
                see_others_pc()
            elif Choice == 3:
                print("==============================")
                print("Thanks to visit.")
                print("==============================")
                time.sleep(10)
                exit(0)
            else:
                raise ValueError
        except ValueError:
            print("==============================")
            print("Wrong input!")
            print("Please Enter only digit(1-3)")
            print("==============================")


def admin_menu():
    """Show the menu for the admin to select their action."""
    passcode = "9628"
    i = input("Enter password to get access to database: ")
    if passcode == i:
        print("==============================")
        print("Access Granted!")
        print("==============================")
        while True:
            print("=======SELECT OPERATION=======")
            print("Press 1 - Insert data")
            print("Press 2 - update data")
            print("Press 3 - Display data")
            print("Press 4 - Search data")
            print("Press 5 - Delete data")
            print("Press 6 - To Exit")
            print("==============================")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    InsertRec()
                elif choice == 2:
                    UpdateRec()
                elif choice == 3:
                    DisplayRec()
                elif choice == 4:
                    SearchRec()
                elif choice == 5:
                    DeleteRec()
                elif choice == 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("==============================")
                print("Wrong input!")
                print("Please Enter only digit(1-6)")
                print("==============================")
    else:
        print("==============================")
        print("Wrong password! Access denied!")
        print("==============================")


def Main_Menu():
    """Show the main menu for the user to select their action."""
    print("==============================")
    print("CUSTOM PC BUILD")


    while True:
        print("==============================")
        print("Press 1 - Log In")
        print("Press 2 - Sign Up")
        print("Press 3 - Continue as Guest")
        print("Press 4 - Access DataBase(Admin)")
        print("Press 5 - To Exit")
        print("==============================")
        try:
            Choice = int(input("Enter your choice: "))
            if Choice == 1:
                usrname = LogIn()
                if usrname:
                    pc_menu(usrname)
            elif Choice == 2:
                SignUp()
            elif Choice == 3:
                gname = Guest()
                if gname:
                    pc_menu(gname)
            elif Choice == 4:
                admin_menu()
            elif Choice == 5:
                print("==============================")
                print("Thanks to visit.")
                print("==============================")
                time.sleep(10)
                exit(0)
            else:
                raise ValueError
        except ValueError:
            print("==============================")
            print("Wrong input!")
            print("Please Enter only digit(1-5)")
            print("==============================")

Main_Menu() # Calling the Main_Menu.
