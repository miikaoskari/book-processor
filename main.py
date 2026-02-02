#!/usr/bin/env python3

import argparse
import shutil

from pathlib import Path


def get_covers(input_path: Path):
    picture_suffixes = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tif",
        ".tiff",
        ".webp",
        ".heic",
        ".heif",
    }

    pictures = []
    for path in input_path.rglob("*"):
        if (
            path.is_file()
            and path.suffix.lower() in picture_suffixes
            and "cover" not in path.name
        ):
            pictures.append(path)

    return pictures


def copy_as_cover(cover: Path):
    dest = cover.parent / f"cover{cover.suffix}"
    shutil.copyfile(cover, dest)


def main():
    parser = argparse.ArgumentParser(
        description="rename metadata pictures for plex as covers"
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
    )

    args = parser.parse_args()

    if not Path(args.input).resolve().is_dir():
        raise NotADirectoryError

    covers = get_covers(Path(args.input).resolve().absolute())

    for cover in covers:
        copy_as_cover(cover)


if __name__ == "__main__":
    main()
