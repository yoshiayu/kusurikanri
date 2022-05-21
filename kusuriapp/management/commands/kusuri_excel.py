from django.core.management.base import BaseCommand
import openpyxl
import os
from pathlib import Path
from kusuriapp.models import CompanyMedicineName


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        medicine_object_list = []
        medicine_name_list = []

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
                            # print(cell.value)

                            # medicine.save()
                            # 重複していないリストを作成

                            if medicine.medicine_name not in medicine_name_list:
                                medicine_object_list.append(medicine)
                                medicine_name_list.append(
                                    medicine.medicine_name)

                            # medicine.save()

                        # ここで保存
                        # for medicine in medicinename_list:

        CompanyMedicineName.objects.bulk_create(
            medicine_object_list)

        # medicine.save()
