from db_init import engine,t_department,t_employee
import sqlalchemy

with engine.connect() as conn:
    join = t_employee.join(t_department,t_employee.c.dept_id == t_department.c.dept_id)
    # query = sqlalchemy.select(join).where(t_department.c.name == 'HR')
    # query = sqlalchemy.select(t_employee).select_from(join).where(t_department.c.name == 'HR')
    query = sqlalchemy.select(t_department).select_from(join).where(t_employee.c.name == 'tom')

    print(conn.execute(query).fetchall())
