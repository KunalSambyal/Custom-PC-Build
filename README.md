# Custom PC Build System

A terminal-based Python and MySQL project that helps users build compatible custom PCs by selecting components such as CPU, GPU, Motherboard, RAM, Storage, and PSU.

The project allows users to:

- Create custom PC builds
- View compatible hardware
- Store user builds in a database
- Manage records using admin access
- Calculate approximate total build cost

> Note: Component prices and hardware data are based on 2023 market data.

---

# Features

## User Features

- User Login & Signup System
- Continue as Guest
- Create Custom PC Builds
- Compatibility-based component selection
- Automatic PSU recommendation
- Total Price Calculation
- View Other Users' PC Builds

## Admin Features

- Insert Records
- Update Records
- Display Records
- Search Records
- Delete Records

---

# Technologies Used

- Python
- MySQL
- mysql-connector-python
- python-dotenv
- Tabulate

---

# Project Structure

```text
Custom-PC-Build-System/
│
├── .env.example
├── .gitignore
├── Components.sql
├── Output(s).pdf
├── README.md
├── main.py
└── requirements.txt
```

---

# How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
cd Custom-PC-Build
```

---

## Step 2: Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (Command Prompt / PowerShell):
.venv\Scripts\activate

# macOS / Linux:
source .venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Create a `.env` file by copying `.env.example`:

```bash
cp .env.example .env
```

Open `.env` and set your MySQL credentials and admin password:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_database_password
DB_NAME=components
ADMIN_PASSWORD=your_admin_password
```

---

## Step 5: Setup the Database

Import the provided SQL database file:

```bash
mysql -u root -p < Components.sql
```

OR

1. Open MySQL Workbench
2. Open `Components.sql`
3. Run the SQL script

This will automatically:

- Create the `components` database
- Create all required tables
- Insert sample hardware data

---

## Step 6: Run the Program

```bash
python main.py
```

---

# Project Modules

The project includes:

- User Authentication System
- Database CRUD Operations
- Hardware Compatibility Logic
- Dynamic Component Selection
- Admin Management System

---

# Screenshots & Output

Project execution screenshots and outputs are included in:

```text
Output(s).pdf
```

---

# Future Improvements

- GUI version using Tkinter or PyQt
- Secure password hashing
- SQL injection prevention using parameterized queries
- Better exception handling
- Online deployment
- Expanded hardware database

---

# Author

Kunal Sambyal
links: X - @Kunal_Sambyal
