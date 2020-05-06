#!/usr/bin/env python
# Copyright (C) 2019-2020 All rights reserved.
# FILENAME:  environment.py
# VERSION: 	 1.0
# CREATED: 	 2020-04-28 16:30
# AUTHOR: 	 Aekasitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
"""Module defining Environment Name and Type"""
import os
AVAILABLE_ENV_NAMES = ('development', 'production')
ENV_NAME = os.environ.get('ENV_NAME', 'development')
IS_PRODUCTION = (ENV_NAME == 'production')

if ENV_NAME not in AVAILABLE_ENV_NAMES:
  raise ValueError(f'Environment Variable $ENV_NAME invalid: `{ENV_NAME}`')