# 张三给李四通过网银转账 100 极客币，现有数据库中三张表：
# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
# 请合理设计三张表的字段类型和表结构；
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

import pymysql
from dbconfig import read_db_conf
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, desc, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 读取数据库配置
dbserver = read_db_conf()
host = dbserver["host"]
database = dbserver["database"]
user = dbserver["user"]
password = dbserver["password"]

Base = declarative_base()

class user_table(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    name = Column(String(15), unique=True)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        result = '{"user_id":%s, "user_name":%s}' % (self.id, self.name)
        return result

class account_table(Base):
    __tablename__ = "account"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer())
    user_asset = Column(DECIMAL(10, 2))
    created_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        result = '{"user_id":%s, "user_asset":%s}' % (self.user_id, self.user_asset)

class accountflow_table(Base):
    __tablename__ = "account_flow"
    id = Column(Integer(), primary_key=True)
    from_id = Column(Integer())
    to_id = Column(Integer())
    deal_money = Column(DECIMAL(10,2))
    ceated_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        result = '{"from_id":%s, "to_id":%s, "deal_money":%s}' % (self.from_id, self.to_id, self.deal_money)
        return result

dburl = "mysql+pymysql://%s:%s:3306/%s?charset=utf8mb4" %(user, password, host, database)
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

sessionclass = sessionmaker(bind=engine)
session = sessionclass()
user_obj = [user(name="zhangsan"), user(name="lisi")]
session.add_all(user_obj)
account_obj = [account_table(user_id=1,user_asset=150), account_table(user_id=2, user_asset=200)]
session.add_all(account_obj)
session.commit()

with engine.begin() as conn:
    zhangsan_count = session.query(account_table).outjoin(user_table, account_table.user_id==user_table.id).filter(user_table.name == "zhangsan").first()
    lisi_count = session.query(account_table).outjoin(user_table, account_table.user_id==user_table.id).filter(user_table.name == "lisi").first()

    if float(zhangsan_count.user_asset) >= 100:
        sql = "UPDATE account SET user_asset=%s, update_time=%s WHERE user_id=%s"
        zs_value = (float(zhangsan_count.user_asset)-100, str(datetime.now()), int(zhangsan_count.user_id))
        conn.execute(sql, zs_value)

        ls_value = (float(lisi_count.user_asset)+100, str(datetime.now()), int(lisi_count.user_id))
        conn.execute(sql, ls_value)

        sql = "INSERT INTO account_flow(from_id, to_id, deal_money, created_time, update_time) VALUES(%s,%s,%s,%s,%s)"
        value = (int(zhangsan_count.user_id),int(lisi_count.user_id),100,str(datetime.now()),str(datetime.now()))
        conn.execute(sql, value)
    else:
        print("交易失败")
        conn.execute("UPDATE account SET user_asset=%s WHERE user_id=%s" %(float(zhangsan_count.user_asset)+200, int(zhangsan_count.user_id)))