# 结合requests模块

import asyncio
import requests

async def download_img(url):
    print("start download: ", url)
    
    loop = asyncio.get_event_loop()
    # requests模块默认不支持异步操作，所以使用线程池配合实现
    fut = loop.run_in_executor(None, requests.get, url)
    
    response = await fut
    print("下载完成")
    
    # 图片保存到本地
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)
        
# 效果和协程一样，耗费资源更多
