def parseLine(str):
    # str = "Adobe Photoshop 2021 v22.5.1.441中文注册激活版 链接: https://pan.baidu.com/s/1gRFJlQacdTo-YC_7zYVDxg  usyg              "
    # 删除末尾的空格
    str  = str.rstrip()
    indexStart = str.find("https")
    if(indexStart ==-1):
        return;
    indexEnd = str.find(" ", indexStart);
    url = str[indexStart:indexEnd]

    if(len(str) -4 <= indexEnd):
        scert = ""
    else:
        scert = str[len(str) -4:]

    print("-------");
    print("url: ", url);
    print("scert: ", scert);

if __name__ == '__main__':

    f = open("list.txt",encoding='utf-8')
    while True:
        line = f.readline()
        if line:
            parseLine(line);
        else:
            break
    f.close()
    print("ok")
    