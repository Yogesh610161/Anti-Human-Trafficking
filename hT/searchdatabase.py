import psycopg2
def search_data(a):
    conn=psycopg2.connect("dbname='DR1' user='postgres' password='yogesh80' host='localhost' port='5432'")
    obj=db.query.filter_by(X='a').first()
    print(obj.Y)
    conn.close()

search_data(101)
