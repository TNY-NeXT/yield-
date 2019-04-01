from urllib.request import urlopen
import gevent, time
from gevent import monkey

monkey.patch_all()

def f(url):
    print("GET: %s" % url)
    resp = urlopen(url)
    data = resp.read()
    with open('xiaohua.html', 'wb') as f:
        f.write(data)
    print("%d bytes received from %s." % (len(data), url))


begin = time.time()
# l = ['http://www.xiaohuar.com/', 'https://www.cnblogs.com/dwlsxj/p/RabbitMQ.html', 'https://www.cnblogs.com/yuanchenqi/articles/5692716.html']
# for url in l:
#     f(url)

gevent.joinall([
        gevent.spawn(f, 'http://www.xiaohuar.com/'),
        gevent.spawn(f, 'https://www.cnblogs.com/dwlsxj/p/RabbitMQ.html'),
        gevent.spawn(f, 'https://www.cnblogs.com/yuanchenqi/articles/5692716.html')
])

end = time.time()
print(end-begin)
