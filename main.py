

# -*-coding:utf-8-*-
from flask import Flask, request, json
import random
import os

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}
}


def getUtteranceParameter():
    data = request.get_json()
    return data['action']['Parameters']


@app.route('/')
def index():
    return 'Hello Flask'


CHO_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def ko_word(word):
    r_lst = []
    for w in list(word.strip()):
        if '가' <= w <= '힣':
            ch1 = (ord(w) - ord('가')) // 588
            r_lst.append(CHO_LIST[ch1])
        else:
            r_lst.append([w])
    r_lst.append(' ')
    return r_lst

good = ['좋아요! 잘하고 있어요!','이 문제를 풀다니 정말 대단해요', '정말 최고최고!','너무 잘하는데요? 저한테도 그 비법을 알려주세요!','당신은 초성퀴즈 왕! 인정합니다','어쩜 이렇게 초성게임을 잘하는지, 배우고싶어요!']
cheerUp = ['아이캔두잇! 할 수 있어요!','노력하는 모습이 너무 멋져요!','우리 조금만 더 힘내요!', '이번 문제가 조금 어려웠네요. 하지만 다음 문제는 분명 맞힐 수 있을거예요.','포기하지 말고 도전해봐요. 분명 멋지게 해낼거예요.']




# 과일

f_list = [['사과','나쁜 마녀가, 백설공주를, 깊게 잠들게 하기 위해, 독을 묻혔던 과일이에요. '],
          ['수박','초록 바탕에 검정 줄무늬를 가진, 단단한 껍질을 자르면, 빨간 속살이 드러난답니다. 여름에 가장 인기가 많은 과일이에요.'],
          ['두리안','아름다운 천국의 달콤한 맛과, 끔직한 지옥의 지독한 냄새를 가지고 있어요. 과일의, 여왕으로, 불린답니다.'],
          ['감귤','제주도에서 많이 자라고, 새콤달콤한 향기와 맛을 가지고 있답니다. 많이 먹으면, 손이 노래질수도 있어요.'],
          ['메론','하얀색의 촘촘한 그물 무늬가 있는, 단단한 껍질을 자르면, 부드럽고 달콤한, 연두색의 속살을 먹을 수 있어요.'],
          ['키위','뽀송뽀송, 하기도 하고, 까끌까끌, 하기도 한, 갈색의 솜털이 껍질에 있어요, 그리고 뉴질랜드에 사는, 날개 없는 새와, 이름이 같답니다.']]


random.shuffle(f_list)


@app.route('/choicefruit', methods=['POST'])
def choicefruit():
    utteranceParameter = getUtteranceParameter


    global number
    number = 0
    global cnt
    cnt = 1

    response = commonResponse

    f_cheerUp = random.randint(0,len(cheerUp)-1)
    f_good = random.randint(0,len(good)-1)

    fruWord = f_list[0][0]
    f_cho = ko_word(fruWord)
    fruQuiz = ".".join(f_cho)
    response['output']['fruWord'] = f_list[0][0]  # 정답
    response['output']['fruQuiz'] = fruQuiz
    response['output']['fruHint1'] = f_list[0][1]  # 힌트1.특징
    response['output']['fruHint2'] = f_list[0][0][:1]  # 힌트2.앞글자
    response['output']['f_cnt'] = cnt
    response['output']['f_number'] = number
    response['output']['f_cheerUp'] = cheerUp[f_cheerUp]
    response['output']['f_good'] = good[f_good]


    del f_list[0]

    return json.dumps(response)

#fruit_c 카운트

@app.route('/fruit_c', methods=['POST'])
def fruit_c():

    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)

    response = commonResponse

    response['output']['f_number'] = number


    return json.dumps(response)



# fruHint1_c 카운트

@app.route('/fruhint1_c', methods=['POST'])
def fruhint1_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['f_number'] = number


    return json.dumps(response)




# fruHint2_c 카운트

