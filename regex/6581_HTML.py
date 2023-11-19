import sys

doc = sys.stdin.read()

# 1. 공백 기준 문자열 분리
str_list = doc.split()

# var: hr는 '-' 80글자 출력을 위함
# var: temp_list는 출력해야 할 문장을 단어 단위로 저장
# var: temp_list는 출력해야 할 문장을 텍스트 단위로 저장
temp_list = list()
temp_line_text = ""

# 분리된 문자열을 단어 단위로 분기
for word in str_list:
    # 2. 현재 단어가 <br>이면 새 줄을 시작해야 함
    # 우선 저장한 문자열을 모두 출력하고 개행
    if word == "<br>":
        temp_line_text = ' '.join(temp_list)
        temp_list = list()
        print(temp_line_text)
    # 3. 현재 단어가 <hr>이면 구분선 출력
    # 현재 줄에서 첫 구분선 출력 지시일 시 구분선만,
    # 아니면 저장한 문자열 모두 출력하고 구분선 출력
    elif word == "<hr>":
        if len(temp_list) != 0:
            temp_line_text = ' '.join(temp_list)
            temp_list = list()
            print(temp_line_text)
        hr = "-" * 80
        print(hr)
    # 4. 일반 단어들은 이전 단어와 합치다가
    # 80글자가 넘으면 넘는 시점의 단어는 '출력 대상'에서 제외
    else:
        temp_list.append(word)
        temp_line_text = ' '.join(temp_list)
        if len(temp_line_text) > 80:
            temp_list.pop(-1)
            temp_line_text = ' '.join(temp_list)
            print(temp_line_text)
            temp_list = list()
            temp_list.append(word)

# 반복 종료 후 마지막 라인 출력
temp_line_text = ' '.join(temp_list)
print(temp_line_text)
