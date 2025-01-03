from db_init import t_person02, engine

with engine.connect() as conn:
    # update_query = t_person02.update().values(address = 'aaa')
    update_query = t_person02.update().values(address = 'bbb').where(t_person02.c.id == 1)

    conn.execute(update_query)
    conn.commit()