# 以客户端的形式同HTTP服务交互
base_url = "http://httpbin.org/get"

from urllib import request, parse
def test_urllib(url):
    params = {
        "name1": "value1",
        "name2": "value2",
    }
    query_string = parse.urlencode(params)
    # Get请求
    u = request.urlopen(url + "?" + query_string)
    # Post请求
    # u = request.urlopen(url, query_string.encode("ascii"))
    return u.read()

if __name__ == "__main__":
    test_urllib(base_url)