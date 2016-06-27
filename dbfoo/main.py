from dbfoo.models import DataBase
from dbfoo.models import User


class DbFoo(DataBase):
    """
    Populates the database with mock data.
    """
    def generate_users_table(self, num):
        for i in range(num):
            u = User()
            u.randomize()
            self.store(u)

if __name__ == "__main__":
    dbstring = "postgres://postgres@/dbfoo"
    db = DbFoo(dbname='dbfoo')
    db.generate_users_table(1)
