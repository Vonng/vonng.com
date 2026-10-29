#!/usr/bin/env python3
"""Rebuild the English charts for /en/pg/pg-nls/ (requires matplotlib).

Data transcribed from languages.png and catalogs.png in the article bundle.
These are September 15, 2026 snapshots, not live translation statistics.
Run from any directory; only languages-en.svg and catalogs-en.svg are written.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BUNDLE = Path(__file__).resolve().parents[1] / "content/pg/pg-nls"
LANGUAGES = [
    ("Ukrainian", "uk", 99),
    ("Swedish", "sv", 99),
    ("Georgian", "ka", 99),
    ("German", "de", 99),
    ("Japanese", "ja", 98),
    ("French", "fr", 94),
    ("Russian", "ru", 91),
    ("Korean", "ko", 89),
    ("Spanish", "es", 89),
    ("Portuguese (Brazil)", "pt_BR", 85),
    ("Greek", "el", 75),
    ("Chinese (Traditional)", "zh_TW", 70),
    ("Italian", "it", 70),
    ("Chinese (Simplified)", "zh_CN", 66),
    ("Czech", "cs", 62),
    ("Turkish", "tr", 58),
    ("Polish", "pl", 46),
]
CATALOGS = [
    ("postgres (server)", 6826, 61),
    ("psql", 1536, 76),
    ("pg_dump", 585, 68),
    ("pg_basebackup", 519, 44),
    ("libpq", 408, 12),
    ("pg_upgrade", 363, 23),
    ("pgscripts", 240, 78),
    ("pg_rewind", 212, 60),
    ("initdb", 210, 94),
    ("pg_combinebackup", 187, 52),
    ("plpgsql", 177, 91),
    ("pg_verifybackup", 166, 48),
    ("pg_ctl", 161, 81),
    ("pg_resetwal", 143, 65),
    ("ecpg", 132, 93),
    ("pg_waldump", 125, 24),
    ("pg_amcheck", 122, 72),
    ("pg_controldata", 106, 74),
    ("plpython", 84, 96),
    ("pg_checksums", 83, 56),
    ("pg_config", 48, 95),
    ("plperl", 43, 93),
    ("pg_test_fsync", 39, 58),
    ("pg_archivecleanup", 34, 79),
    ("ecpglib", 33, 96),
    ("pg_test_timing", 33, 24),
    ("pg_walsummary", 33, 48),
    ("pltcl", 20, 95),
]

INK = "#24282e"
MUTED = "#59636f"
RED = "#c93631"
GOLD = "#c88b21"
GREEN = "#2c7c52"


def canvas(height, rows, title, subtitle):
    fig, ax = plt.subplots(figsize=(14, height), facecolor="white")
    fig.subplots_adjust(left=0.32, right=0.94, top=0.84, bottom=0.115)
    fig.text(0.045, 0.943, title, fontsize=23, weight="bold", color=INK)
    fig.text(0.045, 0.902, subtitle, fontsize=12.5, color=MUTED)
    ax.set_xlim(0, 107)
    ax.set_ylim(rows - 0.35, -0.65)
    ax.set_xticks([])
    ax.tick_params(axis="y", length=0, pad=12, labelsize=12, colors=MUTED)
    for spine in ax.spines.values():
        spine.set_visible(False)
    return fig, ax


def save(fig, filename, title):
    fig.savefig(
        BUNDLE / filename,
        format="svg",
        metadata={
            "Date": None,
            "Title": title,
            "Description": "Historical snapshot: September 15, 2026. Source: babel.postgresql.org; data transcribed from the original Chinese chart in this article bundle.",
            "Creator": "scripts/generate-pg-nls-charts.py (matplotlib)",
        },
    )
    plt.close(fig)


def main():
    plt.rcParams.update({"font.family": ["DejaVu Sans", "sans-serif"], "svg.fonttype": "none", "svg.hashsalt": "pg-nls-20260915"})
    title = "PostgreSQL 19: translation coverage by language"
    fig, ax = canvas(10.4, len(LANGUAGES), title, "Languages represented across nearly all 28 catalogs · September 15, 2026")
    for row, (_, code, value) in enumerate(LANGUAGES):
        color = RED if code == "zh_CN" else "#a7b1bd" if code == "zh_TW" else "#dce1e7"
        ax.barh(row, value, height=0.66, color=color)
        ax.text(value + 1.2, row, f"{value}%", va="center", fontsize=12.5, color=RED if code == "zh_CN" else MUTED)
    ax.set_yticks(range(len(LANGUAGES)), [f"{name}  {code}" for name, code, _ in LANGUAGES])
    ax.get_yticklabels()[13].set_color(RED)
    fig.text(0.045, 0.06, "Georgia: 3.7 million people; all 28 catalogs at 99%.", fontsize=13, color=INK)
    fig.text(0.045, 0.029, "Source: babel.postgresql.org · Historical snapshot reproduced from the original article", fontsize=10.5, color=MUTED)
    save(fig, "languages-en.svg", title)

    title = "Simplified Chinese: only 9 of 28 catalogs qualify"
    fig, ax = canvas(14.2, len(CATALOGS), title, "PostgreSQL 19 · Message counts in parentheses · September 15, 2026")
    for row, (_, _, value) in enumerate(CATALOGS):
        color = GREEN if value >= 80 else GOLD if value >= 50 else RED
        ax.barh(row, value, height=0.65, color=color)
        ax.text(102, row, f"{value}%", va="center", fontsize=12.5, color=MUTED)
    ax.set_yticks(range(len(CATALOGS)), [f"{name}  ({count:,})" for name, count, _ in CATALOGS])
    ax.axvline(80, color=INK, linewidth=1.5, linestyle=(0, (5, 4)))
    ax.text(80, 1.025, "80% release threshold", transform=ax.get_xaxis_transform(), ha="center", fontsize=12, color=INK)
    fig.text(0.045, 0.069, "The largest catalogs lag: postgres has 6,826 messages at 61%; libpq has 408 at 12%.", fontsize=12.5, color=INK)
    fig.text(0.045, 0.042, "Green: 80% or higher · Amber: 50–79% · Red: below 50%", fontsize=11, color=MUTED)
    fig.text(0.045, 0.021, "Source: babel.postgresql.org · Historical snapshot reproduced from the original article", fontsize=10.5, color=MUTED)
    save(fig, "catalogs-en.svg", title)


if __name__ == "__main__":
    main()
