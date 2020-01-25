import os
import tempfile
import shutil
import sys


def main():
    if "--help" in sys.argv:
        print("This tool will present you with an editable list of the files in the working directory."
              " Once you make your edits to those filenames, it will perform the move operations for you")
        exit(0)

    list_file = tempfile.NamedTemporaryFile('w+')

    # Populate the list file
    original_paths = []
    for folder, _, filenames in os.walk(os.path.abspath('.')):
        for filename in filenames:
            path = os.path.join(folder, filename)
            list_file.write(path + '\n')
            original_paths.append(path)

    # Open the list for editing by the user
    os.system(f"subl -w {list_file.name}")

    # Read the paths back out
    list_file.seek(0)
    new_paths = [
        path.strip()
        for path in list_file.read().split('\n')
        if path.strip() != ""
    ]

    if len(new_paths) != len(original_paths):
        print("Lines were deleted from the list file. This is not permitted")
        exit(1)

    changes = [
        (old, new)
        for old, new in zip(original_paths, new_paths)
        if old != new
    ]

    if len(changes) == 0:
        exit(0)

    # Confirm changes
    print("Going to move:")
    for old, new in changes:
        print(f"{old} → {new}")
    print("Continue? (y/n)")
    if input().lower() not in ["y", "yes"]:
        exit(0)

    for old, new in changes:
        shutil.move(old, new)


if __name__ == "__main__":
    main()