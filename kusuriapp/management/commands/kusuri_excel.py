from django.core.management.base import BaseCommand
import openpyxl
import os

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for folder, subFolder, files in os.walk('static'):
            for file in files:
                if file.endswith('.xlsx'):
                    wb = openpyxl.load_workbook(f'{folder}/{file}')
                    for sheet_name in wb.sheetnames:  # シートでループ
                        ws = wb[sheet_name]
                        for row in ws.iter_rows(min_row=2):  # 一行目はヘッダーなのでスキップし、行でループ
                            for cell in row:  # セルでループ
                                print(f'row: {cell.row}, column: {cell.column}, value: {cell.value}')