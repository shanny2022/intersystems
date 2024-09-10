# tests/test_database_update.py
import unittest
from sqlalchemy import create_engine, MetaData, inspect
from database_update import new_table  # Ensure this import is correct

class TestDatabaseUpdate(unittest.TestCase):
    def setUp(self):
        # Set up a temporary database for testing
        self.engine = create_engine('sqlite:///:memory:')
        self.metadata = MetaData()

    def test_new_table_creation(self):
        # Create the table in the temporary database
        new_table.create(self.engine)

        # Check if the table exists
        inspector = inspect(self.engine)
        self.assertIn('new_table', inspector.get_table_names())

    def tearDown(self):
        # Drop all tables and close the connection
        self.metadata.drop_all(self.engine)
        self.engine.dispose()

if __name__ == '__main__':
    unittest.main()
