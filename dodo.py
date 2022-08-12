from itertools import chain
from pathlib import Path

base = Path(__file__).parent
public = base / "public"


def task_team_photos():
    "Compresss team photos into webp format"

    photos = (base / "team").rglob("*.jpg")
    for photo in photos:
        target = public / photo.relative_to(base).with_suffix(".webp")
        target.parent.mkdir(parents=True, exist_ok=True)

        yield {
            "name": photo,
            "actions": [f"cwebp -resize 0 512 -o {target} {photo}"],
            "targets": [target],
            "file_dep": [photo],
        }


def task_stock():
    "Compresss stock photos into webp format"

    stock = (base / "stock").rglob("*.jpg")
    jobs = (base / "jobs").rglob("*.jpg")
    for photo in chain(stock, jobs):
        target = public / photo.relative_to(base).with_suffix(".webp")
        target.parent.mkdir(parents=True, exist_ok=True)

        yield {
            "name": photo,
            "actions": [f"cwebp -resize 0 1024 -o {target} {photo}"],
            "targets": [target],
            "file_dep": [photo],
        }
