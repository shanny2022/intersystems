# database_update.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Connect to the database
engine = create_engine('sqlite:///example.db')
metadata = MetaData()

# Define a new table
new_table = Table('new_table', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String))

def update_schema():
    """
    Update the database schema by creating the new_table.

    This function connects to the database and creates a new table
    called 'new_table' with columns 'id' and 'name'.
    """
    # Create the table in the database
    metadata.create_all(engine)
    print("Database schema updated successfully.")

if __name__ == "__main__":
    update_schema()
