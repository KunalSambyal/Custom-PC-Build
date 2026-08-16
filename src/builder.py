import datetime
import time
from tabulate import tabulate

from src.database import create_connection, get_columns


def select_cpu():
    """For selecting a cpu from the database"""
    conn = cursor = None
    user_cpu = []  # For storing details of user selected CPU
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
        cursor = conn.cursor(buffered=True)

        cpu_query = f"SELECT * FROM cpus WHERE Model LIKE '%{cpu_brand}%' AND core BETWEEN {cpu_core} AND {max_cpu_core} AND thread BETWEEN {cpu_thread} AND {max_cpu_thread}"
        cursor.execute(cpu_query)
        cpus_data = cursor.fetchall()

        if not cpus_data:
            print("No CPU found matching your criteria.")
            return

        column_names = get_columns(cursor, "cpus")
        table = tabulate(cpus_data, headers=column_names, tablefmt="psql")
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
                    for v in range(len(c) - 1):
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
    user_gpu = []  # For storing details of user selected GPU
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
            req_vram = str(vram) + "Gb"
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
            ModelNos.append(i[3])  # Assuming the model number is at index 3

        print("==============================")
        user_gpu_model = input("Enter model number of gpu to select: ")
        while not (user_gpu_model.upper() in ModelNos):
            print("Invalid model number selected.")
            user_gpu_model = input("Enter model number of gpu to select: ")
            print("==============================")

        else:
            for c in gpus_data:
                if c[3] == user_gpu_model.upper():
                    for v in range(len(c) - 1):
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
    user_mb = []  # For storing details of user selected Motherboard
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
                    for v in range(len(c) - 1):
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
    user_mem = []  # For storing details of user selected Memory
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
        mem_per_slot = str(ram_per_slot) + "Gb"
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
                    for v in range(len(c) - 1):
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
        capacity = str(required_capacity) + "GB"
        print("==============================")

        conn = create_connection()
        cursor = conn.cursor(buffered=True)

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
                    for v in range(len(c) - 1):
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
    user_psu = []  # For storing details of user selected PSU
    try:
        other_wattage = 300
        cpu_wattage = cpu[-2]
        gpu_wattage = gpu[-2]
        total_wattage = cpu_wattage + gpu_wattage + other_wattage
        max_total_wattage = total_wattage + 200

        conn = create_connection()
        cursor = conn.cursor(buffered=True)

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
                    for v in range(len(c) - 1):
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

        u_parts = {
            "CPU": u_cpu,
            "GPU": u_gpu,
            "Motherboard": u_mb,
            "Power supply": u_psu,
            "Memory Module": u_mem[0],
        }
        print("==============================")

        print("Selected components are:")
        user_parts_list = []
        for x, y in u_parts.items():
            user_parts_list.append(y[0])
            print(x, ":", y[0])
        print(f"Number of Modules : {u_mem[1]}")
        print(f"Storage Device : {u_storage[0]}")
        print(f"Storage Capacity : {u_storage[1]}")

        print()
        total_price = (
            u_cpu[-1]
            + u_gpu[-1]
            + u_mb[-1]
            + ((u_mem[0][-1]) * u_mem[1])
            + u_psu[-1]
            + u_storage[-1]
        )
        print(f"Price of all components: approximately is {total_price} inr")
        print("==============================")

        dt = datetime.datetime.now()
        date = dt.strftime("%Y-%m-%d")

        conn = create_connection()
        cursor = conn.cursor(buffered=True)
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
        cursor = conn.cursor(buffered=True)
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
            elif Choice == 2:
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
