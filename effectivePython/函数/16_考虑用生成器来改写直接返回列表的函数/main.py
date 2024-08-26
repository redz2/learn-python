# 尽量返回生成器，不要返回列表
def index_words(text):
    """字符串中每个字的首字母位置"""
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == "":
            result.append(index + 1)
    return result


def index_words_iter(text):
    """字符串中每个字的首字母位置"""
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == "":
            yield index + 1