"""Data Access Object (DAO) module providing asynchronous database operations."""

from typing import Any, Dict, List, Optional, Tuple
from sqlalchemy import text
from .database import get_db_session


# =====================================================================
# Schema & Metadata Queries
# =====================================================================
async def fetch_table_columns(tablename: str) -> List[str]:
    """Fetch uppercase column names for table display.

    Args:
        tablename (str): Name of the database table.

    Returns:
        List[str]: List of uppercase column names.
    """
    async with get_db_session() as session:
        query = text(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name = :table_name AND table_schema = DATABASE() "
            "ORDER BY ordinal_position"
        )
        result = await session.execute(query, {"table_name": tablename})
        return [row[0].upper() for row in result.fetchall()]


# =====================================================================
# Component Queries (PC Builder)
# =====================================================================
async def fetch_filtered_cpus(
    cpu_brand: str,
    min_core: int,
    max_core: int,
    min_thread: int,
    max_thread: int,
) -> List[Any]:
    """Fetch CPUs matching brand, core, and thread range filters.

    Args:
        cpu_brand (str): CPU brand identifier (e.g. 'AMD', 'INT').
        min_core (int): Minimum number of CPU cores.
        max_core (int): Maximum number of CPU cores.
        min_thread (int): Minimum number of CPU threads.
        max_thread (int): Maximum number of CPU threads.

    Returns:
        List[Any]: Matching CPU rows from the database.
    """
    async with get_db_session() as session:
        query = text(
            "SELECT * FROM cpus WHERE Model LIKE :brand "
            "AND core BETWEEN :min_c AND :max_c "
            "AND thread BETWEEN :min_t AND :max_t"
        )
        result = await session.execute(
            query,
            {
                "brand": f"%{cpu_brand}%",
                "min_c": min_core,
                "max_c": max_core,
                "min_t": min_thread,
                "max_t": max_thread,
            },
        )
        return result.fetchall()


async def fetch_filtered_gpus(gpu_brand: str, req_vram: str) -> List[Any]:
    """Fetch GPUs matching brand prefix and VRAM capacity.

    Args:
        gpu_brand (str): GPU brand prefix ('Radeon' or 'GeForce').
        req_vram (str): Required VRAM string (e.g. '8Gb').

    Returns:
        List[Any]: Matching GPU rows from the database.
    """
    async with get_db_session() as session:
        query = text("SELECT * FROM gpus WHERE prefix = :brand AND memory LIKE :vram")
        result = await session.execute(
            query, {"brand": gpu_brand, "vram": f"%{req_vram}%"}
        )
        return result.fetchall()


async def fetch_motherboards_by_socket(socket: str) -> List[Any]:
    """Fetch motherboards compatible with the specified CPU socket.

    Args:
        socket (str): The CPU socket type (e.g. 'AM4', 'Socket 1700').

    Returns:
        List[Any]: Matching Motherboard rows.
    """
    async with get_db_session() as session:
        query = text("SELECT * FROM motherboard WHERE socket = :socket")
        result = await session.execute(query, {"socket": socket})
        return result.fetchall()


async def fetch_memory_by_type_and_capacity(mem_type: str, capacity: str) -> List[Any]:
    """Fetch RAM memory modules matching DDR type and module capacity.

    Args:
        mem_type (str): Memory generation/type (e.g. 'DDR4', 'DDR5').
        capacity (str): Per-slot memory capacity (e.g. '16Gb').

    Returns:
        List[Any]: Matching Memory module rows.
    """
    async with get_db_session() as session:
        query = text(
            "SELECT * FROM memory WHERE type LIKE :mem_type AND capacity = :capacity"
        )
        result = await session.execute(
            query, {"mem_type": f"%{mem_type}%", "capacity": capacity}
        )
        return result.fetchall()


