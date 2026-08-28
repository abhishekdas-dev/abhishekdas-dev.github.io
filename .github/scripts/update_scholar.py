#!/usr/bin/env python3
"""Fetch Google Scholar citation stats and write scholar.json.

Google Scholar has no official API and may rate-limit or block automated
requests (including from CI runners). On any failure this script leaves the
existing scholar.json untouched and exits 0, so the site's badges keep showing
the last known-good values instead of breaking.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "e3bDokMAAAAJ")
OUT = os.environ.get("SCHOLAR_OUT", "scholar.json")
URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def skip(msg: str) -> None:
    """Log a warning and exit successfully without changing scholar.json."""
    print(f"::warning::{msg}")
    sys.exit(0)


def main() -> None:
    req = urllib.request.Request(URL, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001 - network/blocked, keep last value
        skip(f"Could not fetch Google Scholar: {exc}. Keeping existing stats.")

    if "gsc_rsb_std" not in html:
        skip("Google Scholar returned no stats (likely rate-limited). Keeping existing stats.")

    nums = [int(x) for x in re.findall(r'gsc_rsb_std">(\d+)<', html)]
    if len(nums) < 3:
        skip("Could not parse the Google Scholar stats table. Keeping existing stats.")

    data = {
        "citations": nums[0],
        "hindex": nums[2],
        "i10index": nums[4] if len(nums) > 4 else 0,
        "updated": datetime.date.today().isoformat(),
    }

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")

    print(f"Wrote {OUT}: {data}")


if __name__ == "__main__":
    main()
