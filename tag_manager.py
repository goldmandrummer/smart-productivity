import os
import subprocess
from functools import reduce

class TagManager:
    # The built-in tags are defined here just in case.
    NONE = 'None'
    GRAY = 'Gray'
    GREEN = 'Green'
    PURPLE = 'Purple'
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    RED = 'Red'
    ORANGE = 'Orange'
    COLORS = {
        NONE: 'None',
        GRAY: 'Gray',
        GREEN: 'Green',
        PURPLE: 'Purple',
        BLUE: 'Blue',
        YELLOW: 'Yellow',
        RED: 'Red',
        ORANGE: 'Orange',
    }

    def __init__(self):
        pass

    def add_tags(self, path: str, tags: str):
        return str(subprocess.run(['tag', '-a', tags, path], capture_output=True).stdout.decode())

    def remove_tags(self, path: str, tags: str):
        return str(subprocess.run(['tag', '-r', tags, path], capture_output=True).stdout.decode())

    def update_tags(self, path: str, old_tags: str, new_tags: str):
        subprocess.run(['tag', '-r', old_tags, path], capture_output=True)
        return str(subprocess.run(['tag', '-a', new_tags, path], capture_output=True).stdout.decode())

    def full_tags_print(self, path: str, color=True):
        return str(subprocess.run(['tag', '-lc' if color else '-l', path], capture_output=True).stdout.decode())

    def full_system_tags_print(self, color=True):
        path = os.environ.get('SYSTEM_USER_PATH', '/Users/$(whoami)/')
        path = str(subprocess.run(['realpath', path], capture_output=True).stdout.decode()) # evaluate $(whoami) and other variables
        result = str(subprocess.run(['tag', '-lRc' if color else '-lR', path], capture_output=True).stdout.decode())
        return result

    def print_tags(self, path: str, color=True):
        tab_split = self.full_tags_print(path, color).rsplit('\n', 1)[0].rsplit('\t', 1)
        if len(tab_split) < 2:
            return ''
        return tab_split[1]

    def print_system_tags(self, color=False):
        line_split = self.full_system_tags_print(color).rsplit('\n')[:-1]
        color_split = [line.rsplit('\t', 1)[1] for line in line_split if '\t' in line]
        return ','.join(color_split)