import sqlite3

class DataStorage:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name,columns):
        column_str = ', '.join([f"{col} {ctype}" for col, ctype in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str})")
        self.conn.commit()

    def insert_data(self, table_name, data):
        column_names = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        self.cursor.execute(f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})", tuple(data.values()))
        self.conn.commit()

    def select_data(self, table_name, columns=None, conditions=None):
        column_str = ', '.join(columns) if columns else '*'
        condition_str = ' AND '.join([f"{col} = ?" for col in conditions]) if conditions else ''
        self.cursor.execute(f"SELECT {column_str} FROM {table_name} WHERE {condition_str}", tuple(conditions))
        return self.cursor.fetchall()

    def update_data(self, table_name, data, conditions):
        set_str = ', '.join([f"{col} = ?" for col in data])
        condition_str = ' AND '.join([f"{col} = ?" for col in conditions])
        self.cursor.execute(f"UPDATE {table_name} SET {set_str} WHERE {condition_str}", tuple(data.values()) + tuple(conditions.values()))
        self.conn.commit()

    def delete_data(self, table_name, conditions):
        condition_str = ' AND '.join([f"{col} = ?" for col in conditions])
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition_str}", tuple(conditions.values()))
        self.conn.commit()

    def close(self):
        self.conn.close()
