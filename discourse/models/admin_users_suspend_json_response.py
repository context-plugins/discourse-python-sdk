from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .suspension import Suspension, SuspensionDict


class AdminUsersSuspendJsonResponse(SdkBaseModel):
    suspension: Suspension


class AdminUsersSuspendJsonResponseDict(TypedDict):
    suspension: Suspension | SuspensionDict
