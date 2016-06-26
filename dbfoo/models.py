from random import choice, randrange

from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import MetaData, create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DataBase(object):
    """
    Performs general database operations.
    """
    def __init__(self,
                 dbtype="postgres",
                 dbhost="",
                 dbuser="postgres",
                 dbpass="",
                 dbname="postgres"):

        self.dbname = dbname
        self.dbtype = dbtype
        self.dbhost = dbhost
        self.dbuser = dbuser
        self.dbpass = dbpass

        dbstring = "{dbtype}://{user}:{dbpass}@{host}/{name}".format(
                dbtype=self.dbtype,
                user=self.dbuser,
                dbpass=self.dbpass,
                host=self.dbhost,
                name=self.dbname)

        self.engine = create_engine(dbstring)

        self.metadata = MetaData(self.engine)
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)

        Base.metadata.create_all(self.engine)

    def create_database(self, name):
        self.execute("create database {}".format(name))

    def drop_table(self, tablename):
        self.execute("drop table \"{}\"".format(tablename))

    def clean_table(self, tablename):
        self.execute("delete from \"{}\"".format(tablename))

    def execute(self, query):
        """
        Executes a query on the database.
        """
        conn = self.engine.connect()
        conn.execute("commit")
        try:
            conn.execute(query)
        except ProgrammingError as e:
            pass
        conn.close()

    def store(self, data):
        session = self.Session()
        if isinstance(data, list) is True:
            session.add_all(data)
        else:
            session.add(data)
        session.commit()
        session.close()


class User(Base, DataBase):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    phone = Column(String)

    generics = ['st', 'ln', 'rd', 'ave', 'blvd', 'drive', 'way']
    specifics = open('data/streetnames.txt', 'r').read().splitlines()

    def __init__(self, first_name=None, last_name=None,
                 email=None, address=None, city=None, state=None, phone=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.phone = phone

    def random_address(self):
        """
        Generates a random street address
        """
        number = randrange(1, 9999)
        specific = choice(self.specifics)
        generic = choice(self.generics)

        return "{} {} {}".format(str(number), specific, generic)

    def pick_random(self, path):
        """
        Picks a random line from a specified file.
        """
        choices = open(path, 'r').read().splitlines()
        return choice(choices)

    def random_first_name(self):
        return self.pick_random('data/firstnames.txt')

    def random_last_name(self):
        return self.pick_random('data/lastnames.txt')

    def random_city(self):
        return self.pick_random('data/cities.txt')

    def random_state(self):
        return self.pick_random('data/states.txt')

    def random_phone(self):
        """
        Generates a random phone number.
        """
        phone = "{}{}{}".format(randrange(100, 999),
                                randrange(100, 999), randrange(1000, 9999))
        return phone

    def randomize(self):
        """
        Generates random info to put in
        the class fields.
        """
        self.first_name = self.random_first_name()
        self.last_name = self.random_last_name()
        username = "{}{}".format(self.first_name, self.last_name).lower()
        self.email = self.create_email(username)
        self.address = self.random_address()
        self.city = self.random_city()
        self.state = self.random_state()
        self.phone = self.random_phone()

    def create_email(self, username):
        """
        Generates a basic email address
        """
        suffix = self.pick_random('data/email_providers.txt')
        return "{}@{}".format(username, suffix)
