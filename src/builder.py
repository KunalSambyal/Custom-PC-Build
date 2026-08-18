"""PC Component Selection and Custom PC Builder module."""

import datetime
import time
from typing import Any, List, Optional, Tuple
from tabulate import tabulate

from src.constants import CPU_BRANDS, GPU_BRANDS, STORAGE_TYPES
from src.dao import (
    fetch_all_users_pcs,
    fetch_filtered_cpus,
    fetch_filtered_gpus,
    fetch_memory_by_type_and_capacity,
    fetch_motherboards_by_socket,
    fetch_psu_by_wattage,
    fetch_storage_by_type_and_capacity,
    fetch_table_columns,
    insert_user_pc_build,
)
from src.utils import choose_component_by_model, handle_cli_error, prompt_int


@handle_cli_error
async def select_cpu() -> Optional[List[Any]]:
    """Interactive CPU selection filtered by brand, cores, and threads.

    Returns:
        Optional[List[Any]]: Selected CPU details list, or None if cancelled/empty.
    """
    print("======STARTING WITH CPUS======")
    print("Select CPU brand.")
    print("Press 1 - AMD")
    print("Press 2 - Intel")
    print("==============================")
    ch = prompt_int("Enter(1/2): ", valid_range=(1, 2), error_message="Wrong Input.\nPlease Enter only in digit.")
    cpu_brand = CPU_BRANDS[ch]

    print("==============================")
    cpu_core = prompt_int("Enter number of cores: ")
    cpu_thread = prompt_int("Enter number of threads: ")
    max_cpu_core = cpu_core + 4
    max_cpu_thread = cpu_thread + 8
    print("==============================")

    cpus_data = await fetch_filtered_cpus(
        cpu_brand, cpu_core, max_cpu_core, cpu_thread, max_cpu_thread
    )

    if not cpus_data:
        print("No CPU found matching your criteria.")
        return None

    columns = await fetch_table_columns("cpus")
    table = tabulate(cpus_data, headers=columns, tablefmt="psql")
    print("Available CPUs are:")
    print(table)

    return choose_component_by_model(cpus_data, 5, "cpu")


@handle_cli_error
async def select_gpu() -> Optional[List[Any]]:
    """Interactive GPU selection filtered by brand and minimum VRAM.

    Returns:
        Optional[List[Any]]: Selected GPU details list, or None if cancelled/empty.
    """
    print("==============================")
    print("=========TIME FOR GPU=========")
    print("Select GPU brand.")
    print("Press 1 - AMD")
    print("Press 2 - NVIDIA")
    print("==============================")
    ch = prompt_int("Enter(1/2): ", valid_range=(1, 2), error_message="Wrong Input.\nPlease Enter only in digit.")
    gpu_brand = GPU_BRANDS[ch]

    vram = prompt_int("Enter required VRAM(in GB): ")
    req_vram = str(vram) + "Gb"
    print("==============================")

    gpus_data = await fetch_filtered_gpus(gpu_brand, req_vram)

    if not gpus_data:
        print("No GPUs found matching your criteria.")
        return None

    column_names = await fetch_table_columns("gpus")
    table = tabulate(gpus_data, headers=column_names, tablefmt="psql")
    print("Available GPUs are:")
    print(table)

    return choose_component_by_model(gpus_data, 3, "gpu")


@handle_cli_error
async def select_motherboard(cpu: List[Any]) -> Optional[List[Any]]:
    """Interactive Motherboard selection filtered by CPU socket compatibility.

    Args:
        cpu (List[Any]): Previously selected CPU row containing socket info.

    Returns:
        Optional[List[Any]]: Selected Motherboard details list, or None.
    """
    cpu_socket = cpu[4]

    print("==============================")
    print("======NOW ON MOTHERBOARDS=====")
    print("Available Motherboards for your CPU:")

    motherboards_data = await fetch_motherboards_by_socket(cpu_socket)

    if not motherboards_data:
        print("No motherboards found matching your CPU socket.")
        return None

    column_names = await fetch_table_columns("motherboard")
    table = tabulate(motherboards_data, headers=column_names, tablefmt="psql")
    print(table)

    return choose_component_by_model(motherboards_data, 4, "motherboard")


@handle_cli_error
async def select_memory(motherboard: List[Any]) -> Tuple[Optional[List[Any]], int]:
    """Interactive RAM selection matching the motherboard memory generation.

    Args:
        motherboard (List[Any]): Previously selected Motherboard details.

    Returns:
        Tuple[Optional[List[Any]], int]: Selected RAM details and number of modules.
    """
    mb_mem_type = motherboard[3]

    print("==============================")
    print("========TO GET MEMORY=========")
    ram_per_slot = int(input("Enter memory you want per slot (in GB): "))
    module_no = int(input("Enter the number of memory module required: "))
    while module_no == 0:
        print("Number of memory module can't be zero!")
        module_no = int(input("Enter the number of memory module required: "))

    mem_per_slot = str(ram_per_slot) + "Gb"
    print("==============================")

    memory_data = await fetch_memory_by_type_and_capacity(mb_mem_type, mem_per_slot)

    if not memory_data:
        print("No memory found matching your motherboard memory type.")
        return None, 0

    column_names = await fetch_table_columns("memory")
    table = tabulate(memory_data, headers=column_names, tablefmt="psql")
    print("Available Memory modules:")
    print(table)

    user_mem = choose_component_by_model(memory_data, 4, "memory")
    return user_mem, module_no


