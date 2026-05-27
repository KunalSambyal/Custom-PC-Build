# Custom PC Build System

A terminal-based Python and MySQL project that helps users build compatible custom PCs by selecting components such as CPU, GPU, Motherboard, RAM, Storage, and PSU.

The project allows users to:

- Create custom PC builds
- View compatible hardware
- Store user builds in a database
- Manage records using admin access
- Calculate approximate total build cost

> Note: Component prices and hardware data are based on 2024 market data.

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
- Tabulate

---

# Project Structure

```text
Custom-PC-Build-System/
│
├── main.py
├── components.sql
├── README.md
├── Output(s).pdf
```

---

# How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
```

---

## Step 2: Install Required Python Libraries

```bash
pip install mysql-connector-python
pip install tabulate
```

---

## Step 3: Setup the Database

Import the provided SQL database file:

```bash
mysql -u root -p < components.sql
```

OR

1. Open MySQL Workbench
2. Open `components.sql`
3. Run the SQL script

This will automatically:

- Create the `components` database
- Create all required tables
- Insert sample hardware data

---

## Step 4: Configure MySQL Connection

Open `main.py` and update your MySQL credentials:

```python
con = sql.connect(
    host="localhost",
    username="root",
    passwd="YOUR_PASSWORD",
    database="components"
)
```

Replace `YOUR_PASSWORD` with your MySQL password.

---

## Step 5: Run the Program

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