@app.route('/fruhint2_c', methods=['POST'])
def fruhint2_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['f_number'] = number

    return json.dumps(response)




# 다음 과일문제

@app.route('/nextfruit', methods=['POST'])
def nextfruit():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    global cnt
    cnt += 1
    print(cnt)

    nf_cheerUp = random.randint(0,len(cheerUp)-1)
    nf_good = random.randint(0,len(good)-1)

    nextfruWord = f_list[0][0]
    f_cho = ko_word(nextfruWord)
    nextfruQuiz = ".".join(f_cho)
    response['output']['nextfruWord'] = f_list[0][0]  # 정답
    response['output']['nextfruQuiz'] = nextfruQuiz
    response['output']['nextfruHint1'] = f_list[0][1]  # 힌트1.특징
    response['output']['nextfruHint2'] = f_list[0][0][:1]  # 힌트2.앞글자
    response['output']['nf_cnt'] = cnt
    response['output']['nf_number'] = number
    response['output']['nf_cheerUp'] = cheerUp[nf_cheerUp]
    response['output']['nf_good'] = good[nf_good]


    del f_list[0]

    return json.dumps(response)


#nextfruit_c 카운트

@app.route('/nextfruit_c', methods=['POST'])
def nextfruit_c():

    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['nf_cnt'] = cnt
    response['output']['nf_number'] = number

    return json.dumps(response)




# nextfruHint1_c 카운트

@app.route('/nextfruHint1_c', methods=['POST'])
def nextfruHint1_c():
    utteranceParameter = getUtteranceParameter

    global number
    number += 1
    print(number)

    response = commonResponse
    response['output']['nf_number'] = number

    return json.dumps(response)




# nextfruHint2_c 카운트

@app.route('/nextfruHint2_c', methods=['POST'])
def nextfruHint2_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['nf_number'] = number

    return json.dumps(response)




# 동물

a_list = [['고릴라','무섭게 화난 것처럼 보이지만, 사실 겁이 많아요. 그리고 주먹을 쥐고, 땅을 짚으며 걸어요. 특이하죠?'],
          ['펭귄','미끄러운 얼음 위에서, 두 발로 뒤뚱뒤뚱, 잘 걷고, 물 속으로 풍덩, 다이빙도 잘해요.'],
          ['햄스터','해바라기 씨를 입 안에 가아득 넣을 수 있는, 볼 주머니가 있고, 몸집이 아주 작아요.'],
          ['카멜레온','마법사처럼 몸 색을 자유롭게 바꿀 수 있고, 기이인 혀로 먹이를 잡을 수 있어요. 그리고 양쪽 눈이 빙그르르, 360도 자유롭게, 따로따로 움직인답니다.'],
          ['까치', '설날에 대한 노래에도 등장하고 이 동물이 울면 반가운 손님이 온다고 해요.'],
          ['백조', '우아한 모습이 멋져요, 러시아 발레의 모티프가 되기도 했어요'],['사막여우', '머리보다 큰 귀로 체온을 조절해요, 여우 중에서는 가장 몸집이 작은 편이예요']]

random.shuffle(a_list)


@app.route('/choiceanimal', methods=['POST'])
def choiceanimal():
    utteranceParameter = getUtteranceParameter

    global number
    number = 0
    global cnt
    cnt = 1

    response = commonResponse

    a_cheerUp = random.randint(0,len(cheerUp)-1)
    a_good = random.randint(0,len(good)-1)


    aniWord = a_list[0][0]
    a_cho = ko_word(aniWord)
    aniQuiz = ".".join(a_cho)
    response['output']['aniWord'] = a_list[0][0]  # 정답
    response['output']['aniQuiz'] = aniQuiz
    response['output']['aniHint1'] = a_list[0][1]  # 힌트1.특징
    response['output']['aniHint2'] = a_list[0][0][:1]  # 힌트2.앞글자
    response['output']['a_cnt'] = cnt
    response['output']['a_number'] = number
    response['output']['a_cheerUp'] = cheerUp[a_cheerUp]
    response['output']['a_good'] = good[a_good]

    del a_list[0]

    return json.dumps(response)

