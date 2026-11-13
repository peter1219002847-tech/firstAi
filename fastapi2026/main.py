from models.base import Base
from models.database import engine
from models.models import Employee,Department

# 创建表
def create_table():
  print("注册的表名:", Base.metadata.tables.keys())
  # 创建所有模型对应的表
  Base.metadata.create_all(bind=engine)
  print("表创建成功")

if __name__ == '__main__':
  create_table()