async def fetch_storage_by_type_and_capacity(
    storage_type: str, capacity: str
) -> List[Any]:
    """Fetch storage devices matching device type and capacity.

    Args:
        storage_type (str): Type of storage ('HDD', 'Sata SSD', 'NVMe M.2').
        capacity (str): Storage capacity string (e.g. '500GB', '1000GB').

    Returns:
        List[Any]: Matching Storage rows.
    """
    async with get_db_session() as session:
        query = text(
            "SELECT * FROM storages WHERE type = :storage_type AND capacity = :capacity"
        )
        result = await session.execute(
            query, {"storage_type": storage_type, "capacity": capacity}
        )
        return result.fetchall()


async def fetch_psu_by_wattage(min_wattage: int, max_wattage: int) -> List[Any]:
    """Fetch power supply units (PSUs) within the calculated wattage range.

    Args:
        min_wattage (int): Minimum required total system wattage.
        max_wattage (int): Maximum safe wattage overhead.

    Returns:
        List[Any]: Matching PSU rows.
    """
    async with get_db_session() as session:
        query = text(
            "SELECT * FROM psu "
            "WHERE CAST(REPLACE(UPPER(Wattage), 'W', '') AS UNSIGNED) BETWEEN :min_w AND :max_w"
        )
        result = await session.execute(
            query, {"min_w": min_wattage, "max_w": max_wattage}
        )
        return result.fetchall()


# =====================================================================
# User PC Build Operations
# =====================================================================
async def insert_user_pc_build(
    username: str,
    cpu: str,
    gpu: str,
    motherboard: str,
    memory: str,
    num_modules: int,
    storage: str,
    psu: str,
    total_price: float,
    date: str,
) -> None:
    """Insert a completed custom PC configuration into the database.

    Args:
        username (str): Username of the builder.
        cpu (str): Selected CPU model name.
        gpu (str): Selected GPU model name.
        motherboard (str): Selected Motherboard model name.
        memory (str): Selected Memory model name.
        num_modules (int): Number of RAM modules.
        storage (str): Selected Storage capacity/model.
        psu (str): Selected PSU model name.
        total_price (float): Total price of all parts combined.
        date (str): Build timestamp (YYYY-MM-DD).
    """
    async with get_db_session() as session:
        query = text(
            "INSERT INTO users_pc "
            "(username, CPU, GPU, MotherBoard, MemModule, NumberOfModule, StorageCapcity, PSU, TotalPrice, date) "
            "VALUES (:username, :cpu, :gpu, :mb, :mem, :num_mod, :storage, :psu, :price, :date)"
        )
        await session.execute(
            query,
            {
                "username": username,
                "cpu": cpu,
                "gpu": gpu,
                "mb": motherboard,
                "mem": memory,
                "num_mod": num_modules,
                "storage": storage,
                "psu": psu,
                "price": total_price,
                "date": date,
            },
        )
        await session.commit()


async def fetch_all_users_pcs() -> Tuple[List[str], List[Any]]:
    """Fetch all saved custom PC configurations along with matching column headers.

    Returns:
        Tuple[List[str], List[Any]]: (list of uppercase headers, list of row tuples).
    """
    async with get_db_session() as session:
        query = text(
            "SELECT CPU, GPU, MotherBoard, MemModule, NumberOfModule, StorageCapcity, PSU, TotalPrice "
            "FROM users_pc"
        )
        result = await session.execute(query)
        headers = [col.upper() for col in result.keys()]
        rows = result.fetchall()
        return headers, rows


# =====================================================================
# Authentication Queries
# =====================================================================
async def fetch_all_usernames() -> Dict[str, str]:
    """Fetch all usernames and their corresponding passwords from the database.

    Returns:
        Dict[str, str]: Mapping of username to password.
    """
    async with get_db_session() as session:
        query = text("SELECT username, password FROM users")
        result = await session.execute(query)
        return {row[0]: row[1] for row in result.fetchall()}


