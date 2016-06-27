from dbfoo.dbfoo import DbFoo


if __name__ == "__main__":
    dbstring = "postgres://postgres@/dbfoo"
    db = DbFoo(dbname='dbfoo')
    db.generate_users_table(1)
