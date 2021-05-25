# -*- coding: utf-8 -*-
from sage.app import application, logger

if __name__ == '__main__':
    # start Application
    logger.info("Start application ...")
    application.run(host="0.0.0.0", port=5000, debug=True)
