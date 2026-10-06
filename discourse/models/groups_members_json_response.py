from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .member import Member, MemberDict
from .meta import Meta, MetaDict
from .owner import Owner, OwnerDict


class GroupsMembersJsonResponse(SdkBaseModel):
    members: list[Member]
    owners: list[Owner]
    meta: Meta


class GroupsMembersJsonResponseDict(TypedDict):
    members: list[MemberDict]
    owners: list[OwnerDict]
    meta: MetaDict
