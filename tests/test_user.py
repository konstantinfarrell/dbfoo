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
            state = self.users.random_state()
            new_state = self.users.random_state()
            self.assertIn(state, states)
            self.assertIn(new_state, states)
            self.assertNotEqual(new_state, state)

    def test_random_phone(self):
        """
        Tests that a random phone number is the correct length
        and that two random phone numbers are unique.
        """
        phone = self.users.random_phone()
        other_phone = self.users.random_phone()
        self.assertEqual(len(phone), 10)
        self.assertNotEqual(phone, other_phone)

    def test_random_city(self):
        """
        Tests that a random city is chosen from the list
        of cities, and that two random cities are unique.
        """
        with open('dbfoo/data/cities.txt', 'r') as cities:
            cities = cities.read().splitlines()
            city = self.users.random_city()
            other_city = self.users.random_city()
            self.assertIn(city, cities)
            self.assertIn(other_city, cities)
            self.assertNotEqual(city, other_city)

    def test_create_email(self):
        """
        Generates a first and last name for a user, then
        tests to ensure the first and last name are contained
        within the generated email address.
        """
        self.users.first_name = self.users.random_first_name()
        self.users.last_name = self.users.random_last_name()
        username = "{}{}".format(self.users.first_name, self.users.last_name)
        email = self.users.create_email(username)
        self.assertIn("{}{}{}".format(self.users.first_name,
                                      self.users.last_name,
                                      '@'), email)


if __name__ == "__main__":
    unittest.main()
