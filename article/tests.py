# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import redis
from django.test import TestCase

# Create your tests here.

re = redis.StrictRedis(host="localhost", port=6379, db=0)


if __name__ == '__main__':
    re.sadd('gogo', 2)
    re.sadd('gogo', 233)
    print re.scard('gogo')
    print re.scard('gog2o')
    ARTICLE_LIKE = 'article_like:{article_id}'
    re.sadd(ARTICLE_LIKE.format(article_id=2), 5)

    if re.sismember('gogo', '2'):
        print ('???')
        re.srem('gogo', 2)

    print re.scard('gogo')