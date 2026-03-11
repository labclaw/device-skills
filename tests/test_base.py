"""Tests for base classes."""
from __future__ import annotations

from typing import Any

import pytest

from device_skills.base import BaseAdapter, BaseBrain, BaseProcessor


class StubAdapter(BaseAdapter):
    def __init__(self) -> None:
        self._connected = False

    def info(self) -> dict[str, Any]:
        return {"name": "stub", "vendor": "test"}

    @property
    def connected(self) -> bool:
        return self._connected

    def connect(self) -> bool:
        self._connected = True
        return True

    def disconnect(self) -> None:
        self._connected = False

    def list_datasets(self) -> list[dict[str, Any]]:
        return [{"name": "sample1"}]

    def acquire(self, **kwargs: Any) -> Any:
        return {"data": [1, 2, 3]}

    def process(self, data_path: str, **kwargs: Any) -> Any:
        return {"result": "processed"}


class StubProcessor(BaseProcessor):
    def load(self, path: str) -> Any:
        return [1, 2, 3]

    def transform(self, raw_data: Any) -> Any:
        return [x * 2 for x in raw_data]

    def extract(self, processed_data: Any) -> dict[str, Any]:
        return {"values": processed_data}


class StubBrain(BaseBrain):
    def analyze(self, data: dict[str, Any], context: str = "") -> str:
        return "Analysis: looks good"

    def summarize(self, findings: list[str]) -> str:
        return f"Summary of {len(findings)} findings"


def test_adapter_lifecycle():
    a = StubAdapter()
    assert not a.connected
    assert a.connect()
    assert a.connected
    assert a.info()["name"] == "stub"
    assert len(a.list_datasets()) == 1
    result = a.acquire()
    assert result["data"] == [1, 2, 3]
    assert a.process("path")["result"] == "processed"
    a.disconnect()
    assert not a.connected


def test_processor_pipeline():
    p = StubProcessor()
    raw = p.load("any/path")
    transformed = p.transform(raw)
    extracted = p.extract(transformed)
    assert extracted["values"] == [2, 4, 6]


def test_brain_analyze():
    b = StubBrain()
    result = b.analyze({"data": [1]}, context="test")
    assert "looks good" in result


def test_brain_summarize():
    b = StubBrain()
    result = b.summarize(["finding1", "finding2"])
    assert "2 findings" in result


def test_adapter_is_abstract():
    with pytest.raises(TypeError):
        BaseAdapter()  # type: ignore[abstract]


def test_processor_is_abstract():
    with pytest.raises(TypeError):
        BaseProcessor()  # type: ignore[abstract]


def test_brain_is_abstract():
    with pytest.raises(TypeError):
        BaseBrain()  # type: ignore[abstract]
