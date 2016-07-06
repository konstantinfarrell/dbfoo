import unittest
from unittest import TestCase
from dbfoo.models import User, DataBase


class TestUser(TestCase):
    def setUp(self):
        """
        Sets up all testing variables that will be used.
        """
        self.dbname = 'dbfootest'
        self.db = DataBase(dbname=self.dbname)
        self.users = User()
        self.session = self.db.Session()

    def test_add_user(self):
        """
        Adds a user and generates data using the "randomize"
        function.
        """
        count = self.session.query(User).count()
        u = User()
        u.randomize()
        self.db.store(u)
        new_count = self.session.query(User).count()
        self.assertEqual(count+1, new_count)

    def test_add_user_from_init(self):
        """
        Adds a user by passing arguments into the User
        class instance.
        """
        count = self.session.query(User).count()
        u = User(first_name='foo', last_name='bar',
                 email='foobar@foobar.net', address='1123 1st st',
                 city='Portland', state='OR', phone='(555) 112-2013')
        self.db.store(u)
        new_count = self.session.query(User).count()
        self.assertEqual(count+1, new_count)

    def test_random_state(self):
        """
        Tests that random states are chosen correctly and that
        two random states are not the same.
        """
        with open('dbfoo/data/states.txt', 'r') as states:
            states = states.read().splitlines()
            u = User()
            state = u.random_state()
            new_state = u.random_state()
            self.assertIn(state, states)
            self.assertIn(new_state, states)
            self.assertFalse(new_state == state)


if __name__ == "__main__":
    unittest.main()
