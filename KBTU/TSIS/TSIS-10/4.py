import psycopg2
from config import config

def update_table():
    sql=(
        '''
        UPDATE dogs
        SET index = '001'
        WHERE name= 'Jack' ;
        '''
    )
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    update_table()