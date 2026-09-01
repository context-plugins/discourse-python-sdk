from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Meta1(SdkBaseModel):
    last_updated_at: str | None
    total_rows_directory_items: int
    load_more_directory_items: str


class Meta1Dict(TypedDict):
    last_updated_at: str | None
    total_rows_directory_items: int
    load_more_directory_items: str
