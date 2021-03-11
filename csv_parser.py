import wx
import csv


CSV_COLUMN_LEVEL = 0
CSV_COLUMN_SP = 1
CSV_COLUMN_INDEX = 2
CSV_COLUMN_TIMESTAMP = 3
CSV_COLUMN_DUR = 4
CSV_COLUMN_LEN = 5
CSV_COLUMN_ERR = 6
CSV_COLUMN_DEV = 7
CSV_COLUMN_EP = 8
CSV_COLUMN_RECORD = 9
CSV_COLUMN_DATA = 10
CSV_COLUMN_SUMMARY = 11
CSV_COLUMN_ASCII = 12


def get_raw_datas(filename):
	print('get_rawdatas: path= ' + filename)
	
	with open(filename, 'r') as file_object:
		reader = csv.reader(file_object)
		
		raw_datas = []
		column_header_found = False
		for row in reader:
			if row[0].find('Level') >= 0:
				column_header_found = True
				print(row)
		
			if column_header_found:
				item = {}
				item['timestamp'] = row[CSV_COLUMN_TIMESTAMP]
				item['len'] = row[CSV_COLUMN_LEN][0:-2]
				item['dev'] = row[CSV_COLUMN_DEV]
				item['ep'] = row[CSV_COLUMN_EP]
				item['record'] = row[CSV_COLUMN_RECORD]
				item['data'] = row[CSV_COLUMN_DATA]
				item['ascii'] = row[CSV_COLUMN_ASCII]
				
				if item['record'].startswith('OUT txn') and item['record'].find('NAK') < 0:
					item['direction'] = 'out'
					raw_datas.append(item)
					#print(item)
				elif item['record'].startswith('IN txn') and item['record'].find('NAK') < 0:
					item['direction'] = 'in'
					raw_datas.append(item)
					#print(item)
				elif item['record'].find('connected') >= 0:
					item['prompt'] = True
					raw_datas.append(item)
					print(item)
						
	return raw_datas

