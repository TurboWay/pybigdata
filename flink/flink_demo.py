#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 17:30
# @Author : way
# @Site : 
# @Describe:

import logging
import os
import shutil
import sys
import tempfile

from pyflink.dataset import ExecutionEnvironment
from pyflink.table import BatchTableEnvironment, TableConfig


def word_count():
    content = "line Licensed to the Apache Software Foundation ASF under one " \
              "line or more contributor license agreements See the NOTICE file " \
              "line distributed with this work for additional information " \
              "line regarding copyright ownership The ASF licenses this file " \
              "to you under the Apache License Version the " \
              "License you may not use this file except in compliance " \
              "with the License"

    t_config = TableConfig()
    env = ExecutionEnvironment.get_execution_environment()
    t_env = BatchTableEnvironment.create(env, t_config)

    # register Results table in table environment
    tmp_dir = tempfile.gettempdir()
    result_path = tmp_dir + '/result'
    if os.path.exists(result_path):
        try:
            if os.path.isfile(result_path):
                os.remove(result_path)
            else:
                shutil.rmtree(result_path)
        except OSError as e:
            logging.error("Error removing directory: %s - %s.", e.filename, e.strerror)

    logging.info("Results directory: %s", result_path)

    sink_ddl = """
        create table Results(
            word VARCHAR,
            `count` BIGINT
        ) with (
            'connector.type' = 'filesystem',
            'format.type' = 'csv',
            'connector.path' = '{}'
        )
        """.format(result_path)
    t_env.sql_update(sink_ddl)

    elements = [(word, 1) for word in content.split(" ")]
    t_env.from_elements(elements, ["word", "count"]) \
        .group_by("word") \
        .select("word, count(1) as count") \
        .insert_into("Results")

    t_env.execute("word_count")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")

    word_count()