#animal_c 카운트

@app.route('/animal_c', methods=['POST'])
def animal_c():

    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['a_number'] = number


    return json.dumps(response)




# anihint1_c 카운트

@app.route('/anihint1_c', methods=['POST'])
def anihint1_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['a_number'] = number

    return json.dumps(response)



# anihint2_c 카운트

@app.route('/anihint2_c', methods=['POST'])
def anihint2_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['a_number'] = number

    return json.dumps(response)


# 다음 동물문제

@app.route('/nextanimal', methods=['POST'])
def nextanimal():
    utteranceParameter = getUtteranceParameter

    global cnt
    cnt += 1
    print(cnt)

    response = commonResponse

    na_cheerUp = random.randint(0,len(cheerUp)-1)
    na_good = random.randint(0,len(good)-1)


    nextaniWord = a_list[0][0]
    a_cho = ko_word(nextaniWord)
    nextaniQuiz = ".".join(a_cho)
    response['output']['nextaniWord'] = a_list[0][0]  # 정답
    response['output']['nextaniQuiz'] = nextaniQuiz
    response['output']['nextaniHint1'] = a_list[0][1]  # 힌트1.특징
    response['output']['nextaniHint2'] = a_list[0][0][:1]  # 힌트2.앞글자
    response['output']['na_cnt'] = cnt
    response['output']['na_number'] = number
    response['output']['na_cheerUp'] = cheerUp[na_cheerUp]
    response['output']['na_good'] = good[na_good]

    del a_list[0]

    return json.dumps(response)

#nextanimal_c 카운트

@app.route('/nextanimal_c', methods=['POST'])
def nextanimal_c():

    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['na_cnt'] = cnt
    response['output']['na_number'] = number

    return json.dumps(response)




# nextaniHint1_c 카운트

@app.route('/nextaniHint1_c', methods=['POST'])
def nextaniHint1_c():
    utteranceParameter = getUtteranceParameter

    global number
    number += 1
    print(number)

    response = commonResponse
    response['output']['na_number'] = number

    return json.dumps(response)




# nextaniHint2_c 카운트

@app.route('/nextaniHint2_c', methods=['POST'])
def nextaniHint2_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['na_number'] = number

    return json.dumps(response)




#사자성어


w_list = [['금시초문', '이제 비로소 처음 들었다는 뜻', '들은 소식이나 소문이, 지금 처음 듣는, 이야기라는 말'],
          ['기고만장', '기운이, 만 길이에, 이를 만큼, 치솟았다는 뜻', '일이 잘 되어, 그 기운이 하늘을 찌를 듯, 높으며 흥분되어 있는 상태를, 가리키는 말'],
          ['어부지리', '두 사람이 다투는 사이에, 엉뚱한 제 삼자가 얻게되는, 예상치 못한 이익을, 가리키는 표현','눈앞의 이익만 생각하다 보면, 손해를 보는 경우도 생길 수 있으니, 양보의 미덕을 발휘하라는 말'],
          ['신토불이', '사람의 몸은, 그 몸이 태어난 땅과, 둘로 나뉠 수 없다는 뜻', '자기가 사는 땅에서, 나고 자란 것을, 먹어야 한다는 의미'],
          ['동문서답','동쪽을 묻는데, 서쪽을 대답한다는 뜻','묻는 말에 대해, 전혀 맞지 않는, 엉뚱한 대답을 가르키는 말'],
          ['새옹지마','변방에 사는, 노인의 말이라는 뜻','세상일은 변화가 많아, 어떤 것이 좋거나, 나쁜 것이 될지, 예측하기 어렵다는 말'],
          ['선견지명','앞서 내다보는, 밝은 지혜라는 뜻','현재의 상황을 통해, 미래를 예측하여, 대비하는 것을, 가르키는 말']]

