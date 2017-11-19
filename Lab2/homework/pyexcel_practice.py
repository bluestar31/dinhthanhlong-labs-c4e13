import pyexcel as p

a_list_of_dictionaries = [
    {
        "Name": 'Adam',
        "Age": 28
    },
    {
        "Name": 'Beatrice',
        "Age": 29
    },
    {
        "Name": 'Ceri',
        "Age": 30
    },
    {
        "Name": 'Dean',
        "Age": 26
    }
]

p.save_as(records = a_list_of_dictionaries, dest_file_name = "pyexcel_practice.xls")

records = p.iget_records(file_name = "pyexcel_practice.xls")
for record in records:
    print("{0} is aged at {1}".format(record['Name'], record['Age']))
