import psycopg2
import pandas as pd

try:
    # Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5435",               # Порт из секции ports
        user="postgres",           # POSTGRES_USER
        password="student",        # POSTGRES_PASSWORD
        database="student_task"          # POSTGRES_DB
    )
    print("✓ Подключение установлено\n")

    query = """
        SELECT
        *
        FROM products as p
        JOIN prices as pr ON p.id = pr.prduct_id;
    """

    df = pd.read_sql(query, connection)
    mean_price = df["price"].mean()
    median_price = df["price"].median()
    std_price = df["price"].std()
    max_price = df["price"].max()
    min_price = df["price"].min()
    print("#1")
    print(f"СРЕДНЯЯ ЦЕНА СОСТАВЛЯЕТ {mean_price}₽\n")
    print("____________________________________________")
    print(f"МЕДИАННАЯ ЦЕНА СОСТАВЛЯЕТ {median_price}₽\n")
    print("____________________________________________")
    print(f"СТАНДАРТНОЕ ОТКЛОНЕНИЕ ЦЕНы СОСТАВЛЯЕТ {std_price}₽\n")
    print("____________________________________________")
    print(f"МАКСИМАЛЬНАЯ ЦЕНА СОСТАВЛЯЕТ {max_price}₽\n")
    print("____________________________________________")
    print(f"МИНИМАЛЬНАЯ ЦЕНА СОСТАВЛЯЕТ {min_price}₽\n")


    ##########2
    q1_price = df["price"].quantile(0.25)
    q3_price = df["price"].quantile(0.75)
    iqr = q3_price - q1_price
    print("#2")
    print(f"Q1: {q1_price}")
    print(f"Q3: {q3_price}")
    print(f"IQR: {iqr}")
    for i,row in df.iterrows():
        if row["price"] > q3_price:
                print(f'Имя товара: {row["name"]}')
                print(f'ID товара: {row["id"]}')
                print("_______________________________________")


    ##############3
    print("#3")
    tmp_df = df.groupby("category")
    categories = df["category"].unique()

    for i in categories:
        category = tmp_df.get_group(i)
        count = len(category)
        mean = category['price'].mean()
        median = category['price'].median()
        std = category['price'].std()
        print(f'Категория: {i}\n')
        print(f'Количество записей: {count}\n')
        print(f'Средняя цена: {mean}₽\n')
        print(f'Медианная цена: {median}₽\n')
        print(f'Стандартное отклонение цены: {std}₽\n')
        print("_______________________________________")


    #################4
    print("#4")
    grouped = df.groupby('prduct_id')
    ids = df['prduct_id'].unique()
    for i in ids:
        new_df = grouped.get_group(i)
        max = new_df['price'].max()
        min = new_df['price'].min()
        diff = max - min

        print(f'ID товара: {i}, max: {max}₽, min: {min}₽, diff: {diff}₽')







except Exception as error:
    print(f"Ошибка при подключении: {error}")
