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


def tax_culc(_name: str, _sheet: int, _max: int) -> None:
    file = load_workbook(path)
    sheet = file[_sheet]
    sums = []
    for i in range(1, _max, 1):
        datas = sheet.cell(i, 2).value
        sums.append(datas)
    print(f'{_name}: {sum(sums)}')

    file.close()


def tax_sum(_sheet: int, _max: int) -> int:
    file = load_workbook(path)
    sheet = file[_sheet]
    sums = []
    for i in range(1, _max, 1):
        datas = sheet.cell(i, 2).value
        sums.append(datas)
    return sum(sums)

    file.close()


if __name__ == '__main__':
    from openpyxl import *

    taxes: list[int] = []
    for i in range(4):
        tax_culc(names[i], sheets[i], max_row[i])
    sums: dict[str, int]
    sums = tax_sum(sheets[0], max_row[0])
    sums = tax_sum(sheets[1], max_row[1])
    sums = tax_sum(sheets[2], max_row[2])
    sums = tax_sum(sheets[3], max_row[3])
