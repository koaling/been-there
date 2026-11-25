"""Validate precedents/*.yaml against the schema in precedents/SCHEMA.md."""
import glob
import re
import sys

import yaml

CAUSES = {
    "no-market-need", "unit-economics", "pricing", "premature-scaling", "competition",
    "timing", "overengineering", "regulation", "labor-model", "distribution", "retention",
    "trust-privacy", "team", "fraud", "platform-dependency",
}
REQUIRED = ["name", "slug", "type", "years", "region", "sector", "causes", "root_cause", "lesson", "status"]
SOURCE_TYPES = {"founder-postmortem", "news", "analysis", "ai-generated"}

errors = []
for path in sorted(glob.glob("been-there/precedents/*.yaml")):
    try:
        d = yaml.safe_load(open(path, encoding="utf-8"))
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid YAML ({e})")
        continue
    for k in REQUIRED:
        if not d.get(k):
            errors.append(f"{path}: missing '{k}'")
    slug = path.split("/")[-1][:-5]
    if d.get("slug") != slug:
        errors.append(f"{path}: slug '{d.get('slug')}' must match file name '{slug}'")
    if d.get("type") not in {"failure", "survivor"}:
        errors.append(f"{path}: type must be failure or survivor")
    causes = d.get("causes") or []
    if not 1 <= len(causes) <= 3:
        errors.append(f"{path}: use 1-3 cause tags")
    for c in causes:
        if c not in CAUSES:
            errors.append(f"{path}: unknown cause tag '{c}'")
    if d.get("status") not in {"needs-source", "verified"}:
        errors.append(f"{path}: status must be needs-source or verified")
    sources = d.get("sources") or []
    if d.get("status") == "verified":
        if not sources:
            errors.append(f"{path}: verified entries need at least one source")
        if sources and all(s.get("type") == "ai-generated" for s in sources):
            errors.append(f"{path}: an ai-generated source can't be the only source")
    for s in sources:
        if s.get("type") not in SOURCE_TYPES:
            errors.append(f"{path}: unknown source type '{s.get('type')}'")
        if not re.match(r"^https?://", str(s.get("url", ""))):
            errors.append(f"{path}: source '{s.get('title', '?')}' needs a URL")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(glob.glob('been-there/precedents/*.yaml'))} precedents valid")
