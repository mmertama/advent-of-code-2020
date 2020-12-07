import functools

example = '''abc

a
b
c

ab
ac

a
a
a
a

b'''


def check_custom_declaration_forms_any(data):
    records = []
    current_record = set()
    for line in data:
        if len(line) == 0:
            records.append(current_record)
            current_record = set()
        else:
            for v in line:
                current_record.add(v)
    records.append(current_record)
    value = functools.reduce(lambda acc, s: acc + len(s), records, 0)
    print("records", value)


def check_custom_declaration_forms_all(data):
    records = []
    current_record = None
    for line in data:
        if len(line) == 0:
            records.append(current_record)
            current_record = None
        elif current_record is None:
            current_record = set([x for x in line])
        else:
            current_record.intersection_update(line)

    records.append(current_record)
    value = functools.reduce(lambda acc, s: acc + len(s), records, 0)
    print("records", value)

