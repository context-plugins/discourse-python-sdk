from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .extras import Extras, ExtrasDict
from .group1 import Group1, Group1Dict


class GroupsByIdJsonResponse(SdkBaseModel):
    group: Group1
    extras: Extras


class GroupsByIdJsonResponseDict(TypedDict):
    group: Group1Dict
    extras: ExtrasDict
