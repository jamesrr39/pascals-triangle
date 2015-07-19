__author__ = 'james'


def get_next_row(current_row):
    new_row = [1]
    for index, number in enumerate(current_row):
        if index is not 0:
            new_row.append(number + current_row[index -1])
    new_row.append(1)
    return new_row
