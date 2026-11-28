#!/usr/bin/env python3
"""Convert openapi/openapi.yaml (OpenAPI 3.2) into an OpenAPI 3.1.1 document.

openapi-python-client only accepts 3.1.x, so the generator reads the converted copy.
Usage: downgrade_openapi.py <input-3.2.yaml> <output-3.1.yaml>
"""

from __future__ import annotations

import sys
from typing import Any

import yaml

TAG_ONLY_32 = ("parent", "kind", "summary")


def _strip_server_names(servers: list[dict[str, Any]] | None) -> None:
    for server in servers or []:
        server.pop("name", None)


def _convert_example(example: Any) -> None:
    if isinstance(example, dict) and "$ref" not in example:
        if "dataValue" in example:
            example["value"] = example.pop("dataValue")
        example.pop("serializedValue", None)


def _walk(node: Any) -> None:
    if isinstance(node, dict):
        if isinstance(node.get("servers"), list):
            _strip_server_names(node["servers"])
        examples = node.get("examples")
        if isinstance(examples, dict):
            for example in examples.values():
                _convert_example(example)
        for value in node.values():
            _walk(value)
    elif isinstance(node, list):
        for item in node:
            _walk(item)


def downgrade(doc: dict[str, Any]) -> dict[str, Any]:
    doc["openapi"] = "3.1.1"
    doc.pop("$self", None)
    for tag in doc.get("tags", []):
        summary = tag.get("summary")
        if summary and not tag.get("description"):
            tag["description"] = summary
        for key in TAG_ONLY_32:
            tag.pop(key, None)
    _walk(doc)
    return doc


class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def _str_presenter(dumper: yaml.SafeDumper, data: str) -> yaml.ScalarNode:
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_Dumper.add_representer(str, _str_presenter)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: downgrade_openapi.py <input-3.2.yaml> <output-3.1.yaml>")
    with open(sys.argv[1], encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    with open(sys.argv[2], "w", encoding="utf-8") as fh:
        yaml.dump(downgrade(doc), fh, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=110)


if __name__ == "__main__":
    main()
