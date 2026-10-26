import psycopg2

try:

    # Устанавливаем соединение

    connection = psycopg2.connect(

        host="localhost",          # База в контейнере, но доступна через localhost

        port="5435",               # Порт из секции ports

        user="postgres",           # POSTGRES_USER

        password="student",        # POSTGRES_PASSWORD

        database="student_task"          # POSTGRES_DB

    )

    cursor = connection.cursor()

    cursor.execute("SELECT name, category from products order by name;")

    products = cursor.fetchall()

    for product in products:
        print(f"Product: {product[0]} | {product[1]}")

    cursor.close()


except Exception as error:

    print(f"Ошибка при подключении: {error}")
