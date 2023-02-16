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

h = 'hiroko'
t = 'takashi'
path = './tax_return2.xlsx'


def tax_culc(_name: str, _sheet: int, _max: int):
    file = openpyxl.load_workbook(path)
    sheet = file[_sheet]
    sums = []
    for i in range(1, _max, 1):
        datas = sheet.cell(row=i, column=2).value
        sums.append(datas)
    print(f'{_name}: {sum(sums)}')

    file.close()


if __name__ == "__main__":
    import openpyxl

    for i in range(2, 4, 1):
        tax_culc(t, sheets[i], max_row[i])

    for i in range(2):
        tax_culc(h, sheets[i], max_row[i])
