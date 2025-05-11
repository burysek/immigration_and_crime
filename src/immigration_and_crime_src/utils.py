from pathlib import Path

def get_project_root():
    '''Returns the project root directory, i.e., immigration_and_crime/, irrespective of where in the file system you are'''
    cwd = Path.cwd()
    if cwd.name == 'notebooks':
        root = cwd.parent
    elif cwd.name == 'immigration_and_crime':
        root = cwd
    elif cwd.name == 'data':
        root = cwd.parent
    elif cwd.name == 'external':
        root = cwd.parent.parent
    else:
        print("Unable to locate the 'immigration_and_crime/' directory. " \
        "Navigate into this directory and execute the notebook from there, or any of its subdirectory")

    return root