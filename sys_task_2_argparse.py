import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("file")
args = parser.parse_args()
result = []
try:
    with open(''.join(args.file), 'r') as file:
        for line in file.readlines():
            result.append(line.strip())
    if args.sort:
        result = sorted(result)
    if args.num:
        for num, line in enumerate(result):
            print(f'{num} {line}')
    else:
        for line in result:
            print(line)
    if args.count:
        print(f'rows count: {len(result)}')
except Exception:
    print('ERROR')
