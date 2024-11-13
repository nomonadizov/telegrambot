import sqlite3

connection = sqlite3.connect('storage.db')
cursor = connection.cursor()

create_db_user_info = """
    CREATE TABLE IF NOT EXISTS userinfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        fullname TEXT,
        birth DATE,
        education TEXT,
        address TEXT,
        phone_number TEXT,
        additional_phone_number TEXT,
        marital_status TEXT,
        previous_job TEXT,
        expected_salary TEXT,
        expected_length TEXT,
        language_1 TEXT,
        language_1_level TEXT,
        language_2 TEXT,
        language_2_level TEXT,
        it_knowledge TEXT,
        source TEXT
    );
"""
cursor.execute(create_db_user_info)
connection.commit()
insert_query = """
    INSERT INTO userinfo (username, fullname, birth, education, address, phone_number, additional_phone_number, marital_status, previous_job, expected_salary, expected_length, language_1, language_1_level, language_2, language_2_level, it_knowledge, source)
    VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

def insert_data_to(modified_data):
    with sqlite3.connect('storage.db') as connection:
        cursor = connection.cursor()
        cursor.executemany(insert_query, [modified_data])
        connection.commit()
