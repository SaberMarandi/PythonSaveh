# A0185 - جابجایی بیتی

n = int(input())
direction = input().strip()
shift = int(input())

if direction == 'L':
    result = n << shift
else:  # direction == 'R'
    result = n >> shift

print(result)
