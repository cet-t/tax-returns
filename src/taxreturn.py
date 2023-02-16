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


def tax_culc(_name: str, _sheet: int, _max: int):
    file = load_workbook(path)
    sheet = file[_sheet]
    sums = []
    for i in range(1, _max, 1):
        datas = sheet.cell(row=i, column=2).value
        sums.append(datas)
    print(f'{_name}: {sum(sums)}')

    file.close()


def all_tax() -> int:
    pass


if __name__ == '__main__':
    from openpyxl import *

    taxes: list[int] = []
    for i in range(4):
        tax_culc(names[i], sheets[i], max_row[i])
