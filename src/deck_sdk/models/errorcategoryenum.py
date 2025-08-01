"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class ErrorCategoryEnum(str, Enum):
    INVALID_REQUEST = "INVALID_REQUEST"
    INVALID_RESULT = "INVALID_RESULT"
    INVALID_INPUT = "INVALID_INPUT"
    DATA_SOURCE_ERROR = "DATA_SOURCE_ERROR"
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"
    API_ERROR = "API_ERROR"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    RECAPTCHA_ERROR = "RECAPTCHA_ERROR"
    FETCH_BALANCE = "FETCH_BALANCE"
    ADD_PAYMENT_METHOD = "ADD_PAYMENT_METHOD"
    FETCH_PAYMENT_METHODS = "FETCH_PAYMENT_METHODS"
    PAYMENT = "PAYMENT"
