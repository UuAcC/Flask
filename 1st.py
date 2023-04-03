import sys

in_data = list(sys.stdin)
source = list(in_data[0])
res = []
for line in in_data[1:]:
    pre_res = []
    count = 0
    line = line.strip()
    for char in line:
        if char in source:
            if count == 0:
                if char == line[-1]:
                    continue
                else:
                    count = 1
            else:
                count += 1
                if count != len(line):
                    pre_res.append(count)
                count = 1
                continue
        else:
            if count == 0:
                continue
            else:
                if char == line[-1]:
                    count = 0
                else:
                    count += 1
    try:
        res.append(min(pre_res))
    except ValueError:
        pass
print(', '.join(sorted(list(set([str(x) for x in res])))))
