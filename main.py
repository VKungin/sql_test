import sqlite3


def create_tables(cursor):
    cursor.execute(
        """
        CREATE TABLE customer (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department_id INTEGER,
            salary REAL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE department (
            department_id INTEGER,
            bonus_rate REAL
);
    """
    )


def insert_data(cursor):
    cursor.executemany(
        "INSERT INTO department (department_id, bonus_rate) VALUES (?, ?)",
        [(1, 0.15), (2, 0.1), (3, 0)],
    )

    cursor.executemany(
        "INSERT INTO customer (id, name, salary, department_id) VALUES (?, ?, ?, ?)",
        [
            (1, "Иван", 1000, 1),
            (2, "Пётр", 800, 1),
            (3, "Алла", 1350, 3),
            (4, "Николай", 1000, 2),
            (5, "Светлана", 1100, 2),
            (6, "Константин", 900, 1),
        ],
    )


def calculate_bonuses(cursor):
    cursor.execute(
        """
        SELECT c.name AS name, (c.salary * d.bonus_rate) AS total_bonus
        FROM customer c
        JOIN department d ON c.department_id = d.department_id
        ORDER BY total_bonus DESC
    """
    )

    results = cursor.fetchall()

    for row in results:
        print("Name:", row[0])
        print("Total Bonus:", row[1])
        print()


def main():
    conn = sqlite3.connect("customer_department")
    curs = conn.cursor()

    create_tables(curs)
    insert_data(curs)
    conn.commit()

    calculate_bonuses(curs)
    conn.close()


if __name__ == "__main__":
    main()
