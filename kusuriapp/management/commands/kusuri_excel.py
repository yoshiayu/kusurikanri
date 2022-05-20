from django.core.management.base import BaseCommand
import openpyxl
import os
from pathlib import Path
from kusuriapp.models import CompanyMedicineName
import pandas as pd

df = pd.read_excel('All.xlsx')
del_list = df.loc[:, 'cell.value'].drop_duplicates(
    keep='last').dropna().to_list()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for folder, subFolder, files in os.walk('static'):
            for file in files:
                if file.endswith('.xlsx'):
                    wb = openpyxl.load_workbook(f'{folder}/{file}')
                    for sheet_name in wb.sheetnames:  # シートでループ
                        ws = wb[sheet_name]
                        # 一行目はヘッダーなのでスキップし、行でループ
                        for row in ws.iter_rows(min_row=2):
                            # print(sheet_name)

                            medicine = CompanyMedicineName()

                            medicine.initials = str(
                                Path(f'{folder}/{file}').parent).split('/')[-1][0]
                            medicine.company_name = sheet_name
                            # print(str(Path(f'{folder}/{file}').parent).split('/')[-1][0])
                            # print(str(Path(f'{folder}/{file}').parent).split('/')[-1][0])

                            for cell in row:  # セルでループ
                                # print(f'row: {cell.row}, column: {cell.column}, value: {cell.value}')
                                if cell.column == 2:
                                    medicine.medicine_name = cell.value

                            cell.value = []

                            for i in range(1, ws.max_row):
                                if ws.cell(i, 1).value != ws.cell(i-1, 1).value:
                                    medicine.medicine_name.append(
                                        ws.cell(i, 1).value)
                                cell.value = list(filter(None))

                            # print(cell.value)

                            medicine.save()

                            #medicine = [cell.value]
                            #medicine_k = []
                            # for i in medicine:
                            #    if i not in medicine_k:
                            #        medicine_k.append(i)

                            #cell.value = []

                            # for Q in range(ws.max_row + 1):
                            #    if Q == 0:
                            #        continue
                            #list = ws.cell(i, 1).value
                            #list_Num = Q

                            # for i in reversed(range(ws.max_row + 1)):
                            #    if i == 0:
                            #        break
                            #    if ws.cell(i, 1).value == list:
                            #        if i == Q:
                            #            continue
                            #    else:
                            #        ws.delete_row(i)
                            # wb.save(medicine.medicine_name)