@handle_cli_error
async def select_storage() -> Optional[List[Any]]:
    """Interactive Storage device selection (HDD, SATA SSD, NVMe M.2).

    Returns:
        Optional[List[Any]]: Selected storage details list, or None.
    """
    print("========TIME FOR STORAGE======")
    print("Select storage type.")
    print("Press 1 - HDD")
    print("Press 2 - SSD")
    print("Press 3 - NVMe M.2")
    print("==============================")

    ch = prompt_int("Enter(1/2): ", valid_range=(1, 3))
    storage_type = STORAGE_TYPES[ch]

    print("==============================")
    required_capacity = int(input("Enter required storage capacity (in GB): "))
    capacity = str(required_capacity) + "GB"
    print("==============================")

    storage_data = await fetch_storage_by_type_and_capacity(storage_type, capacity)

    if not storage_data:
        print("No storage devices found matching your criteria.")
        return None

    column_names = await fetch_table_columns("storages")
    table = tabulate(storage_data, headers=column_names, tablefmt="psql")
    print("Available Storage Devices are:")
    print(table)

    return choose_component_by_model(storage_data, 4, "storage")


@handle_cli_error
async def select_psu(cpu: List[Any], gpu: List[Any]) -> Optional[List[Any]]:
    """Interactive Power Supply selection based on total system component wattage.

    Args:
        cpu (List[Any]): Selected CPU details containing TDP.
        gpu (List[Any]): Selected GPU details containing TDP.

    Returns:
        Optional[List[Any]]: Selected PSU details list, or None.
    """
    other_wattage = 300
    cpu_wattage = cpu[-2]
    gpu_wattage = gpu[-2]
    total_wattage = cpu_wattage + gpu_wattage + other_wattage
    max_total_wattage = total_wattage + 200

    psu_data = await fetch_psu_by_wattage(total_wattage, max_total_wattage)

    if not psu_data:
        print("No power supplies found that match the total wattage of the system.")
        return None

    column_names = await fetch_table_columns("psu")
    table = tabulate(psu_data, headers=column_names, tablefmt="psql")
    print("==============================")
    print("Atlast select Power Supply unit from below:")
    print(table)

    return choose_component_by_model(psu_data, 3, "power supply")


@handle_cli_error
async def build_user_pc(username: str) -> None:
    """Orchestrate end-to-end component selection and save the configuration.

    Args:
        username (str): The active username building the PC.
    """
    u_cpu = await select_cpu()
    if not u_cpu:
        return
    u_mb = await select_motherboard(u_cpu)
    if not u_mb:
        return
    u_mem, num_modules = await select_memory(u_mb)
    if not u_mem:
        return
    u_gpu = await select_gpu()
    if not u_gpu:
        return
    u_storage = await select_storage()
    if not u_storage:
        return
    u_psu = await select_psu(u_cpu, u_gpu)
    if not u_psu:
        return

    user_parts = {
        "CPU": u_cpu,
        "GPU": u_gpu,
        "Motherboard": u_mb,
        "Power supply": u_psu,
        "Memory Module": u_mem,
    }
    print("==============================")

    print("Selected components are:")
    user_parts_list = []
    for part_name, part_data in user_parts.items():
        user_parts_list.append(part_data[0])
        print(f"{part_name} : {part_data[0]}")
    print(f"Number of Modules : {num_modules}")
    print(f"Storage Device : {u_storage[0]}")
    print(f"Storage Capacity : {u_storage[1]}")

    print()
    total_price = (
        u_cpu[-1]
        + u_gpu[-1]
        + u_mb[-1]
        + (u_mem[-1] * num_modules)
        + u_psu[-1]
        + u_storage[-1]
    )
    print(f"Price of all components: approximately is {total_price} inr")
    print("==============================")

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

    await insert_user_pc_build(
        username=username,
        cpu=user_parts_list[0],
        gpu=user_parts_list[1],
        motherboard=user_parts_list[2],
        memory=user_parts_list[4],
        num_modules=num_modules,
        storage=u_storage[1],
        psu=user_parts_list[3],
        total_price=total_price,
        date=date,
    )


@handle_cli_error
async def view_other_pcs() -> None:
    """Display saved PC builds from other community users."""
    headers, data = await fetch_all_users_pcs()
    print("==============================")
    print("Other users PC Builts are:")
    table = tabulate(data, headers=headers, tablefmt="psql")
    print(table)
    print("==============================")


async def pc_menu(username: str) -> None:
    """Display the PC builder menu for logged-in or guest users.

    Args:
        username (str): Active username.
    """
    while True:
        print("==============================")
        print("Press 1 - Create PC")
        print("Press 2 - See Otehrs PC Build")
        print("Press 3 - To Exit")
        print("==============================")
        choice = prompt_int("Enter your choice: ", valid_range=(1, 3))
        if choice == 1:
            await build_user_pc(username)
        elif choice == 2:
            await view_other_pcs()
        elif choice == 3:
            print("==============================")
            print("Thanks to visit.")
            print("==============================")
            time.sleep(10)
            exit(0)
