def auto_sum(_sum) -> int:
    ret: int = sum(_sum)
    return ret


def mn(_med, _nur, _name) -> None:
    hm = auto_sum(_med)
    hn = auto_sum(_nur)
    print(f'{_name}: {hm}')
    print(f'{_name}: {hn}')
    print(f'sum: {hm+hn}')


if __name__ == "__main__":
    import datas
    import sys
    import openpyxl

    sys.path.append("./hiro.py")
    sys.path.append("./taka.py")

    # mn(datas.hiro_med, datas.hiro_nur, "hiroko")
    # mn(datas.taka_med, datas.taka_nur, "takashi")

    wb = openpyxl.load_workbook('./tax_return.xlsx')
    sheet = wb['hiroko_med']
    v = sheet.cell(row=1, column=1).value
    wb.close()
    print(v)
