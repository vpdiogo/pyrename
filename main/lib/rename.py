import os


__path__ = os.getcwd()


def rename_file(old_name, new_name, key=None):
    old_file = os.path.join(__path__, old_name)
    new_file = os.path.join(__path__, new_name)
    os.rename(old_file, new_file)
