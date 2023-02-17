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


def tax_culc(_name: str, _sheet: int, _max: int) -> None:
    file = openpyxl.load_workbook(path)
    sheet = file[_sheet]
    sums = []
    for i in range(1, _max, 1):
        datas = sheet.cell(i, 2).value
        sums.append(datas)
    print(f'{_name}: {sum(sums)}')

    file.close()


def tax_sum(_sheet: int, _max: int) -> int:
    file = openpyxl.load_workbook(path)
    sheet = file[_sheet]
    sums = []
    for i in range(1, _max, 1):
        datas = sheet.cell(i, 2).value
        sums.append(datas)
    file.close()
    return sum(sums)


sums: list[int]
sums = [
    tax_sum(sheets[0], max_row[0]),
    tax_sum(sheets[1], max_row[1]),
    tax_sum(sheets[2], max_row[2]),
    tax_sum(sheets[3], max_row[3]),
]
all_: int = 0
alls = [
    sums[0],  # 医1
    sums[1],  # 介1
    sums[2],  # 医2
    sums[3],  # 介2
    sums[0]+sums[2],  # 医合計
    sums[1]+sums[3],  # 介合計
    sums[0]+sums[1],  # 合計1
    sums[2]+sums[3],  # 合計2
    sum(sums),
]

if __name__ == '__main__':
    import openpyxl

    path = 'data/tax_return2.xlsx'
    # for i in range(len(sums)):
    # print(sums[i])
