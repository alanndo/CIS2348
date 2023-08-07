# 2133915
# Alan Do

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    finally:
        print('{} {}'.format(name, age))
        parts = input().split()
        name = parts[0]