async def insert_user_record_db(
    name: str,
    username: str,
    password: Optional[str] = None,
    email: Optional[str] = None,
    date: str = "",
    time: str = "",
) -> None:
    """Insert a new user record into the database.

    Args:
        name (str): Full name of the user.
        username (str): Unique username.
        password (Optional[str]): Account password.
        email (Optional[str]): User email address.
        date (str): Registration date (YYYY-MM-DD).
        time (str): Registration time (HH:MM AM/PM).
    """
    async with get_db_session() as session:
        query = text(
            "INSERT INTO Users (Name, Username, Password, Email, SignedUpOn, SignedUpAt) "
            "VALUES (:name, :username, :password, :email, :signed_up_on, :signed_up_at)"
        )
        await session.execute(
            query,
            {
                "name": name,
                "username": username,
                "password": password,
                "email": email,
                "signed_up_on": date,
                "signed_up_at": time,
            },
        )
        await session.commit()


# =====================================================================
# Admin CRUD Queries
# =====================================================================
async def admin_insert_record(tablename: str, values: List[Any]) -> None:
    """Insert a record into the specified component table.

    Args:
        tablename (str): Name of the component table.
        values (List[Any]): List of ordered values matching the table columns.
    """
    async with get_db_session() as session:
        placeholders = ", ".join(f":val_{i}" for i in range(len(values)))
        params = {f"val_{i}": val for i, val in enumerate(values)}
        query = text(f"INSERT INTO {tablename} VALUES ({placeholders})")
        await session.execute(query, params)
        await session.commit()


async def admin_fetch_by_model(tablename: str, model: str) -> List[Any]:
    """Fetch a single component record by its Model code.

    Args:
        tablename (str): Name of the component table.
        model (str): Unique model number/code.

    Returns:
        List[Any]: Matching database rows (typically 0 or 1 row).
    """
    async with get_db_session() as session:
        query = text(f"SELECT * FROM {tablename} WHERE model = :model")
        result = await session.execute(query, {"model": model})
        return result.fetchall()


async def admin_update_record(
    tablename: str, columns: List[str], values: List[Any], model: str
) -> None:
    """Update an existing component record in the database.

    Args:
        tablename (str): Name of the component table.
        columns (List[str]): List of column names to update.
        values (List[Any]): New values corresponding to each column.
        model (str): Model number of the record to update.
    """
    async with get_db_session() as session:
        set_clauses = [f"{col} = :val_{i}" for i, col in enumerate(columns)]
        params = {f"val_{i}": val for i, val in enumerate(values)}
        params["model"] = model
        query = text(
            f"UPDATE {tablename} SET {', '.join(set_clauses)} WHERE Model = :model"
        )
        await session.execute(query, params)
        await session.commit()


async def admin_display_records(tablename: str, limit: int = 0) -> List[Any]:
    """Fetch records from the specified table, with an optional limit.

    Args:
        tablename (str): Name of the component table.
        limit (int): Maximum number of records to return (0 for all records).

    Returns:
        List[Any]: List of table rows.
    """
    async with get_db_session() as session:
        if limit > 0:
            query = text(f"SELECT * FROM {tablename} LIMIT :limit")
            result = await session.execute(query, {"limit": limit})
        else:
            query = text(f"SELECT * FROM {tablename}")
            result = await session.execute(query)
        return result.fetchall()


async def admin_search_records(
    tablename: str, colname: str, value: Any, is_exact: bool = False
) -> List[Any]:
    """Search for records in a table matching column criteria.

    Args:
        tablename (str): Name of the component table.
        colname (str): Target column name to search on.
        value (Any): Search term or value.
        is_exact (bool): If True, performs exact equality; otherwise uses LIKE.

    Returns:
        List[Any]: Matching database rows.
    """
    async with get_db_session() as session:
        if is_exact:
            query = text(f"SELECT * FROM {tablename} WHERE {colname} = :val")
            result = await session.execute(query, {"val": value})
        else:
            query = text(f"SELECT * FROM {tablename} WHERE {colname} LIKE :val")
            result = await session.execute(query, {"val": f"%{value}%"})
        return result.fetchall()


async def admin_delete_record(tablename: str, model: str) -> None:
    """Delete a component record from the table by its Model code.

    Args:
        tablename (str): Name of the component table.
        model (str): Model number of the record to delete.
    """
    async with get_db_session() as session:
        query = text(f"DELETE FROM {tablename} WHERE model = :model")
        await session.execute(query, {"model": model})
        await session.commit()
