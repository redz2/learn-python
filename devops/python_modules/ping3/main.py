import ping3
import time
import asyncio
import threading
import concurrent
import os

class TestPing3():
    
    def __init__(self):
        pass
    
    # 同步函数
    def ping(self, ip):
        # print(threading.current_thread().ident)
        
        # float | None | False: The delay in seconds/milliseconds, False on error and None on timeout.
        response_time = ping3.ping(ip, timeout=4)
        
        # if response_time:
        #     print(f"response time is {response_time}")
        # else:
        #     print(f"ping timeout")
        return ip, response_time
    
    # ping压力测试
    # TODO: 将压力测试改造成并发，或者直接用ping_in_many_thread
    def stress_ping_test(self, ip:str, total_requests:int):
        total_time = 0
        failed_requests = 0
        for _ in range(total_requests):
            start_time = time.perf_counter()
            response_time = ping3.ping(ip, timeout=3)
            end_time = time.perf_counter()
            
            if response_time:
                total_time += end_time - start_time
            else:
                failed_requests += 1
            
            successful_requests = total_requests - failed_requests
            successful_rate = (successful_requests  / total_requests) * 100
            try:
                average_response_time = (total_time / successful_requests) * 1000
            except ZeroDivisionError:
                average_response_time = "inf "
            
        print("test result --------------------")
        print(f"total requests: {total_requests}")
        print(f"successful requests: {successful_requests}")
        print(f"failed requests: {failed_requests}")
        print(f"successful rate: {successful_rate}%")
        print(f"average response time: {average_response_time}ms")
    
    # 异步代码太有魅力了 
    async def ping_in_many_thread(self, ips:[str], *, need_response_time=False):
        
        # 在主线程中执行
        # print(threading.current_thread().ident)
        
        # 获取当前event loop，如果没有抛出异常
        loop = asyncio.get_running_loop()
        
        if not need_response_time:
            
            # 使用线程并发执行，会增加响应时间，获取响应时间的值没啥意义
            worker_num = len(ips)
            
            # 在默认的循环执行器中执行
            # tasks = [loop.run_in_executor(pool, self.ping, ip) for ip in ips]
            
            # 在自定义线程池中执行
            with concurrent.futures.ThreadPoolExecutor(max_workers=worker_num) as pool:
                # loop.run_in_executor 把普通函数放到executor中执行，将普通函数包装成Future对象
                # 本质上是多线程并发
                tasks = [loop.run_in_executor(pool, self.ping, ip) for ip in ips]
                result, _ = await asyncio.wait(tasks)
                self.handle_thread_or_process_result(result)
        else:
            # 如果要精确的响应时间，使用多进程并行执行
            cpu_count = os.cpu_count()
            print(f"this machine have {cpu_count} cpus")
            worker_num = cpu_count
            
            # 在自定义的进程池中执行
            with concurrent.futures.ProcessPoolExecutor(max_workers=worker_num) as pool:
                tasks = [loop.run_in_executor(pool, self.ping, ip) for ip in ips]
                result, _ = await asyncio.wait(tasks)
                self.handle_thread_or_process_result(result, thread=False)
        
    def handle_thread_or_process_result(self, result, thread=True):
        print("")
        print("="*30)
        print("")
        for fut in result:
            r = fut.result()
            if r[1]:
                if thread:
                    print(f"ip: {r[0]}\nhost is up")
                else:
                    print(f"ip: {r[0]}\nhost is up; response time is: {round(r[1]*1000,2)} ms")
            elif r[1] is None:
                print(f"ip: {r[0]}\nhost is down")
            else:
                print(f"ip: {r[0]}\nhost maybe error")
            print("")
            
    
    def ping_hosts(self, ip, *, ips=None):
        """parse ips"""
        pass
    
if __name__ == "__main__":
    
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    t = TestPing3()
    # t.ping("www.baidu.com")
    # t.stress_ping_test("1.1.1.3", 10)
    # print(threading.current_thread().ident)
    
    ips = ["10.239.241." + str(i+1) for i in range(4)]
    start_time = time.perf_counter()
    asyncio.run(t.ping_in_many_thread(ips, need_response_time=True))
    end_time = time.perf_counter()
    print("spend time: ", end_time - start_time)
    