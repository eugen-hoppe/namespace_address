import os
import shutil


PYTEST_CACHE = ".pytest_cache"
APP_PATH = "app"


def remove_pycache(directory):
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            if dir == "__pycache__":
                pycache_dir = os.path.join(root, dir)
                shutil.rmtree(pycache_dir)
                print(f"{pycache_dir} is deleted")


if __name__ == "__main__":
    remove_pycache(APP_PATH)
    if os.path.exists(PYTEST_CACHE):
        shutil.rmtree(PYTEST_CACHE)
