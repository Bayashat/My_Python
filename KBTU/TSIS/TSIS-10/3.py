import psycopg2
from config import config


def insert_vendor_list(vendor_list):
    stmt = "INSERT INTO products (id, name , discription) VALUES (%s,%s, %s)"

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(stmt,vendor_list)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    insert_vendor_list([
       ('1', 'apple', 'qqqq'),
       ('2', 'banana', ' qwer')
    ])
