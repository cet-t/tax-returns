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

titles = [
    'hiroko medical',
    'hiroko nursing',
    'takashi medical',
    'takashi nursing',
    'nursing',
]

path = 'data/tax_return2.xlsx'


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

    sums: list[int]
    sums = [
        tax_sum(sheets[0], max_row[0]),
        tax_sum(sheets[1], max_row[1]),
        tax_sum(sheets[2], max_row[2]),
        tax_sum(sheets[3], max_row[3]),
    ]
    alls = [
        sums[0],
    ]

    for i in range(len(sums)):
        print(sums[i])
