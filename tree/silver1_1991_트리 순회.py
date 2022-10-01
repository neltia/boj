"""
이진 검색 트리(BST, Binary Search Tree)
트리vs그래프: 트리는 순환 구조를 갖지 않는 그래프

전위 순회(preorder):   루트-왼쪽-오른쪽
중위 순회(inorder):    왼쪽-루트-오른쪽
후위 순회(postorder):  왼쪽-오른쪽-루트
"""

import sys

# 노드의 개수 1<=26
N = int(sys.stdin.readline().strip())
# 이진 트리 변수
tree = {}

for n in range(N):
    # 노드, 왼쪽 자식과 오른쪽 자식이 입력으로 주어짐
    root, left, right = sys.stdin.readline().strip().split()
    # 노드는 딕셔너리의 키로,
    # 왼쪽 자식과 오른쪽 자식은 딕셔너리 노드 키의 리스트로 삽입
    tree[root] = [left, right]


# 전위순회
# 자식 노드가 없는 '.'을 제외하고
# root부터 왼쪽 자식과 오른쪽 자식 순으로 재귀
# 1. 첫 키 출력,
# 2. 첫 키의 왼쪽 값으로 루트를 설정하여 다시 자식 노드 확인해 재귀
def preorder(root):
    if root != '.':
        print(root, end='')      # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며,
# 항상 A가 루트 노드가 된다.
# 따라서 A를 고정 시작 값으로 사용한다.
# - 전위순회
preorder('A')
print()
# - 중위순회
inorder('A')
print()
# - 후위순회
postorder('A')
