from db_init import engine,t_person

with engine.connect() as connection:
    query = t_person.select()
    result_set = connection.execute(query)

    # for row in result_set:
    #     print(f"row:{row}")
    #     print(f"id:{row[0]}")
    #     print(f"name:{row.name}")

    # result = result_set.fetchall()
    # print(result)

    row = result_set.fetchone()
    print(row)






