from multiprocessing.reduction import duplicate
from django.core.management.base import BaseCommand
from numpy import iterable
import openpyxl
import os
from pathlib import Path
from kusuriapp.models import CompanyMedicineName
import pandas as pd


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # def __inter__(file):

        for folder, subFolder, files in os.walk('static'):
            for file in files:
                if file.endswith('.xlsx'):
                    wb = openpyxl.load_workbook(f'{folder}/{file}')

                    for sheet_name in wb.sheetnames:  # シートでループ
                        ws = wb[sheet_name]

                        # 一行目はヘッダーなのでスキップし、行でループ
                        for row in ws.iter_rows(min_row=2):
                            print(sheet_name)
                            medicine = CompanyMedicineName()
                            medicine.initials = str(
                                Path(f'{folder}/{file}').parent).split('/')[-1][0]
                            medicine.company_name = sheet_name

                       # print(str(Path(f'{folder}/{file}').parent).split('/')[-1][0])
                       # print(str(Path(f'{folder}/{file}').parent).split('/')[-1][0])

                            for cell in row:  # セルでループ
                                medicine = [cell.value]
                                medicine_k = []
                                for i in medicine:
                                    if i not in medicine_k:
                                        medicine_k.append(i)

                                print(
                                    f'row: {cell.row}, column: {cell.column}, value: {cell.value}')

                                if cell.column == 2:

                                    medicine.medicine_name = cell.value

                                print(cell.value)

                                medicine.save()

                            # 以下ゴミ
                            #cell.value = []
                            # for i in range(1, ws.max_row):
                            #    if ws.cell(i, 1).value != ws.cell(i-1, 1).value:
                            #        cell.value.append(
                            #            ws.cell(i, 1).value)
                            #        cell.value = list(
                            #            filter(None, medicine.medicine_name))

                                #uniqued = []
                                # for x in cell:
                                #    if not x in uniqued:
                                #        uniqued.append(x)

                                #duplicated = [cell]
                                # print(duplicated)

                                #uniqued = set(duplicated)
                                # print(uniqued)

                            # medicine.save()

                            #cell.value = []

                            #    for Q in range(ws.max_row + 1):
                            #        if Q == 0:
                            #            continue

                            #        list = ws.cell(Q, 1).value

                            #        list_Num = Q

                            #        for i in reversed(range(ws.max_row + 1)):
                            #            if i == 0:
                            #                break

                            #            if i == Q:
                            #                continue
                            #            else:
                            #                ws.delete_rows(i)
                            #    wb.save(f'{folder}/{file}/1')

                            #df = pd.read_excel(".xlsx")
                            # del_list = df.loc[:, cell.value].drop_duplicates(
                            # keep='last').dropna().to_list()
