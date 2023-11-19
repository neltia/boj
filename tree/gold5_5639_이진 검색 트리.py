"""
이진 검색 트리(BST, Binary Search Tree)
트리vs그래프: 트리는 순환 구조를 갖지 않는 그래프

이진 트리:
1. 노드의 왼쪽 서브트리의 모든 노드의 키는 노드의 키보다 작다.
2. 노드의 오른쪽쪽 서브트리의 모든 노드의 키는 노드의 키보다 크다.
3. 왼쪽, 오른쪽 서브트리도 이진 검색 트리다.

전위 순회(preorder): 루트-왼쪽-오른쪽
- 루트를 방문하고, 왼쪽, 오른쪽 서브 트리를 순서대로 방문하며 노드 키 출력

후위 순회(postorder): 왼쪽-오른쪽-루트
- 루트를 방문하고, 왼쪽, 오른쪽 서브 트리를 순서대로 방문하며 노드 키 출력
"""

import sys

# 재귀 깊이를 입력 조건인 노드에 든 키 값은 10^6보다 작은 양의 정수임을 반영
sys.setrecursionlimit(10**6)

# 입력이 없을 때까지 입력 값을 리스트에 추가
# - 전위 순회한 트리 값
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except EOFError:
        break


# 후위 순회: postorder
def postorder(first, end):
    # 시작과 끝 값이 역전되면 끝
    if first > end:
        return

    # 오른쪽 노드가 없을 경우
    mid = end + 1

    # 서브 트리 찾기
    for i in range(first+1, end+1):
        # 첫 값(루트)보다 크면 오른쪽 서브 트리에 해당
        if num_list[first] < num_list[i]:
            mid = i
            break

    # 왼쪽 서브 트리 재귀 탐색
    postorder(first + 1, mid - 1)
    # 오른쪽 서브 트리 재귀 탐색
    postorder(mid, end)
    # 탐색 값 출력
    print(num_list[first])


# 전체 트리 값을 두고 후위순회 시작
postorder(0, len(num_list)-1)
