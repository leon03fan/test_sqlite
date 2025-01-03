from db_init import Session,Person02
import datetime

session = Session()

# p = Person02(name='阿文',birthday=datetime.date(1999, 2, 1),address='北京')
# session.add(p)
# session.commit()

list_person = [
    Person02(name='朱胜文',birthday=datetime.date(1989, 2, 1),address='上海'),
    Person02(name='吴宗霖',birthday=datetime.date(1969, 2, 1),address='台湾')
]
session.add_all(list_person)
session.commit()


