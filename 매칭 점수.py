import re
from collections import defaultdict


def solution(word, pages):
    word = word.lower()
    linked_state = defaultdict(list)

    url_regex = re.compile('content="https://([^"]*)', re.IGNORECASE)
    link_regex = re.compile('href="https://([^"]*)', re.IGNORECASE)

    graph = defaultdict(list)
    for index,page in enumerate(pages):
        lines = page.split('<') # 이 부분을 header부분과 body부분으로 나눠서 하면 더 깔끔하고 빠르게 처리가능할듯.
        url = ''
        for line in lines:
            url_result = url_regex.findall(line)
            if len(url_result) > 0:
                url = url_result[0]
                if url not in linked_state:
                    linked_state[url].extend([index,0,0,0])
                continue

            link_result = link_regex.findall(line)
            if len(link_result) > 0:
                link = link_result[0]
                graph[link].append(url)
                linked_state[url][2] += 1
                continue

            if len(url) > 0:
                linked_state[url][1] += re.sub('[^a-zA-Z]', ' ', line.lower()).split().count(word)

    result = [0] * (index+1)
    for state in linked_state.keys():
        sum = 0
        for linked_me in graph[state]:
            if linked_me in linked_state.keys():
                sum += linked_state[linked_me][1] / linked_state[linked_me][2]  # 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수
        result[linked_state[state][0]] = linked_state[state][1] + sum

    return result.index(max(result))

# solution("Muzi", [
#     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
#     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
