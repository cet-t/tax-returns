sheets = [
    'hiroko_med',
    'hiroko_nur',
    'takashi_med',
    'takashi_nur'
]

max_row = {
    'hm': 30,
    'hn': 39,
    'tm': 64,
    'tn': 75
}

h = 'hiroko'
t = 'takashi'

path = './tax_return2.xlsx'


def tax_culc(_name: str, _sheet: int, _max: int):
    file = openpyxl.load_workbook(path)
    sheet = file[_sheet]
    sums = []
    c: int
    for i in range(1, _max, 1):
        datas = sheet.cell(row=i, column=2).value
        sums.append(datas)
        c += i
    file.close()

    print(f'{_name}: {sum(sums)}({c})')


if __name__ == "__main__":
    import openpyxl

    tax_culc(h, sheets[0], max_row['hm'])
    tax_culc(h, sheets[1], max_row['hn'])
    tax_culc(t, sheets[2], max_row['tm'])
    tax_culc(t, sheets[3], max_row['tn'])
