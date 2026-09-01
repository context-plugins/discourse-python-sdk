from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .suspended_by import SuspendedBy, SuspendedByDict


class Suspension(SdkBaseModel):
    suspend_reason: str
    full_suspend_reason: str
    suspended_till: str
    suspended_at: str
    suspended_by: SuspendedBy


class SuspensionDict(TypedDict):
    suspend_reason: str
    full_suspend_reason: str
    suspended_till: str
    suspended_at: str
    suspended_by: SuspendedBy | SuspendedByDict
