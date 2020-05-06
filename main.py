#!/usr/bin/python
# coding:utf-8
# Copyright (C) 2019-2020 All rights reserved.
# FILENAME:  main.py
# VERSION: 	 1.0
# CREATED: 	 2020-05-06 19:20
# AUTHOR: 	 Aekasitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
import asyncio
from argparse import ArgumentParser
### Local Modules ###
from configs.environment import IS_PRODUCTION
from helpers.async_logger import AsyncLogger
from helpers.pickler import Pickler

async def main():
  ### Parse Arguments ###
  parser = ArgumentParser(description='Kaggle Competition Boilerplate by @aekasitt')
  parser.add_argument('--production', '-p', \
      help='Overrides IS_PRODUCTION check and run in production', \
        action='store_true', default=False)
  args = parser.parse_args()
  ### Initiate Logger Instance ###
  logger = AsyncLogger.get_instance('scrap')
  await logger.info(args)
  ### Initiate Pickler Instance ###
  pickler = Pickler.get_instance()
  welcome_msg = await pickler.load('welcome_msg') or 'Hello, World!'
  await pickler.save('welcome_msg', welcome_msg)
  await logger.infoSuccess(welcome_msg)
  AsyncLogger.release_instance()
  Pickler.release_instance()

if __name__ == '__main__':
  asyncio.run(main())