#!/usr/bin/env python3
"""Fail if any Pokémon family is stripped from Emerald Ultimate."""
from pathlib import Path
import re

source = Path("include/config/species_enabled.h").read_text()
disabled = re.findall(r"^#define\s+(P_FAMILY_\w+)\s+FALSE\b", source, re.M)
if disabled:
    raise SystemExit("Disabled families: " + ", ".join(disabled))
families = re.findall(r"^#define\s+P_FAMILY_\w+\s+\S+", source, re.M)
print(f"Emerald Ultimate: {len(families)} Pokémon families configured; none explicitly disabled.")
