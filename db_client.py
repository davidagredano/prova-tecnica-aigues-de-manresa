import psycopg

credentials = {
    "host": "10.8.21.61",
    "dbname": "postgres",
    "port": 5432,
    "user": "mosquitto",
    "password": "2024.PERTE",
}


QUERY = "TODO"


with psycopg.connect(**credentials) as conn:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        )
        tables = cur.fetchall()

        cur.execute(
            "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'observations'"
        )

        cur.execute(QUERY)
        things = cur.fetchall()
        for record in things:
            print(record)
