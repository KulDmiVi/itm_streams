def demo_work():
    file = open('lorum.txt', encoding='utf-8')
    print(file.read(3))
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    file.close()

    file= open('test1.txt', 'w',  encoding='utf-8')
    file.write('ТЕСТ1\n')
    file.write('ТЕСТ2\n')
    file.close()

    file = open('test1.txt', 'a+',  encoding='utf-8')
    file.write('ТЕСТ3\n')
    file.seek(0)
    for symbol in file.read():
        print(symbol)
    file.close()

    file = open('test1.txt', 'r+',  encoding='utf-8')
    print(file.readlines())
    file.write('ТЕСТ4\n')
    file.seek(0)
    print(file.readlines())
    file.close()


if __name__ == '__main__':
    demo_work()
