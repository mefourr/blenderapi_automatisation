import bpy
import os
import logging

DEFAULT_DIR = "G:\\Детали"


def make_new_path(*, filename: str) -> str:
    return os.path.join("G:\\Detail", filename)


def file_exists(*, filename: str) -> bool:
    try:
        for file in os.listdir(DEFAULT_DIR):
            if filename == file:
                return True
        return False
    except FileNotFoundError:
        logging.exception("Directory not found: %s", DEFAULT_DIR)
        exit()


def parse_blend(*, file_path: str) -> None:
    bpy.ops.wm.open_mainfile(filepath=file_path)
    parse_objects()
    # bpy.ops.wm.save_mainfile()
    bpy.ops.wm.quit_blender()


def parse_objects() -> None:
    for object in bpy.data.libraries:
        if "World" in object.name:
            continue

        filename = os.path.basename(object.filepath)

        if not filename:
            logging.exception("file name for object doesn't exist")
            return None

        if not object.filepath:
            logging.exception("file path for object doesn't exist")
            return None

        current_path: str = object.filepath

        if "G:\\Detail" not in current_path:
            if file_exists(filename=filename):
                current_path = make_new_path(filename=filename)
                object.filepath = current_path

        print(object.filepath)


def main() -> None:
    current_dir: str = "blends"  # os.getcwd()
    blend_ex: str = ".blend"

    try:
        blend_files = [
            file for file in os.listdir(current_dir) if file.endswith(blend_ex)
        ]

        if len(blend_files) == 0:
            raise ValueError("blend files equal zero")
    except ValueError as e:
        exit(str(e))

    for blend_file in blend_files:
        file_path = os.path.join(current_dir, blend_file)
        parse_blend(file_path=file_path)


if __name__ == "__main__":
    main()

# -Y, --disable-autoexec
# Disable automatic Python script execution (pydrivers & startup scripts), (default).

# --python-console
# Run Blender with an interactive console.
