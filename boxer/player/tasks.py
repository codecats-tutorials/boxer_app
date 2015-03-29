# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from celery.task import task

@task
def test(param):
    return 'The test task executed with argument "%s" ' % param


