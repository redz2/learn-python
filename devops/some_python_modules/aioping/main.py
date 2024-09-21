import asyncio
import aioping
import uvloop


async def do_ping(host):
    try:
        # aioping.verbose_ping(dest_addr="1.1.1.1", timeout=3, count=3, family=aioping.ICMP_ECHO_REPLY)
        delay = await aioping.ping(host) * 1000
        print("Ping response in %s ms" % delay)

    except TimeoutError:
        print("Timed out")
        
async def do_ping_hosts(hosts):
    tasks = []
    for host in hosts:
        tasks.append(asyncio.create_task(do_ping(host)))
    results, _ = await asyncio.wait(tasks)
    print(results)
        

# asyncio.run(do_ping("google.com"))
hosts = ("www.baidu.com" for i in range(100))


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.run(do_ping_hosts(hosts))


