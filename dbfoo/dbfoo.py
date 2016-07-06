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
