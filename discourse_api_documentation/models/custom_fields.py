from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CustomFields(SdkBaseModel):
    first_name: OptionalNullable[str] = UNSET


class CustomFieldsDict(TypedDict):
    first_name: NotRequired[str | None]
