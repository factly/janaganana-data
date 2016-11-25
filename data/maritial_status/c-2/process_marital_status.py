import sys
import glob
import xlrd
import unicodecsv as csv

all_files = glob.glob('*.xls')

for xls_file in all_files:
    csv_file = './csv/' + xls_file.split(".")[0] + '.csv';
    with xlrd.open_workbook(xls_file) as wb:
        sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
        print "writing " + csv_file + " ...";
        with open(csv_file, 'wb') as f:
            c = csv.writer(f, dialect='excel', encoding='utf-8');
            for r in range(sh.nrows):
                c.writerow(sh.row_values(r));


