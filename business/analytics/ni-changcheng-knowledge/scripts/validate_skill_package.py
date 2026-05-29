#!/usr/bin/env python3
"""Validator for the ni-changcheng-knowledge skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "SKILL.md",
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "agents/openai.yaml",
]

FRONTMATTER_REQUIRED = {"name:", "description:"}

SKILL_REQUIRED_SECTIONS = [
    "## 身份",
    "## 核心指令",
    "## 风格约束",
    "## 知识边界",
]

YAML_REQUIRED = {
    "interface:",
    "display_name:",
    "short_description:",
    "default_prompt:",
}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    # Check required files
    for rel in REQUIRED:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")

    # Check SKILL.md
    skill_path = root / "SKILL.md"
    if skill_path.exists():
        content = skill_path.read_text(encoding="utf-8", errors="ignore")

        # Check frontmatter
        if not re.search(r"^---\n.*?^---", content, flags=re.S | re.M):
            errors.append("SKILL.md missing YAML frontmatter (--- block)")
        else:
            # Extract frontmatter and check for invalid characters
            fm_match = re.search(r"^---\n(.*?)^---", content, flags=re.S | re.M)
            if fm_match:
                fm = fm_match.group(1)
                # Check for non-ASCII in frontmatter keys/values that could cause issues
                for line_num, line in enumerate(fm.strip().split("\n"), start=2):
                    # Check for Chinese characters in YAML keys (before colon)
                    key_part = line.split(":")[0] if ":" in line else line
                    if re.search(r"[\u4e00-\u9fff]", key_part):
                        errors.append(
                            f"SKILL.md frontmatter line {line_num}: "
                            f"Chinese character in YAML key '{key_part}' - use English only"
                        )
                    # Check for Chinese in YAML array values like tags: [中文]
                    if re.search(r"\[.*[\u4e00-\u9fff].*\]", line):
                        errors.append(
                            f"SKILL.md frontmatter line {line_num}: "
                            f"Chinese characters in YAML array - use English tags only"
                        )

                # Check required frontmatter fields
                for field in FRONTMATTER_REQUIRED:
                    if field not in fm:
                        errors.append(f"SKILL.md frontmatter missing required field: {field}")

                # Check for $ prefix reference in SKILL.md or openai.yaml
                yaml_content = ""
                yaml_path = root / "agents" / "openai.yaml"
                if yaml_path.exists():
                    yaml_content = yaml_path.read_text(encoding="utf-8", errors="ignore")
                if "$ni-changcheng-knowledge" not in content and "$ni-changcheng-knowledge" not in yaml_content:
                    errors.append(
                        "SKILL.md or openai.yaml should reference $ni-changcheng-knowledge"
                    )

        # Check required sections
        for section in SKILL_REQUIRED_SECTIONS:
            if section not in content:
                errors.append(f"SKILL.md missing required section: {section}")
    else:
        errors.append("SKILL.md not found")

    # Check agents/openai.yaml
    yaml_path = root / "agents" / "openai.yaml"
    if yaml_path.exists():
        yaml_content = yaml_path.read_text(encoding="utf-8", errors="ignore")
        for term in YAML_REQUIRED:
            if term not in yaml_content:
                errors.append(f"agents/openai.yaml missing: {term}")
    else:
        errors.append("agents/openai.yaml not found")

    # Check VERSION
    version_path = root / "VERSION"
    if version_path.exists():
        ver = version_path.read_text(encoding="utf-8").strip()
        if not re.match(r"\d+\.\d+\.\d+", ver):
            errors.append(f"VERSION format invalid: '{ver}', expected X.Y.Z")
    else:
        errors.append("VERSION not found")

    # Check knowledge source files exist
    context_manual = Path(r"d:\Trae工作内容\BI数据分析\00_上下文衔接手册.md")
    if not context_manual.exists():
        errors.append(f"Knowledge source not found: {context_manual}")

    # Result
    if errors:
        print(f"VALIDATION FAILED - {len(errors)} error(s):")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    else:
        print("VALIDATION PASSED - skill package is complete")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
