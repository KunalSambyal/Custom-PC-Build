# Custom PC Build System

A modular, asynchronous CLI-based Python application powered by **Async SQLAlchemy** and **MySQL** that helps users build compatible custom PCs by guiding them through component selection (CPU, GPU, Motherboard, RAM, Storage, and PSU).

---

## Key Highlights

- **Asynchronous Architecture:** Non-blocking async/await database operations powered by **SQLAlchemy 2.0** and **`asyncmy`**.
- **Hardware Compatibility Engine:** Dynamically validates CPU socket compatibility with motherboards, memory generations (DDR4/DDR5), and total system wattage for PSU selection.
- **DAO Pattern:** Data access logic is decoupled into a dedicated Data Access Object (`src/dao.py`) layer with parameterized queries to prevent SQL injection.
- **Admin Inventory Dashboard:** Complete CRUD operations (Insert, Update, Display, Search, Delete) for hardware inventory management.
- **Modular Design:** Clear separation of concerns conforming to PEP 8 standards with PEP 257 docstrings across all modules.

> **Note:** Component prices and hardware specifications are based on 2024 market data.

---

## Features

### User Features

- **User Authentication & Profiles:** Secure account creation, password complexity validation, and login.
- **Guest Access:** Jump directly into building a PC with automatically generated guest sessions.
- **Interactive PC Builder:**
    - Dynamic filtering by CPU cores, threads, and brand (AMD/Intel).
    - Dedicated GPU selection by VRAM capacity (AMD Radeon / NVIDIA GeForce).
    - Socket-matched Motherboard recommendation.
    - Compatible DDR RAM selection with customizable module counts.
    - Storage selection (HDD, SATA SSD, NVMe M.2).
    - Auto-calculated total system wattage with overhead for PSU selection.
- **Build Summary & Estimation:** Real-time approximate pricing breakdown and automated build persistence.
- **Community Builds Showcase:** View configurations built and saved by other users.

### Admin Features

- **Password-Protected Access:** Secure admin terminal access.
- **Inventory Management (CRUD):**
    - **Insert:** Add new components to any category table.
    - **Update:** Modify component specifications and pricing by model number.
    - **Display:** View table records with formatted ASCII tables (`tabulate`).
    - **Search:** Query inventory by column criteria (exact numeric or pattern matching).
    - **Delete:** Remove obsolete parts with confirmation prompts.

---

## Technologies Used

- **Language:** Python 3.10+ (`asyncio`)
- **Database:** MySQL
- **ORM & Driver:** SQLAlchemy 2.0 (Async Extension) & `asyncmy`
- **Configuration:** `python-dotenv`
- **Output Formatting:** `tabulate`

---

## Project Structure

```text
Custom-PC-Build/
├── .env.example              # Sample environment variables
├── .gitignore                # Git ignore patterns
├── Components.sql            # MySQL database dump and sample hardware data
├── Output(s).pdf             # Project execution screenshots and visual outputs
├── README.md                 # Project documentation
├── main.py                   # Async application entrypoint
├── requirements.txt          # Python package dependencies
└── src/                      # Modular application source code
    ├── __init__.py           # Package initializer
    ├── admin.py              # Admin dashboard and CRUD interface
    ├── auth.py               # User authentication, registration, and guest logic
    ├── builder.py            # Hardware compatibility and custom PC builder workflow
    ├── constants.py          # Centralized constants (tables, brands, storage types)
    ├── dao.py                # Data Access Object (Async SQLAlchemy queries)
    ├── database.py           # Async database engine and session factory
    └── utils.py              # Input validation, prompts, and CLI error handling
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/KunalSambyal/Custom-PC-Build.git
cd Custom-PC-Build
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell / Command Prompt):
.venv\Scripts\activate

# macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Open `.env` and fill in your MySQL database URL and admin password:

```env
# Database connection string (Async SQLAlchemy with asyncmy)
DB_URL=mysql+asyncmy://root:your_mysql_password@localhost:3306/components

# Admin Access Password
ADMIN_PASSWORD=your_admin_password
```

### 5. Import the Database Schema

Import `Components.sql` into MySQL to create the database and seed hardware data:

**Using MySQL CLI:**

```bash
mysql -u root -p < Components.sql
```

_Or open `Components.sql` inside **MySQL Workbench** / **phpMyAdmin** and execute the script._

### 6. Run the Application

```bash
python main.py
```

---

## Application Architecture

```mermaid
graph TD
    Main[main.py: main_menu] --> Auth[src/auth.py]
    Main --> Builder[src/builder.py]
    Main --> Admin[src/admin.py]

    Auth --> DAO[src/dao.py]
    Builder --> DAO
    Admin --> DAO

    Builder --> Utils[src/utils.py]
    Admin --> Utils
    Auth --> Utils

    DAO --> DB[src/database.py: AsyncSession]
    DB --> MySQL[(MySQL Database)]
```

---

## Screenshots & Output

Visual walkthroughs, sample runs, and menu execution outputs are available in:

- [`Output(s).pdf`](<file:///D:/code/Projects/Custom-PC-Build/Output(s).pdf>)

---

## Future Improvements

- Graphical User Interface (GUI) / Web dashboard using modern frontend frameworks.
- Industry-standard password hashing using bcrypt or Argon2.
- Integration with external e-commerce and hardware price tracking APIs for live pricing.
- Export custom PC build summaries and invoices as PDF / CSV.
- Automated test suites (pytest-asyncio) and CI/CD pipelines.

---

## Author

**_Kunal Sambyal_**
