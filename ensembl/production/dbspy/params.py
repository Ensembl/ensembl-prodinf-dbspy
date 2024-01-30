# See the NOTICE file distributed with this work for additional information
#   regarding copyright ownership.
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Module containing specialised parameters to be used in the main module.
"""

from typing import Any

from fastapi import Path, Query


def HostPath(**kwargs) -> Any:
    return Path(..., regex=r"^[a-z0-9\-\.]+$", **kwargs)


def DBNamePath(**kwargs) -> Any:
    return Path(..., regex=r"^\w+$", **kwargs)


def PortPath(**kwargs) -> Any:
    return Path(..., ge=0, le=9999, **kwargs)


def PatternQuery(**kwargs) -> Any:
    return Query(None, regex=r"^[\w\%]+$", **kwargs)
