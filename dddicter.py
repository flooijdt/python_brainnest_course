def dicter(dicts):
    for i in dicts:
        for k, v in i.items():
            try:
                if k == "a":
                    return v
            except KeyError:
                continue

dicts = [{"a": 1, "b": 2, "f": 6}, {"c": 1, "b": 2}, {"d": 1, "b": 2}]

print(dicter(dicts))
