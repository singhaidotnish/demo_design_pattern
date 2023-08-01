
def task_format():
    return {
        'actions': ['yapf -i --recursive src\\'],
        'doc': 'Formats code under src\\ using yapf'
    }

def task_format_check():
    return {
        'basename': 'format-check',
        'actions': ['yapf --diff --recursive src\\'],
        'doc': 'Checks code formatting for files under src\\ using yapf'
    }

def task_unit_test():
    return {
        'basename': 'unit-test',
        'actions': ['pytest -q tests\\'],
        'doc': 'Runs unit-test'
    }

def task_validate():
    return {
        'actions': ['echo Ok'],
        'task_dep': ['format-check', 'unit-test'],
        'doc': 'Validates this python package by checking formatting and unit-test'
    }

