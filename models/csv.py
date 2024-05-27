import io
import csv

class dCsv():
    def dataToCsv(self,fields,data):
        output=io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
        output.seek(0)
        file=io.BytesIO()
        file.write(output.getvalue().encode('utf-8'))
        file.seek(0)
        return file
