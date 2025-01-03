from db_init import t_person02, engine

with engine.connect() as conn:
    delete_query = t_person02.delete().where(t_person02.c.id == 1)

    conn.execute(delete_query)
    conn.commit()



