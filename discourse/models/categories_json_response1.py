from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category_list import CategoryList, CategoryListDict


class CategoriesJsonResponse1(SdkBaseModel):
    category_list: CategoryList


class CategoriesJsonResponse1Dict(TypedDict):
    category_list: CategoryList | CategoryListDict
