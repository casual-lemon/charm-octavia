# Copyright 2018 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

sys.path.append('src')
sys.path.append('src/lib')

# Mock out charmhelpers so that we can test without it.
import charms_openstack.test_mocks  # noqa
charms_openstack.test_mocks.mock_charmhelpers()

import mock
import charms
charms.leadership = mock.MagicMock()
sys.modules['charms.leadership'] = charms.leadership
keystoneauth1 = mock.MagicMock()
novaclient = mock.MagicMock()
sys.modules['charms.leadership'] = charms.leadership
sys.modules['keystoneauth1'] = keystoneauth1
sys.modules['novaclient'] = novaclient
