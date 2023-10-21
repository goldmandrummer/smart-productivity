import subprocess

class TagManager:
    def __init__(self):
        pass

    def add_tag(self, tag: str):
        subprocess.run(['tag', '-a', tag])

    def remove_tag(self, tag: str):
        subprocess.run(['tag', '-r', tag])

    def update_tag(self, old_tag: str, new_tag: str):
        subprocess.run(['tag', '-r', old_tag])
        subprocess.run(['tag', '-a', new_tag])