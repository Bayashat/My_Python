import re
import csv

file = open("raw.txt", 'r', encoding='utf-8')
all_lines = file.read()

Company_Name = re.search(r'ДУБЛИКАТ\n(?P<Name>.+)\n', all_lines).group("Name")  # Филиал ТОО EUROPHARMA Астана
print(Company_Name)

Bin_Number = re.search(r'БИН (?P<Bin>\d+)', all_lines).group("Bin")     # 080841000761

Items = re.compile(r'(?P<index>\d+\.)\n(?P<name>[^\n]+)\n(?P<count>[0-9, ]+) x (?P<price>[0-9, ]+)\n(?P<total>[0-9, ]+)')

for match in re.finditer(Items, all_lines):
    print(match.group('index') + " " + match.group('name') + " " + match.group('count') + " " + match.group("price") + " " + match.group("total"))

List = [["Company_Name", "Bin_Number", "Title", "Count", "Price", "Total", "Date", "Address"]]

for match in re.finditer(Items, all_lines):
    List.append([Company_Name, Bin_Number, match.group('name'), match.group('count'), match.group("price"), match.group("total")])

############   CSV (Comma Seperated Value):

with open("file.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(List)
