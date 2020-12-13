# 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
# 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
# 将 ORM、插入、查询语句作为作业内容提交
from datetime import datetime,date
from sqlalchemy import Column, Integer, String, DateTime, DateTime, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class user_table(Base):
    __tablename__ = "userorm"
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    age = Column(Integer())
    birthday = Column(Date())
    sex = Column(String(2))
    degree = Column(String(20))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime, onupdate=datetime.now)

def __repr__(self):
    return f'user_table(id={self.id}, name={self.name})'

dburl ="mysql+pymysql://testuser:testpass@localhost:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

sessionclass = sessionmaker(bind=engine)
session = sessionclass()

user1 = user_table(name='zhangsan', age=45, birthday=date(1975, 8, 28), sex='f', degree='undergraduate')
user2 = user_table(name='lisi', age=33, birthday=date(1987, 4, 16), sex='f', degree='undergraduate')
user3 = user_table(name='wangwu', age=20, birthday=date(2000, 7, 19), sex='m', degree='undergraduate')
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()

query =session.query(user_table)
for i in query:
    print(i)
session.commit()
