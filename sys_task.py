import sys

result = []
sorting = (True if "--sort" in sys.argv[1:] else False)
for arg in sys.argv[1:]:
    if arg == "--sort":
        continue
    else:
        result.append(f"Key: {arg.split('=')[0]} Value: {arg.split('=')[1]}")
if sorting:
    result = sorted(result)
for r in result:
    print(r)
