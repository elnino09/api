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
import copy
import itertools

import elnino.api.app
import elnino.config
import elnino.service
import elnino.storage

__all__ = ['list_opts']

_opts = [
    ('api', list(itertools.chain(
        elnino.api.app.api_opts,))),
    ('output', list(itertools.chain(
        elnino.config.output_opts))),
    ('state', list(itertools.chain(
        elnino.config.state_opts))),
    ('storage', list(itertools.chain(
        elnino.storage.storage_opts))),
    (None, list(itertools.chain(
        elnino.api.app.auth_opts,
        elnino.service.service_opts)))
]


def list_opts():
    return [(g, copy.deepcopy(o)) for g, o in _opts]
