from pathlib import Path

import imagesize

base = Path(__file__).relative_to(Path.cwd()).parent
public = base / "public"


def task_webp():
    "Compresss images into webp format"

    images = (base / "images").rglob("*.*")

    for image in filter(lambda image: image.suffix in ".jpg.jpeg.png.webp", images):
        target = public / image.relative_to(base).with_suffix(".webp")
        target.parent.mkdir(parents=True, exist_ok=True)

        # we create a 512px version of every image
        yield {
            "name": target,
            "actions": [f"cwebp -resize 512 0 -o {target} {image}"],
            "targets": [target],
            "file_dep": [image],
        }

        # for images greater than 512px we also create a 1024px version
        source_width, _ = imagesize.get(image)
        if source_width > 512:
            target_1024 = target.with_stem(target.stem + "-1024")
            yield {
                "name": target_1024,
                "actions": [f"cwebp -resize 1024 0 -o {target_1024} {image}"],
                "targets": [target_1024],
                "file_dep": [image],
            }
