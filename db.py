import psycopg2
import settings


def create_conn():
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
    )
    conn.set_session(autocommit=True)
    return conn


def insert_search_query(user_id, query):
    conn = create_conn()
    cursor = conn.cursor()
    stmt = "INSERT INTO user_search VALUES(%s, %s)"
    cursor.execute(stmt, (str(user_id), str(query)))
    conn.close()


def get_search_history(user_id, query):
    conn = create_conn()
    cursor = conn.cursor()
    stmt = "SELECT query FROM user_search WHERE user_id = %s AND query LIKE %s"
    cursor.execute(stmt, (str(user_id), '%' + str(query) + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
