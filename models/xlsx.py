import csv
import io
from xlsxwriter.workbook import Workbook
class dXlsx():
    def csvToXlsx(self,file):
        input=file.read().decode('utf-8')
        output=io.BytesIO()
        workbook = Workbook(output)
        worksheet = workbook.add_worksheet()
        reader = csv.reader(io.StringIO(input))
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)

        workbook.close()
        output.seek(0)
        return output
    