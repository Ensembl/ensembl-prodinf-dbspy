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
