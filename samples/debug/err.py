# err.py
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


def main2():
    try:
        bar('0')
    except Exception as e:
        print('error:', e)
    finally:
        print('finally...')


main2()
main()
