from db_init import engine,t_department,t_employee

with engine.connect() as conn:
    conn.execute(t_department.insert(),[
        {"name":'HR'},
        {"name":"IT"}
    ])

    conn.execute(t_employee.insert(),[
        {"dept_id":1,"name":"Jack"},
        {"dept_id":1,"name":"Mary"},
        {"dept_id":1,"name":"tom"},
        {"dept_id":2,"name":"Smith"},
        {"dept_id":2,"name":"Leon"},
        {"dept_id":2,"name":"Rose"}
    ])

    conn.commit()