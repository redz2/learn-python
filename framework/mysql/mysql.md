# 数据库
1. 数据库管理系统: Oracle、MySQL、SQLServer、PostgreSQL、Redis、ES、MongoDB

2. SQL
    * 做什么，而不是怎么做
    * 注释
        * 单行: --
        * 多行: /* */

3. 数据库操作（文件夹）
```sql
-- 创建数据库
create database [if not exist] db_name [character set xxx];

-- 查询数据库
show databases;
show databases like '%xxx%';
show create database db_name; -- 查看数据库的创建方式

-- 修改数据库
alter database db_name [character set xxx];

-- 删除数据库
drop database [if exists] db_name;

-- 使用数据库
use db_name; -- 切换数据库
select database();

-- 备份数据库
mysqldump -u username -p password database_name > backup.sql
```

4. 数据表操作（文件）
    * 数据库数据类型
        * 字符串: CHAR、VARCHAR、TINYTEXT、TEXT、ENUM
        * 整数类型: TINYINT、SMALLINT、MEDIUMINT、INT、BIGINT
        * bool类型: TINYINT(1)
        * 浮点数: FLOAT、DOUBLE、DECIMAL
        * 日期: DATE、DATETIME、TIME、TIMESTAMP、YEAR
    * 约束
        * 非空约束: NOT NULL
        * 唯一约束: UNIQUE
        * 默认值约束: DEFAULT
        * 主键约束: id INT PRIMARY KEY AUTO_INCREMENT(非空且唯一)
```sql
-- 创建数据表
CREATE TABLE my_table (
    field1 type 约束条件,
    field2 type,
    field3 type -- 最后不要加逗号，不然会报错
) [character set utf8];

-- 查看数据表
show tabls;
desc table_name; -- 查看表结构
show create table table_name; -- 查看建表语句

-- 删除数据表
drop table [if exists] table_name;

-- 修改数据表
alter table <old_name> RENAME [TO] <new_name>; -- 修改表名
alter table <table_name> [DEFAULT] CHARACTER SET <字符集名>; -- 修改表名

-- 表字段的增删改查
alter table <table_name> add name char; -- 增加一个字段
alter table <table_name> add age int after name; -- 再增加一个字段，放在name字段后面
alter table <table_name> drop age; -- 删除一个字段
alter table <table_name> modify name varchar; -- 修改字段类型
alter table <table_name> change name new_name varchar first; -- 修改字段类型(默认放在最后，first、after用于调整字段位置)
```

5. 表记录操作（数据）
* 添加记录
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2); -- 添加单条记录
INSERT INTO table_name (column1, column2) VALUES (value1, value2), -- 批量添加多条记录
                                                (value3, value4);
                                                (value5, value6);
INSERT table_name SET column1="value1",column2="value2"; -- 用的不多                                        
```
* 删除记录
```sql
delete from table; -- 清空表，危险操作
delete from table WHERE name = "yuan"; -- 删除一条记录
delete from table WHERE age > 35 ORDER BY desc age LIMIT 5; -- 删除多条记录
```
* 查询记录
```sql
-- SQL语句执行顺序: from where select group by having order by limit
select *|field1,field2 from table_name
                    WHERE 条件          -- and、in、like、regexp、regexp_like
                    GROUP BY field      -- 分组查询: 根据字段对结果集进行分组，使用聚合函数进行统计（max,min,avg,sum,count）
                                        -- 不分组也可以使用聚合函数，会将当前数据集作为一个大的组
                    HAVING 筛选条件       -- 对分组后的数据进行二次过滤
                    ORDER BY field1,field2  -- 按照某个字段排序 asc（升序）desc（降序）
                    LIMIT 限制条数;       -- 10,10 跳过前10条显示接下来的10条，最常用于分页

select 类别 '部门', avg(数量) '平均工资' from table
                    WHERE 条件              -- 分组之前，进行过滤
                    GROUP BY 类别           -- 分组
                    HAVING avg(数量) < 1000 -- 分组之后，进行过滤
                    ORDER BY sum(数量) desc;

select * from table WHERE birth > '2000-10-20'; -- 日期: year(birth) month(birth) day(birth)

-- 查询去重: distinct
select distinct age from table; -- 对于查询的结果集进行去重
```

* 修改记录
```sql
update table set salary = salary * 1.25 WHERE age > 35; -- 更新某些记录，一般使用id来更新一条记录
```