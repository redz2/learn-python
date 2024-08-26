import asyncio
import aiomysql

async def main():
    # 连接MySQL
    conn = await aiomysql.connect(
        host="127.0.0.1", port=3306, user="root", password="12345", db="mysql"
    )
    # 创建CURSOR
    cur = await conn.cursor()
    # 执行SQL
    await cur.execute("SELECT Host,User FROM user")
    # 获取SQL结果
    result = await cur.fetchall()
    print(result)
    # 关闭CURSOR
    await cur.close()
    # 关闭连接
    conn.close()

asyncio.run(main())