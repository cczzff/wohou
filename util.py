# coding=utf8
"""
工具库
"""


def slices(src, size):
    """
    将src里的元素分批slice 出来
    example：
    for ids in slices(range(10000), 100):
        # ids is a list
        print len(ids)


    :param src:
    :param size:
    :return:
    """

    size = int(size)
    if size < 1:
        raise ValueError('size < 1')

    if not isinstance(src, (list, tuple)):
        raise TypeError('should be list or tuple')

    def _iter(src, size):
        offset = 0
        while True:
            piece = src[offset:offset + size]
            if not piece:
                break

            yield piece
            offset += size

    return _iter(src, size)




















