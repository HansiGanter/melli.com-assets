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

        # for images greater than 512px we also create a 1024px/1536px version
        for width in 1024, 1536, 2048:
            source_width, _ = imagesize.get(image)
            if source_width > width:
                target_lg = target.with_stem(target.stem + f"-{width}")
                yield {
                    "name": target_lg,
                    "actions": [f"cwebp -resize {width} 0 -o {target_lg} {image}"],
                    "targets": [target_lg],
                    "file_dep": [image],
                }
