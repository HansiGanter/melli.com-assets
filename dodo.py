from pathlib import Path

base = Path(__file__).parent
public = base / "public"


def task_webp():
    "Compresss images into webp format"

    images = (base / "images").rglob("*.*")

    for image in filter(lambda image: image.suffix in ".jpg.png.webp", images):
        target = public / image.relative_to(base).with_suffix(".webp")
        target.parent.mkdir(parents=True, exist_ok=True)

        parts = target.relative_to(base).parts
        if "team" in parts:
            width = 512
        elif "stock" in parts:
            width = 1024
        elif "backgrounds" in parts:
            width = 1024
        else:
            width = 512

        yield {
            "name": image,
            "actions": [f"cwebp -resize 0 {width} -o {target} {image}"],
            "targets": [target],
            "file_dep": [image],
        }
