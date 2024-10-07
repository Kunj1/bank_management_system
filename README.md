# The Continental

This is a Python-based Bank Management System built using `Tkinter` for the GUI and `MySQL` as the database. It allows users to perform basic banking operations such as account creation, deposits, withdrawals, and balance inquiries. The project was designed to simulate banking operations with a focus on simplicity and ease of use.

## Features:
- User authentication with **generated captcha** and **email** verification.
- Create new accounts and manage user information.
- Perform banking transactions: deposit, withdraw, check balance.
- Admin functionality to monitor and manage users and transactions.
- Local database storage with MySQL.

## Technology Stack:
- **Frontend:** Python `Tkinter` for the GUI.
- **Backend:** Python scripts to handle logic and database interactions.
- **Database:** MySQL for data storage.
  
## Requirements:
1. **Operating system:** Windows 10/macOS or later.
2. **RAM:** At least 8GB.
3. **Internal Storage:** More than 500GB.
4. **Python:** Version 3.7.3 or above.
5. **Backend:** MySQL 8.0 or above.
6. **IDE:** PyCharm (recommended).

## Installation Instructions:
1. Clone the repository to your local machine.
2. Install the necessary Python dependencies by running the following commands in your terminal or command prompt:
   ```
   pip install Tkinter
   pip install mysql-connector-python
   pip install Pillow
   pip install yagmail
   ```
   
3. Set up the MySQL database:
   - Ensure you have MySQL installed with InnoDB and MySQLDump.
   - Execute the provided SQL database file using the following command:
     ```bash
     mysql -u root -p [database_name] < bnkfinaldb.sql
     ```
   If you encounter errors, refer to this [StackOverflow link](https://stackoverflow.com/questions/5920136/mysql-is-not-recognised-as-an-internal-or-external-command-operable-program-or-b) for troubleshooting.

4. **Update Database Credentials:**  
   Before running the program, open the Python script (`continental_user.py`), and update the MySQL username and password with your own credentials.

## How to Run:
1. Navigate to the `continental_user.py` file.
2. Run the application using the following command:
   ```bash
   python continental_user.py
   ```
3. Enjoy using the Bank Management System!

## Future Improvements:
- Convert the desktop app into a web application using Flask or Django.
- Host the app on a cloud platform.
- Add more advanced security and encryption features.

---
