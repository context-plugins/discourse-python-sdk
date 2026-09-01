from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccessControl(SdkBaseModel):
    mandatory_acl: Any
    banned_acl: Any


class AccessControlDict(TypedDict):
    mandatory_acl: Any
    banned_acl: Any
