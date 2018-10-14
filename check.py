class news():
    """__init__() functions as the class constructor"""
    def __init__(self, fact=None, link=None):
        self.fact = fact
        self.link = link


data = []


def readFile(path):
    global data
    temp = news()
    file = open(path, 'r')
    a = file.readlines()
    b = []
    for i in range(len(a)):
        b.append(a[i])
    for i in range(len(a)):

        a[i] = a[i][2:].rstrip('\n')
        b[i] = b[i][0]
        temp.link = a[i]
        temp.fact = b[i]
        data.append(news(b[i], a[i]))
    for i in range(len(data)):
        print(data[i].link)


def check(link, data1):
    # print(data1.link)
    if link == data1.link:
        # import pdb; pdb.set_trace()
        if data1.fact == '1':
            return 1
        elif data1.fact == '0':
            return 0
    else:
        return -1


def usercheck(link):
    global data
    for i in range(len(data)):
        # import pdb; pdb.set_trace()
        if check(link, data[i]) == 1:
            return 1
        elif check(link, data[i]) == 0:
            return 0
    return -1


def user_define(type, link):
    global data
    data.append(news(type, link))
    f = open("a", "a")
    for i in range(len(data)):
        f.write(data[i].fact + " " + data[i].link + '\n')
