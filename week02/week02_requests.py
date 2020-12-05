import requests
from lxml import etree


def getAnswer(myURL, header):
    re = requests.get(myURL, headers=header)
    selector = etree.HTML(re.text())
    answer = '//*[@id="root"]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div[1]/span'

    answer_chunk = selector.xpath(answer)

    return answer_chunk, re.status_code


def wriFile(filename,answerList):
    with open(filename, "w+") as r:
        for line in answerList:
            r.write(line)


if __name__ == '__main__':
    targetURL = "https://www.zhihu.com/question/60031957/answer/1589729360"  

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    answer, repsStatus = getAnswer(targetURL, header)

    if repsStatus != 200:
        pass

    wriFile("answer.results",answerList=answer)