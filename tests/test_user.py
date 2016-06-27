import unittest
from unittest import TestCase
from dbfoo.dbfoo import DbFoo
from dbfoo.models import User, DataBase, Base
from sqlalchemy import func

class TestUser(TestCase):
    def setUp(self):
        self.dbname = 'dbfootest'
        self.db = DataBase(dbname=self.dbname)
        self.users = User()
        self.session = self.db.Session()

    def test_add_user(self):
        count = self.session.query(User).count()
        u = User()
        u.randomize()
        self.db.store(u)
        new_count = self.session.query(User).count()
        self.assertEqual(count+1, new_count)

    def test_add_user_from_init(self):
        count = self.session.query(User).count()
        u = User(first_name='foo', last_name='bar',
                 email='foobar@foobar.net', address='1123 1st st',
                 city='Portland', state='OR', phone='(555) 112-2013')
        self.db.store(u)
        new_count = self.session.query(User).count()
        self.assertEqual(count+1, new_count)

if __name__ == "__main__":
    unittest.main()
