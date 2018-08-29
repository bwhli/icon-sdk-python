# -*- coding: utf-8 -*-
# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from unittest import TestCase, main
from IconService.wallet.wallet import KeyWallet
from IconService.Icon_service import IconService
from IconService.providers.http_provider import HTTPProvider
from IconService.libs.in_memory_zip import gen_deploy_data_content
from tests.example_config import TEST_PRIVATE_KEY, TEST_HTTP_ENDPOINT_URI_V3


class TestSendSuper(TestCase):
    """
    A super class of other send test class, it is for unit tests of sending transaction.
    All of sup classes for testing sending transaction extends this super class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Sets needed data like an instance of a wallet and IconService
        and default values used to make 4 types of transactions. (transfer, call, deploy, message)
        """
        cls.wallet = KeyWallet.load(TEST_PRIVATE_KEY)
        cls.icon_service = IconService(HTTPProvider(TEST_HTTP_ENDPOINT_URI_V3))

        # bytes of sample_token's content
        # current_dir_path = path.abspath(path.dirname(__file__))
        # score_path = path.join(current_dir_path, 'sample_token')
        # install_content_bytes = gen_deploy_data_content(score_path)
        install_content_bytes = b'PK\x03\x04\x14\x00\x00\x00\x08\x00P\x95\xf4LPJ<\xd7\'\x02\x00\x00]\x06\x00\x00V\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token/sample_token.py\x8dTQk\xdb0\x10~\xf7\xaf\x10}\x89\x9d\xae%c/\xc3,c\xc9\xb2\x87A\xe8\n\xf1\x06\xa3\x14!\xdb\xe7`\xaaHFRBC\xe9\x7f\xdf\xd9\x91%%\x8d\xd3\xe9)\xd1\xf9\xbe\xfb\xbeOwW)\xb9!u!\x85\x06\xb5\xab\x0b \xf5\xa6\x91\xca\x90q\x14E\x05gZ\x93\x15\xdb4\x1c2\xf9\x04"\xfe\x89\x1f\xae\n\xa9`\xce4$i\x14\x11<\x94\xceg\xcb\xd9\xdd\xf7\x1f+2%\xa3\x9cq&\n\xd0#\x1b\xcb~e\xb3%]\xfd\xbe\xbf_\xfem\xe3F\x1a\xc6\xa9\xde6\r\xdf\x8f\x0e\x00\xdf`\x07\xc2p\xb9\x8ekQ\xc23\x94\xd3OI\x17(\xa1"\x99bBW\xa0b\r\xbc\xfa@XY*Z!\xe9\x94\xcc\xf0\'hm\xef\x8c\x0cnv\x8co!%\xb50IJ\x1aT\x119<JkQ\x1bJ-^\x99\xa7\xc4\xa9Z0\xc3\xf2V\x19\xb9\xf9J\xee\xa4\x80\xb4Kk\x0f\x12F\x0e\xc9\xadK/\xf3\xc4\x07\x11\n#\xa14\x94\xfa\x87\xa9\xc5<\xb6\xb1\xd0\x86\xb6\xaa\xe5H\xcd\xbe\x81i\xcb\xf3\x14\xac\xf7\x11\x81\x16ua<Ro\xf6y\x14\xa7S\nd\xaa\x91\x10\xb7J;\xde\x07r\x9d3\x08\xfcq2\x99 \x0c\x14\xf5\x86qw\xf9\xf9\x82\xfc\x00\xd5\xd6j\xcf\x89\xf0\xa0\x12\x19c\x112\x1e\xf7E\xa2K\x9e\xddj0qx1h\xcaC\xf7\x7f\xa3\xd7\x98\x82-\xa3\x1e\xb1j\x98xd\xc3\xb6)\x99\x81\xce\x85\xcb\xca\xec\x87I\xdf\x95\xcf\x06\x94`<V\xc0J)\xf8~\x9a\xa9-\xf8\xce\x0c\x0bzt4\xd1\x83+0[%\xcej]\xa3\xd6\xff\xaddeSY\rN\xc1{\xb5\x9ds.\xf51\x9c\ts<e\xf4\xdc\x98\xd1\xb7sF\x83Ak\t\xe4R\xf2\xd4\xbfq]\x1d\xca\x07\xfc=rB\xbe\xf4\xf9.\xc1=\xb5\xc2\x95\xa0L\\]\xbd\xf8\x84\xd7\x91\xee\x9d\xc0\xd4\x97C\xee\xebU\xf2\xa6\xa7\x9cV\x9f\xdb6\xc8\xa5\xe8\x8d\xa5\xf2\x0e\x94\x91\xc3@m\xec\xba\x879\xc6q;\xcc\x97\xf4v\xf6.&\xa7/\xd7\xf6\xc0I\x83\xf8\xde;\xb3\x15\x876\xa0\x7f\x98\x81\xb6\x0c\xb1\x82\xa1r\xb0\x16-X.\x15.\x80\x9c\x15OCCuX\xb9\xd1?PK\x03\x04\x14\x00\x00\x00\x08\x00P\x95\xf4L\x08M\x80\x83"\x00\x00\x00&\x00\x00\x00R\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token/__init__.pyK+\xca\xcfU\xd0+N\xcc-\xc8I\x8d/\xc9\xcfN\xcdS\xc8\xcc-\xc8/*Q\x08\x06\x8b\x85\x80\x84\xb8\x00PK\x03\x04\x14\x00\x00\x00\x08\x00P\x95\xf4L\x05}|\x97B\x00\x00\x00\\\x00\x00\x00S\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token/package.json\xab\xe6R\x00\x02\xa5\xb2\xd4\xa2\xe2\xcc\xfc<%+\x05%\x03=\x03=C%\x1d\x88xnbf^|ZfN*H\xa681\xb7 \'5\xbe$?;5\x0fEAqr~\x11XE0XE\x08X\x01W-\x00PK\x01\x02\x14\x03\x14\x00\x00\x00\x08\x00P\x95\xf4LPJ<\xd7\'\x02\x00\x00]\x06\x00\x00V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x00\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token/sample_token.pyPK\x01\x02\x14\x03\x14\x00\x00\x00\x08\x00P\x95\xf4L\x08M\x80\x83"\x00\x00\x00&\x00\x00\x00R\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x9b\x02\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token/__init__.pyPK\x01\x02\x14\x03\x14\x00\x00\x00\x08\x00P\x95\xf4L\x05}|\x97B\x00\x00\x00\\\x00\x00\x00S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81-\x03\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token/package.jsonPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\x85\x01\x00\x00\xe0\x03\x00\x00\x00\x00'

        # bytes of sample_token2's content
        # score_path = path.join(current_dir_path, 'sample_token2')
        # update_content_bytes = gen_deploy_data_content(score_path)
        update_content_bytes = b'PK\x03\x04\x14\x00\x00\x00\x08\x00\'|\x14M|9?K6\x02\x00\x00\x95\x06\x00\x00W\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token2/sample_token.py\x8dT]k\xdb0\x14}\xf7\xaf\x10y\x89\x9d\xae%c/\xc3,c\xc92\xd8 t\x85d\x832\x8a\x90\xed\xeb\xceT\x91\x8c\xa4\x84\x86\xd2\xff\xbekG\x96\x94\x0f\xa7\xd3\x93\xad\xab{\xee\xb9G\xe7\xaaTrM\xaa\\\n\rj[\xe5@\xaau-\x95!\xa3(\x8ar\xce\xb4&K\xb6\xae9\xac\xe4\x13\x88\xf8\x07\x1e\\\xe6R\xc1\x8ciH\xd2("\xb8(\x9dM\x17\xd3\xdb\xaf\xdf\x96dB\x86\x19\xe3L\xe4\xa0\x876\xb6\xfa\xb9\x9a.\xe8\xf2\xd7\xdd\xdd\xe2\xbe\x89\x1bi\x18\xa7zS\xd7|7\xdc\x03|\x81-\x08\xc3\xe5c\\\x89\x02\x9e\xa1\x98|H\xda@\x01%Y)&t\t*\xd6\xc0\xcbw\x84\x15\x85\xa2%\x92N\xc9\x14?Ak\xbbgd\xb0\xb3e|\x03)\xa9\x84IRRc\x17\x91\xc3\xa3\xb4\x12\x95\xa1\xd4\xe2\x15YJ\\WsfX\xd6tF\xae?\x93[) m\xd3\x9a\x85\x84\x91Cr\xe3\xd2\x8b,\xf1A\x84\xc2H\xd8\x1a\xb6\xfa\x9b\xa9\xf9,\xb6\xb1P\x86\xa6\xaa\xe5H\xcd\xae\x86I\xc3\xf3\x18\xac\xd3\x11\x81\xe6Un<R\'\xf6y\x14\xd7\xa7\x14\xc8T#!n;my\xef\xc9\xb5\xca \xf0\xfb\xf1x\x8c0\x90Wk\xc6\xdd\xe6\xc7\x0b\xed\x07\xa8\xb6V\xb3\x8e\x1a\x0f*\x91\x11\x16!\xa3QW$\xba\xa4\xd9\x8d\x06\x13\x87\x1b\xbd\xa2\xfci\xff\xd7\xfa\x11S\xd02\xea\x01\xab\x86\x89\x072l\xea\x82\x19hU\xb8\xdc\x99=\x98t\xae|6\xa0\x04\xe3\xb1\x02VH\xc1w\x93\x95\xda\x80wfX\xd0\xa3\xa3\x88\x1e\\\x81\xd9(A\xc6\xff\x89h\xdb\xa3\xb2\xecu{o\x8dc\x85\\\xeaC\xe8}s8M\xf4\xdc8\xd1\xd3y\xa2\xc1@5\x042)y\xea\xef\xb2*\xf7\xe5\x03\xfe\x1e9!\x9f\xba|\x97\xe0\xaeT\xe1\xe8+\x13\x97\x83\x17\x9f\xf0:\xd4\x9d\x12\x98\xfa\xb2\xcf}\x1d$\'\xdeq\xbd\xfa\xdc\xc6\x08\x97\xa2\xd7\x96\xca\x1bPF\xf6\x035\xb1\xab\x0e\xe6\x10\xc7\xbdU\xbe\xa4\x97\xb3S19\xbe\xb9\xc6\x03G\x06\xf1\x1e;\xf3\xfa\xf5\xbdt\xfeb\xce[\xe3\x00+\x18\x1e\x07k\xd1\x82G\xa4\xc4A\xcfX\xfe\xd47<\xfei}\xd3\xdb\x7f\x81s\xe9q\xb4Q\'<\x07\xdf\x9b3\x83(\xfa\x07PK\x03\x04\x14\x00\x00\x00\x08\x00P\x95\xf4L\x08M\x80\x83"\x00\x00\x00&\x00\x00\x00S\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token2/__init__.pyK+\xca\xcfU\xd0+N\xcc-\xc8I\x8d/\xc9\xcfN\xcdS\xc8\xcc-\xc8/*Q\x08\x06\x8b\x85\x80\x84\xb8\x00PK\x03\x04\x14\x00\x00\x00\x08\x00P\x95\xf4L\xb85\xd6|B\x00\x00\x00\\\x00\x00\x00T\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token2/package.json\xab\xe6R\x00\x02\xa5\xb2\xd4\xa2\xe2\xcc\xfc<%+\x05%\x03=\x03=#%\x1d\x88xnbf^|ZfN*H\xa681\xb7 \'5\xbe$?;5\x0fEAqr~\x11XE0XE\x08X\x01W-\x00PK\x01\x02\x14\x03\x14\x00\x00\x00\x08\x00\'|\x14M|9?K6\x02\x00\x00\x95\x06\x00\x00W\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x00\x00\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token2/sample_token.pyPK\x01\x02\x14\x03\x14\x00\x00\x00\x08\x00P\x95\xf4L\x08M\x80\x83"\x00\x00\x00&\x00\x00\x00S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\xab\x02\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token2/__init__.pyPK\x01\x02\x14\x03\x14\x00\x00\x00\x08\x00P\x95\xf4L\xb85\xd6|B\x00\x00\x00\\\x00\x00\x00T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81>\x03\x00\x00Users/boyeon/PycharmProjects/IconPythonSDK/tests/api_send/sample_token2/package.jsonPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\x88\x01\x00\x00\xf2\x03\x00\x00\x00\x00'

        cls.setting = {
            "from": cls.wallet.get_address(),
            "to": "hx5bfdb090f43a808005ffc27c25b213145e80b7cd",
            "to_governance": "cx0000000000000000000000000000000000000001",
            "step_limit": 4000000000,
            "nid": 3,
            "nonce": 3,
            # It is used to send icx(transfer) only.
            "value": 1000000000000000000,
            # It is used to send call only.
            "method": "transfer",
            "params_call": {
                "to": "hxab2d8215eab14bc6bdd8bfb2c8151257032ecd8b",
                "value": "0x1"
            },
            # It is used to send SCORE install(deploy).
            # If SCORE's address is as follows, it means install SCORE.
            "to_install": "cx0000000000000000000000000000000000000000",
            "content_type": "application/zip",
            # Data type of content should be bytes.
            "content_install": install_content_bytes,
            "content_update": update_content_bytes,
            # It is used to deploy only.(install)
            "params_install": {
                "init_supply": 10000
            },
            # It is used to send message only.
            "data": "test"
        }


if __name__ == "__main__":
    main()

