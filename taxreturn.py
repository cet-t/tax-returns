class defs:
    def auto_sum(_sum) -> int:
        ret: int = sum(_sum)
        return ret

    def mn(_med, _nur, _name) -> None:
        hm = defs.auto_sum(_med)
        hn = defs.auto_sum(_nur)
        print(f'{_name}: {hm}')
        print(f'{_name}: {hn}')
        print(f'sum: {hm+hn}')


if __name__ == "__main__":
    import openpyxl
    import datas

    # defs.mn(datas.hiro_med, datas.hiro_nur, "hiroko")
    # defs.mn(datas.taka_med, datas.taka_nur, "takashi")

    sheets = [
        'hiroko_med',
        'hiroko_nur',
        'takashi_med',
        'takashi_nur'
    ]

    file = openpyxl.load_workbook('./tax_return2.xlsx')
    sheet = file[sheets[0]]
    v = sheet.cell(row=1, column=1).value
    print(v)
    file.close()
