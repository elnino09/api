# -*- coding: utf-8 -*-
# Copyright 2014 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Stéphane Albert
#
import abc

from oslo_config import cfg
import six
from stevedore import driver


storage_opts = [
    cfg.StrOpt('backend',
               default='sqlalchemy',
               help='Name of the storage backend driver.')
]

CONF = cfg.CONF
CONF.register_opts(storage_opts, group='storage')

STORAGES_NAMESPACE = 'elnino.storage.backends'


def get_storage(collector=None):
    storage_args = {}
    backend = driver.DriverManager(
        STORAGES_NAMESPACE,
        cfg.CONF.storage.backend,
        invoke_on_load=True,
        invoke_kwds=storage_args).driver
    return backend


@six.add_metaclass(abc.ABCMeta)
class BaseStorage(object):
    """Base Storage class:

        Handle incoming data from the global orchestrator, and store them.
    """
    def __init__(self, **kwargs):
        pass
