"""
启动界面
"""
from tornado import ioloop, web
import logging
from API import *
from API.Test import *

# 1.消息记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# 2.获取局域网ip
def get_local_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


# 2.配置app路由url
def make_app():
    # 路由
    application = [
        (r"/", Test),  # 测试
    ]
    app = web.Application(application)

    return app


if __name__ == '__main__':
    app = make_app()
    # 端口
    port = 5000
    # 局域网访问
    app.listen(port, address="0.0.0.0")
    # 事件的提示
    logger.info(f"service started, listening port 5000:")
    logger.info(f"local ip: http://127.0.0.1:{port}")
    logger.info(f"local ip: http://{get_local_ip()}:{port}")

    # 开始事件循环
    ioloop.IOLoop.current().start()