random.shuffle(w_list)



@app.route('/choicefourword', methods=['POST'])
def choicefourword():
    utteranceParameter = getUtteranceParameter

    global number
    number = 0
    global cnt
    cnt = 1

    response = commonResponse

    w_cheerUp = random.randint(0,len(cheerUp)-1)
    w_good = random.randint(0,len(good)-1)

    fourWord = w_list[0][0]
    w_cho = ko_word(fourWord)
    fourQuiz = ".".join(w_cho)
    response['output']['fourWord'] = w_list[0][0]  # 정답
    response['output']['fourMean'] = w_list[0][1]  # 뜻풀이
    response['output']['fourQuiz'] = fourQuiz
    response['output']['fourHint1'] = w_list[0][2]  # 힌트1.속뜻
    response['output']['fourHint2'] = w_list[0][0][:2]  # 힌트2.앞두글자
    response['output']['w_cnt'] = cnt
    response['output']['w_number'] = number
    response['output']['w_cheerUp'] = cheerUp[w_cheerUp]
    response['output']['w_good'] = good[w_good]


    del w_list[0]

    return json.dumps(response)



#four_c 카운트

@app.route('/four_c', methods=['POST'])
def four_c():

    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['w_number'] = number


    return json.dumps(response)




# fourHint1_c 카운트

@app.route('/fourHint1_c', methods=['POST'])
def fourHint1_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['w_number'] = number

    return json.dumps(response)




# fourHint2_c 카운트

@app.route('/fourHint2_c', methods=['POST'])
def fourHint2_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['w_number'] = number

    return json.dumps(response)




# 다음 사자성어

@app.route('/nextfourword', methods=['POST'])
def nextfourword():
    utteranceParameter = getUtteranceParameter


    global cnt
    cnt += 1
    print(cnt)

    response = commonResponse

    nw_cheerUp = random.randint(0,len(cheerUp)-1)
    nw_good = random.randint(0,len(good)-1)


    nextfourWord = w_list[0][0]
    w_cho = ko_word(nextfourWord)
    nextfourQuiz = ".".join(w_cho)
    response['output']['nextfourWord'] = w_list[0][0]  # 정답
    response['output']['nextfourMean'] = w_list[0][1]  # 뜻풀이
    response['output']['nextfourQuiz'] = nextfourQuiz
    response['output']['nextfourHint1'] = w_list[0][2]  # 힌트1.속뜻
    response['output']['nextfourHint2'] = w_list[0][0][:2]  # 힌트2.앞두글자
    response['output']['nw_cnt'] = cnt
    response['output']['nw_number'] = number
    response['output']['nw_cheerUp'] = cheerUp[nw_cheerUp]
    response['output']['nw_good'] = good[nw_good]

    del w_list[0]

    return json.dumps(response)

#nextfour_c 카운트

@app.route('/nextfour_c', methods=['POST'])
def nextfour_c():

    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['nw_cnt'] = cnt
    response['output']['nw_number'] = number

    return json.dumps(response)




# nextfourHint1_c 카운트

@app.route('/nextfourHint1_c', methods=['POST'])
def nextffourHint1_c():
    utteranceParameter = getUtteranceParameter

    global number
    number += 1
    print(number)

    response = commonResponse
    response['output']['nw_number'] = number

    return json.dumps(response)




# nextfourHint2_c 카운트

@app.route('/nextfourHint2_c', methods=['POST'])
def nextfourHint2_c():
    utteranceParameter = getUtteranceParameter


    global number
    number += 1
    print(number)


    response = commonResponse
    response['output']['nw_number'] = number

    return json.dumps(response)


#end 액션

@app.route('/endaction', methods=['POST'])
def endaction():
    utteranceParameter = getUtteranceParameter


    global cnt
    global number

    response = commonResponse

    response['output']['e_cnt'] = cnt
    response['output']['e_number'] = number


    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
