import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Chatbot copy').sheet1
#selection = sheet.getDataRange()
pp = pprint.PrettyPrinter()
orderid ='#7221'
cell = sheet.find(orderid)
row = cell.row
pp.pprint(row)
pp.pprint(sheet.cell(row,9).value)