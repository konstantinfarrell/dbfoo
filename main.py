from models import DataBase
from models import User


class DbFoo(DataBase):
    """ """
    def populate_users_table(self, num):
        for i in range(num):
            u = User()
            u.randomize()
            self.store(u)


if __name__ == "__main__":
    dbstring = "postgres://postgres@/dbfoo"
    db = DbFoo(dbname='dbfoo')
    db.populate_users_table(1)
