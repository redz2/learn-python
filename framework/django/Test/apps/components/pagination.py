# 自定义分页类

# PageNumberPagination
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
class CustomPagination(PageNumberPagination):
    
    """
    page_query_param: 前端发送的页数关键字名，默认为"page"
    page_size_query_param: 默认为None，一般设置为page_size
    page_size: 查询每页的数量
    max_page_size: 默认值为None
    """
    page_size_query_param = "page_size"
    max_page_size = 3


# LimitOffsetPagination
class CustomLimitPagination(LimitOffsetPagination):
    """
    default_limit: 默认值与PAGE_SIZE设置一致
    limit_query_param: 默认值为limit，查询每页的数量，相当于page_size
    offset_query_param: 默认值为offset，查询位置的初始偏移量，相当于page
    max_limit: 默认值为None
    
    """
    pass

