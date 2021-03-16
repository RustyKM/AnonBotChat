import psycopg2

welcome_massage = "Привет.\nПрежде чем начать общение, выбери свой пол."

def create_db():
    pass

print(psycopg2.__doc__)

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432")

cursor = conn.cursor()
print(cursor)