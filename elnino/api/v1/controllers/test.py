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
import pecan
from pecan import rest
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan
from elnino.api.v1.datamodels import CloudkittyModule


class TestController(rest.RestController):
    """REST Controller for testing.

    """

    _custom_actions = {
        'test': ['GET'],
    }

    @wsme_pecan.wsexpose(CloudkittyModule)
    def test(self):
        """Test api if OK.

        """
        return CloudkittyModule(
                module_id='test',
                description='test',
                enable=True,
                hot_config=True,
                priority=3)
