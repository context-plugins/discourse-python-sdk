from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category1 import Category1, Category1Dict


class CategoryList(SdkBaseModel):
    can_create_category: bool
    can_create_topic: bool
    categories: list[Category1]


class CategoryListDict(TypedDict):
    can_create_category: bool
    can_create_topic: bool
    categories: list[Category1Dict]
