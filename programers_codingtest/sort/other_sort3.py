def solution1(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

def solution3(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i:
      return i
  return len(sorted_citations)


def solution(citations):
    citations.sort()
    n, answer = len(citations), 0
    for i, cites in enumerate(citations):
        h = n - i
        if cites >= h:
            return h
    return

def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for c in citations:
        if c > h_index:
            h_index += 1
    return h_index

citations = [3,0,6,1,5]
solution(citations)
