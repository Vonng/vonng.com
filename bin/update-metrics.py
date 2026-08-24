#!/usr/bin/env python3
"""Refresh data/metrics.yaml from the public sources behind the About page.

Three numbers, three public sources, no credentials:

  stars      sum of stargazers over every public repo the user owns
             https://api.github.com/users/<user>/repos
  followers  https://api.github.com/users/<user>
  rank       position on committers.top for a country, read out of the badge
             https://user-badge.committers.top/<country>/<user>.svg

The build fetches the same three sources itself (layouts/_partials/metrics.html)
and only falls back to the file when it cannot reach them, so running this is
about keeping a sane number checked in — for offline builds, and for anywhere
else the numbers get quoted.

Usage:
  python3 bin/update-metrics.py            # report the drift, write nothing
  python3 bin/update-metrics.py --write    # rewrite data/metrics.yaml
"""

import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date, timezone, datetime
from pathlib import Path

FILE = Path(__file__).resolve().parent.parent / "data" / "metrics.yaml"
TIMEOUT = 20
HEADERS = {"User-Agent": "vonng.com-metrics", "Accept": "application/vnd.github+json"}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8")


def stars(user):
    """Sum stargazers over every public repo the user owns."""
    total, page = 0, 1
    while True:
        repos = json.loads(
            get(f"https://api.github.com/users/{user}/repos"
                f"?per_page=100&type=owner&page={page}")
        )
        total += sum(r["stargazers_count"] for r in repos)
        if len(repos) < 100:
            return total
        page += 1


def followers(user):
    return json.loads(get(f"https://api.github.com/users/{user}"))["followers"]


def rank(country, user):
    """Read `committers.top rank: Singapore #5` out of the badge title."""
    svg = get(f"https://user-badge.committers.top/{country}/{user}.svg")
    found = re.search(r"rank:[^<]*#(\d+)", svg)
    if not found:
        raise ValueError("no rank in the committers.top badge")
    return int(found.group(1))


def main():
    text = FILE.read_text()
    current = {
        key: int(re.search(rf"^{key}:\s*(\d+)", text, re.M).group(1))
        for key in ("stars", "followers", "rank")
    }
    user = re.search(r"^user:\s*(\S+)", text, re.M).group(1)
    country = re.search(r"^country:\s*(\S+)", text, re.M).group(1)

    fresh, failed = {}, False
    for key, fetch in (("stars", lambda: stars(user)),
                       ("followers", lambda: followers(user)),
                       ("rank", lambda: rank(country, user))):
        try:
            fresh[key] = fetch()
        except (urllib.error.URLError, ValueError, KeyError, TimeoutError) as err:
            print(f"  {key:<10} FAILED: {err}", file=sys.stderr)
            fresh[key], failed = current[key], True

    for key in current:
        was, now = current[key], fresh[key]
        arrow = "  (unchanged)" if was == now else f"  <- {was}"
        print(f"  {key:<10} {now}{arrow}")

    if "--write" not in sys.argv:
        print("\nnothing written; pass --write to update data/metrics.yaml")
        return 1 if failed else 0
    if fresh == current:
        print("\ndata/metrics.yaml is already current")
        return 1 if failed else 0

    today = datetime.now(timezone.utc).date().isoformat()
    text = re.sub(r"^updated:.*$", f"updated: {today}", text, count=1, flags=re.M)
    for key, value in fresh.items():
        text = re.sub(rf"^({key}:\s*)\d+", rf"\g<1>{value}", text, count=1, flags=re.M)
    FILE.write_text(text)
    print(f"\ndata/metrics.yaml updated ({today})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
