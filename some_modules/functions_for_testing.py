import separator


def get_formatted_name(first_name, last_name, second_name=None):
    """ Возвращает форматированное полное имя """
    _second_name = f' {second_name.title()} ' if second_name else ' '
    full_name = f'{first_name.title()}{_second_name}{last_name.title()}'

    return full_name
