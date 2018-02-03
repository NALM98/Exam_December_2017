import urllib.request
import re
from pymystem3 import Mystem
import json

#1
def parsing():
    address = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
    with urllib.request.urlopen(address) as task_file:
        html = task_file.read().decode('utf-8')
    reg_tag = re.compile('<.*?>', re.DOTALL)
    reg_script = re.compile('<script>.*?</script>', re.DOTALL)
    reg_comment = re.compile('<!--.*?-->', re.DOTALL)

    text = reg_tag.sub("", html)
    text = reg_script.sub("", text)
    text = reg_comment.sub("", text)

    text = text.replace('&nbsp;', ' ')
    text = text.replace('&rarr;', ' ') 

    small_let = re.compile('\s(с[а-я]*?)\s')
    big_big_let = re.compile('(С[А-Я]*?)\s')
    big_small_let = re.compile('(С[а-я]*?)\s')

    arr = re.findall(small_let, text) + re.findall(big_big_let, text) + re.findall(big_small_let, text)

    return arr
#2

def analyzer():
    source = set()
    part = parsing()
    for elem in part:
        source.add(elem.lower())
    mystem = Mystem()
    for item in source:
        result = mystem.analyze(item)
        info = result[0]
        verb = info['analysis']
        line = json.dumps(verb)
        if 'V' in line:
            print(item)

        
analyzer()
