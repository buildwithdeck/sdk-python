"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from deck_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class LinkTokenGetResponseLanguage(str, Enum):
    r"""The language used for the Link session corresponding to the provided Link token"""

    EN = "EN"
    ES = "ES"
    FR = "FR"
    DE = "DE"
    IT = "IT"
    PT = "PT"
    NL = "NL"
    PL = "PL"
    SV = "SV"
    DA = "DA"
    NO = "NO"
    ET = "ET"
    LT = "LT"
    LV = "LV"
    RO = "RO"


class LinkTokenGetResponseBetaSourceStatus(str, Enum):
    r"""The beta source status filter from which data sources will be displayed during the Link session corresponding to the provided Link token."""

    LIVE_AND_BETA = "LiveAndBeta"
    ONLY_LIVE = "OnlyLive"
    ONLY_BETA = "OnlyBeta"


class LinkTokenGetResponseTypedDict(TypedDict):
    language: NotRequired[Nullable[LinkTokenGetResponseLanguage]]
    r"""The language used for the Link session corresponding to the provided Link token"""
    beta_source_status: NotRequired[Nullable[LinkTokenGetResponseBetaSourceStatus]]
    r"""The beta source status filter from which data sources will be displayed during the Link session corresponding to the provided Link token."""
    countries: NotRequired[Nullable[List[str]]]
    r"""The countries filter from which data sources will be displayed during the Link session corresponding to the provided Link token"""
    source_types: NotRequired[Nullable[List[str]]]
    r"""The source types filter from which data sources will be displayed during the Link session corresponding to the provided Link token"""
    source_guids: NotRequired[Nullable[List[str]]]


class LinkTokenGetResponse(BaseModel):
    language: OptionalNullable[LinkTokenGetResponseLanguage] = UNSET
    r"""The language used for the Link session corresponding to the provided Link token"""

    beta_source_status: OptionalNullable[LinkTokenGetResponseBetaSourceStatus] = UNSET
    r"""The beta source status filter from which data sources will be displayed during the Link session corresponding to the provided Link token."""

    countries: OptionalNullable[List[str]] = UNSET
    r"""The countries filter from which data sources will be displayed during the Link session corresponding to the provided Link token"""

    source_types: OptionalNullable[List[str]] = UNSET
    r"""The source types filter from which data sources will be displayed during the Link session corresponding to the provided Link token"""

    source_guids: OptionalNullable[List[str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "language",
            "beta_source_status",
            "countries",
            "source_types",
            "source_guids",
        ]
        nullable_fields = [
            "language",
            "beta_source_status",
            "countries",
            "source_types",
            "source_guids",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
