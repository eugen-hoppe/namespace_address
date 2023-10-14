import os
import shutil


def remove_pycache(directory):
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            if dir == "__pycache__":
                pycache_dir = os.path.join(root, dir)
                shutil.rmtree(pycache_dir)
                print(f"{pycache_dir} is deleted")



if __name__ == "__main__":
    remove_pycache("app")
    shutil.rmtree(".pytest_cache")
