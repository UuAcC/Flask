import sys

count = (True if "--count" in sys.argv[1:] else False)
num = (True if "--num" in sys.argv[1:] else False)
sort = (True if "--sort" in sys.argv[1:] else False)
filename = sys.argv[1:]
if count:
    filename.remove("--count")
if num:
    filename.remove("--num")
if sort:
    filename.remove("--sort")
result = []
try:
    with open(''.join(filename), 'r') as file:
        for line in file.readlines():
            result.append(line.strip())
    if sort:
        result = sorted(result)
    if num:
        for number, line in enumerate(result):
            print(f'{number} {line}')
    else:
        for line in result:
            print(line)
    if count:
        print(f'rows count: {len(result)}')

except Exception:
    print('ERROR')