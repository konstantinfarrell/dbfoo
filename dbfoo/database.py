from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import MetaData, create_engine
from sqlalchemy.exc import ProgrammingError, OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DataBase(object):
    """ Performs general database operations. """
    
    def __init__(self,
                 dbtype="postgresql",
                 dbhost="localhost",
                 dbuser="postgres",
                 dbpass="postgres",
                 dbname="postgres"):

        self.dbname = dbname
        self.dbtype = dbtype
        self.dbhost = dbhost
        self.dbuser = dbuser
        self.dbpass = dbpass

        self.engine = create_engine(self.dbstring)
        try:
            self.engine.connect()
        except OperationalError:
            self.create_database(dbname)
            self.engine = create_engine(self.dbstring)
            self.engine.connect()

        self.metadata = MetaData(self.engine)
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)

        Base.metadata.create_all(self.engine)

    @property
    def dbstring(self):
        dbstring = "{dbtype}://{user}:{dbpass}@{host}/{name}".format(
                dbtype=self.dbtype,
                user=self.dbuser,
                dbpass=self.dbpass,
                host=self.dbhost,
                name=self.dbname)
        return dbstring

    def create_database(self, name):
        self.execute_root("create database {}".format(name))

    def drop_database(self, name):
        self.execute_root("drop database {}".format(name))

    def drop_table(self, tablename):
        self.execute("drop table \"{}\"".format(tablename))

    def clean_table(self, tablename):
        self.execute("delete from \"{}\"".format(tablename))

    def execute_root(self, query):
        """
        Connects to the 'postgres' database to perform operations.
        """
        name = self.dbname
        self.dbname = 'postgres'
        self.engine = create_engine(self.dbstring)
        self.engine.connect()
        self.execute(query)
        self.dbname = name

    def execute(self, query):
        """
        Executes a query on the database.
        """
        conn = self.engine.connect()
        conn.execute("commit")
        try:
            conn.execute(query)
        except ProgrammingError as e:
            print(e)
        except OperationalError as e:
            print(e)
        conn.close()

    def store(self, data):
        session = self.Session()
        if isinstance(data, list) is True:
            session.add_all(data)
        else:
            session.add(data)
        session.commit()
        session.close()
