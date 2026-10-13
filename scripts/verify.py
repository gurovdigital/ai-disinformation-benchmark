"""Checks this repository: the checksums of the data files, and the figures of datasets.csv counted again from the responses.

    python3 scripts/verify.py

Python 3.9 or later, nothing to install. The last line is VERIFY: OK when everything matches.
"""
import csv, hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
bad = 0

for line in (ROOT / "CHECKSUMS.txt").read_text(encoding="utf-8").splitlines():
    want, name = line.split("  ", 1)
    got = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    if got != want:
        bad += 1
        print("CHECKSUM DIFFERS:", name)
print("checksums checked:", len((ROOT / "CHECKSUMS.txt").read_text(encoding="utf-8").splitlines()))

board = {}
for d in csv.DictReader(open(ROOT / "datasets.csv", encoding="utf-8")):
    folder = ROOT / d["folder"]
    rows = [json.loads(l) for l in open(folder / "responses.jsonl", encoding="utf-8")]
    table = list(csv.DictReader(open(folder / "responses.csv", encoding="utf-8")))
    counted = sum(r["counted"] for r in rows)
    ok = len(rows) == int(d["responses"]) == len(table) and counted == int(d["counted"])
    bad += not ok
    print(f"{d['dataset']}: {len(rows)} responses, {counted} counted", "" if ok else "  <- DIFFERS from datasets.csv")
    for r in rows:
        if r["on_board"]:
            x = board.setdefault(r["assistant"], [0, 0])
            x[0] += 1
            x[1] += r["counted"]

print()
print("Our own measurements on the board, by assistant:")
for name, (n, c) in sorted(board.items(), key=lambda kv: -kv[1][1] / kv[1][0]):
    print(f"  {name:22} {c:4} of {n:4}  {100 * c / n:5.1f}%")
print()
print("VERIFY: OK" if not bad else f"VERIFY: {bad} PROBLEMS")
sys.exit(1 if bad else 0)
