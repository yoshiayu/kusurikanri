from multiprocessing.reduction import duplicate
from django.core.management.base import BaseCommand
from numpy import iterable
import openpyxl
import os
from pathlib import Path
from kusuriapp.models import CompanyMedicineName


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for folder, subFolder, files in os.walk('static'):
            for file in files:
                if file.endswith('.xlsx'):
                    wb = openpyxl.load_workbook(f'{folder}/{file}')
                    for sheet_name in wb.sheetnames:  # シートでループ
                        ws = wb[sheet_name]

                # def __inter__(iterable):
                    uniqued = []
                    for x in duplicated:
                        if not x in uniqued:
                            uniqued.append(x)

                            duplicated = [CompanyMedicineName]
                            print(duplicated)

                            uniqued = set(duplicated)
                            print(uniqued)
                            # 一行目はヘッダーなのでスキップし、行でループ
                            for row in ws.iter_rows(min_row=2):
                                print(sheet_name)
                            medicine = CompanyMedicineName()
                            medicine.initials = str(
                                Path(f'{folder}/{file}').parent).split('/')[-1][0]
                            medicine.company_name = sheet_name

                            medicine = [CompanyMedicineName]
                            medicine_k = []
                            for i in medicine:
                                if i not in medicine_k:
                                    medicine_k.append(i)
                       # print(str(Path(f'{folder}/{file}').parent).split('/')[-1][0])
                       # print(str(Path(f'{folder}/{file}').parent).split('/')[-1][0])
                            for cell in row:  # セルでループ
                                print(
                                    f'row: {cell.row}, column: {cell.column}, value: {cell.value}')
                                if cell.column == 2:
                                    medicine.medicine_name = cell.value
                                print(cell.value)
                            medicine.save()
