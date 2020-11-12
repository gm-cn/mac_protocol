# coding=utf-8
# import logging
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, BASE_DIR)
from bmstools.utils import log, auth
from bmstools.pkg.server import server


def main():
    logger = log.setup()
    logger.info("start server")
    private_key, public_key = auth.gen_key()
    with open(os.path.join(BASE_DIR, "/bmstools/pkg/server/private.pem"), "w") as f:
        f.write(private_key)
    with open(os.path.join(BASE_DIR, "/bmstools/pkg/server/public.pem"), "w") as f:
        f.write(public_key)

    s = server.get_server()
    s.run()


if __name__ == '__main__':
    main()
