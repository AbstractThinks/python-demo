1. 依赖包安装`pip install -r requirements.txt`

2. No module named MYSQLdb 问题解决
> pip install mysql-python (mix os)
> apt-get install python-mysqldb (Linux Ubuntu)
> pip install mysqlclient (Windows)

3. 创建数据库 python db_create.py

4. 数据库迁移
> python db_migrate.py db init  (创建一个迁移库)
> python db_migrate.py db migrate -m "initial migration" (创建迁移脚本)
> python db_migrate.py db upgrade (更新数据库)
