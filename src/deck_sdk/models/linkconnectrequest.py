"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .linkconnectrequestfield import (
    LinkConnectRequestField,
    LinkConnectRequestFieldTypedDict,
)
from deck_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class LinkConnectRequestTypedDict(TypedDict):
    link_token: str
    r"""The link_token, must be provided when calling Link endpoints, for identifying the Link session."""
    source_id: str
    r"""Identifier of the data source to connect to."""
    fields: List[LinkConnectRequestFieldTypedDict]
    r"""List of values provided for fields specific to the selected source"""
    terms_of_use_url: NotRequired[Nullable[str]]
    r"""The accepted terms of use by the end-user"""
    privacy_policy_url: NotRequired[Nullable[str]]
    r"""The accepted privacy policy by the end-user"""


class LinkConnectRequest(BaseModel):
    link_token: str
    r"""The link_token, must be provided when calling Link endpoints, for identifying the Link session."""

    source_id: str
    r"""Identifier of the data source to connect to."""

    fields: List[LinkConnectRequestField]
    r"""List of values provided for fields specific to the selected source"""

    terms_of_use_url: OptionalNullable[str] = UNSET
    r"""The accepted terms of use by the end-user"""

    privacy_policy_url: OptionalNullable[str] = UNSET
    r"""The accepted privacy policy by the end-user"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["terms_of_use_url", "privacy_policy_url"]
        nullable_fields = ["terms_of_use_url", "privacy_policy_url"]
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
