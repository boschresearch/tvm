# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""UMA codegen for the my_ai_hw accelerator"""

import tvm
import pathlib


def gen_includes() -> str:
    topdir = pathlib.Path(__file__).parent.absolute()

    includes = ""
    includes += f'#include "{topdir}/conv2dnchw.cc"'
    return includes


def gen_replace_call_extern(args: tvm.ir.container.Array) -> str:
    return "my_custom_api_function({}, {}, {})".format(*args)