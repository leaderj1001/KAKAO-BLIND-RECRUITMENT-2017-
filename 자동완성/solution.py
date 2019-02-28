class Node(object):
    def __init__(self, key, value, count, data=None):
        """
        struct Node를 정의한다.
        :param key: char value, example) 'a', 'b', ...
        :param value: head 노드 다음 부터 지금 key까지 오는데 몇 번을 거쳐왔는가?
        :param count: 같은 key가 몇 번이나 나왔는가?
        :param data: key 값이 각 단어의 마지막 char라면 전체 word를 넣어주고, 아니라면 None을 넣어준다.
        """
        self.key = key
        self.value = value
        self.count = count
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(key=None, value=0, count=0)

    def insert(self, string):

        # self.head는 처음을 나타내는 dummy node이다.
        current_node = self.head

        value = 0
        for char in string:
            value += 1

            # char를 가진 자식이 없다면, 노드를 만들어 생성해준다.
            if char not in current_node.children:
                current_node.children[char] = Node(key=char, value=value, count=1)
            # value, 몇 번째 위치한 Node인지 알려준다.
            # count, 현재 char가 몇 번이나 나왔는지 알려준다.
            else:
                current_node.children[char].value = value
                current_node.children[char].count += 1

            # 노드 이동
            current_node = current_node.children[char]

        current_node.data = string

    def starts_with(self):
        current_node = self.head
        answer = 0

        queue = list(current_node.children.values())
        while queue:
            curr = queue.pop()
            if curr.data != None:
                answer += curr.value
                queue += list(curr.children.values())
            elif curr.data == None and curr.count == 1:
                answer += curr.value
            else:
                queue += list(curr.children.values())

        return answer


def solution(words):
    answer = 0

    t = Trie()
    for word in words:
        t.insert(word)

    list1 = []
    for word in words:
        if word[0] not in list1:
            list1.append(word[0])

    answer += t.starts_with()

    return answer