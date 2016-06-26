import unittest
from main import DbFoo
from models import User, DataBase
from sqlalchemy import func

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = DbFoo(dbname='dbfoo')
        self.users = User()
        self.session = self.db.Session()
        super().setUp()

    def test_add_user(self):
        count = self.session.query(func.count(self.users.first_name)).scalar()
        u = User()
        u.randomize()
        self.db.store(u)
        new_count = self.session.query(func.count(self.users.first_name)).scalar()
        self.assertEqual(count+1, new_count)

    def test_add_user_from_init(self):
        count = func.count(self.users)
        u = User(first_name='foo', last_name='bar',
                 email='foobar@foobar.net', address='1123 1st st',
                 city='Portland', state='OR', phone='(555) 112-2013')
        self.db.store(u)
        self.assertEqual(count+1, func.count(self.users))

if __name__ == "__main__":
    unittest.main()
