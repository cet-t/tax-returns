sheets = [
    'hiroko_med',
    'hiroko_nur',
    'takashi_med',
    'takashi_nur'
]

max_row = [
    30,
    39,
    64,
    75
]

names = [
    'hiroko-med',
    'hiroko-nur',
    'takashi-med',
    'takashi-nur'
]

path = 'data/tax_return2.xlsx'

datas: int


class AA:
    def __init__(self, _name: str, _sheet: int, _max: int):
        file = load_workbook(path)
        sheet = file[_sheet]
        sums = []
        for i in range(1, _max, 1):
            datas = sheet.cell(row=i, column=2).value
            sums.append(datas)
        print(f'{_name}: {sum(sums)}')

        file.close()


def get_all() -> int:
    taxes: list[int] = []

    return 0


if __name__ == '__main__':
    from openpyxl import *

    for i in range(4):
        AA(names[i], sheets[i], max_row[i])
