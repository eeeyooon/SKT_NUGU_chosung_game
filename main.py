

#은경님 코드



num = randint(0,len(w_list))

quize1 = w_list[num][0]
answer1 = w_list[num][1]

del w_list[num]

if not w_list:
  w_list = [['구사일생','아홉 번 죽을 뻔하다 한 번 살아난다는 뜻','많은 어려움을 겪고 살아남았을 때 쓰이는 말'],['견물생심' ,'물건을 실제로 보면 가지고 싶은 욕심이 생긴다는 뜻','좋은 물건을 보면 그것을 가지고 싶은 마음이 생기므로 욕심을 경계하라는 말'],['결초보은' ,'풀을 묶어 은혜를 값는 다는 뜻','죽어서도 은혜를 잊지 않고 갚는다는 말'],['고육지책 ','자신의 몸을 희생해 적을 속인다는 뜻','적을 이기거나 또는 어려운 사태를 벗어나기 위한 수단으로 제 몸을 괴롭혀가면서 까지 짜내어 마지막으로 쓰는 계책'],['과유불급','지나친 것은 미치치 못한것과 같다는 뜻','무엇이든 적당함이 가장 좋다는 말'],['교학상장 ','가르침과 배움이 서로 진보시켜 준다는 뜻','가르치는 일과 배우는 일이 서로 자신의 공부의 효과를 증진 시킨다는 말'],['구우일모 ','아홉 마리 소에게서 빠진 하나의 털이라는 뜻','매우 많은 것 가운데 극히 적은 수를 이르는 말'],['군자삼락 ','군자의 세 가지 즐거움이라는 뜻','첫째, 부모가 살아계시고, 둘째, 하늘을 우러러 부끄러움이 없고, 셋째, 천하의 영재를 가르치는 즐거움을 가리켜 맹자에 나오는 말'],['금시초문 ','이제 비로소 처음 들었다는 뜻    ','들은 소식이나 소문이 지금 처음 듣는 이야기라는 말'],['금의야행 ','비단옷을 입고 밤길을 간다는 뜻','애써 한 일을 아무도 알아주는 사람이 없어서 헛수고로 돌아감을 빗대는 말'],['기고만장 ','기운이 만 길이에 이를 만큼 치솟았다는 뜻','일이 잘 되어 그 기운이 하늘을 찌를 듯 높으며 흥분되어 있는 상태를 가리키는 말'],['대기만성 ','큰 그릇은 늦게 이루어진다는 뜻','큰 사람이 되기 위해서는 만은 노력과 시간이 필요함을 나타내는 말'],['동고동락 ','같이 고생하고 같이 즐거움도 함께 한다는 뜻','세상의 즐거운 일과 괴로운 일을 모두 함께 겪는 것을 가리키는 말'],['동문서답 ','동쪽을 묻는데 서쪽을 대답한다는 뜻','묻는 말에 대해 전혀 맞지 않는 엉뚱한 대답을 가르키는 말'],['동서고금 ','동양과 서양 그리고 옛날과 지금이라는 뜻','언제, 어디서나의 의미로 시간과 공간의 경계없이 공통적으로 해당되는 경우에 사용되는 말'],['명경지수 ','밝은 거울과 정지된 물이라는 뜻','고요하고 깨끗한 마음을 가리키는 말'],['목불인견 ','눈으로 차마 보지 못한다는 뜻','처지가 몹시 딱하거나 처참한 모습일 때 쓰여요. 슬프고 처참한 광경을 가리키는 말'],['문일지십 ','한 가지를 들으면 열 가지를 미루어 안다는 뜻','총명하고 영특하다는 말'],['문전성시 ','문 앞에 마치 시장이 선 것 같다는 뜻','세력이 있어 찾아오는 사람이 매우 많아 문 앞이 시장처럼 북적거릴 때 쓰이는 말'],['부지기수','그 수를 알지 못한다는 뜻','헤아릴 수 없을 만큼 매우 많은 양을 가리키는 말'],['비일비재 ','하나도 아니요, 둘도 아니다 라는 뜻','셀 수 없을 만큼 많은 것을 가리키는 표현으로 같은 일이 여러 번 일어날 때 쓰이는 말'],['사필귀정 ','무슨 일이든 결국 옮은 이치대로 돌아간다는 뜻','모든 일은 결국에는 반드시 바른 길로 돌아가게 되어 있음을 비유하는 말'],['삼고초려','초가집을 세 번 찾아간다는 뜻','훌륭한 인물을 모시기 위해 최선을 다하는 모습을 가리키는 말'],['삼삼오오 ','세 명씩 혹은 다섯 명씩, 각기 무리지어 흩어져 있는 사람들의 모습을 이르는 말','아주 많은 인원의 군중은 아니지만 소소하게 모여 무리를 이룬 것을 가리키는 말'],['새옹지마','변방에 사는 노인의 말 이라는 뜻','세상일은 변화가 많아 어떤 것이 좋거나 나쁜 것이 될지 예측하기 어렵다는 말'],['선견지명 ','앞서 내다보는 밝은 지혜라는 뜻','현재의 상황을 통해 미래를 예측하여 대비하는 것을 가르키는 말'],['설상가상 ','눈 위에 서리가 덮인 격이라는 뜻','엎친 데 덮친 격으로 어려운 일이 연거푸 일어남을 가르키는 말'],['소탐대실','작은 것을 탐하다가 큰 손실을 입는다는 뜻','물욕에 의해 나라가 망한 일화를 빗대어, 작은 욕심에 눈이 어두워져 큰 것을 잃는다는 말'],['신토불이 ','사람의 몸음 그 몸이 태어난 땅과 둘로 나뉠 수 없다는 뜻','자기가 사는 땅에서 나고 자란 것을 먹어야 한다는 의미'],['십중팔구 ','열 개 가운데 여덟, 아홉 개라는 뜻','높은 확률로 꽤 확신하고 미리 추측할 수 있는 경우를 나타내는 말'],['안면부지','얼굴을 모른다는 뜻','이전에 만난 적이 없어 서로 모르는 사이를 가리키는 말'],['안하무인 ','눈 아래 사람이 없다는 뜻','다른 사람을 존중하지 않고 무례하고 뻔뻔하게 행동하는 사람 또는 그러한 자세를 이르는 말 '],['약석지언','약이나 침과 같은 말이라는 뜻','사람의 잘못을 뉘우치고 고치게 하는 말'],['어두육미 ','물고기는 머리. 육고기는 꼬리가 맛있다는 뜻','맛있는 부위로서 물고기의 머리부위, 짐승고기의 꼬리부위 역시 버릴 것 없이 훌륭한 요리가 된다는 뜻'],['어부지리 ','두 사람이 다투는 사이에 엉뚱한 제 삼자가 얻게되는 예상치 못한 이익을 가리키는 표현','눈앞의 이익만 생각하다 보면 손해를 보는 경우도 생길 수 있으니 양보의 미덕을 발휘하라는 말'],['언중유골 ','말 속에 뼈가 있다는 뜻','예사로운 말 같으나 그 속에 단단한 속뜻이 들어 있음을 이르는 말'],['역지사지','다른 사람의 처지에서 생각하라는 뜻','자기 중심의 시각이 아니라 상대의 시각에서 헤아려 보라는 말'],['오만방자','거만하고 거만하여 남을 업신여기며 제멋대로 행동한다는 뜻','남을 업신여긴다는 오만하다 와 교만하고 제멋대로라는 방자하다 가 합쳐저 만들어진 표현으로 무례한 행동을 가리키는 말'],['온고지신','옛 것을 익히고 새 것을 안다는 뜻','    과거 전통과 역사가 바탕이 된 후에 새로운 지식이 습득되어야 제대로 된 배움이 될 수 있다는 말'],['요산요수','산을 좋아하고 물을 좋아하다는 뜻','지혜로운 사람은 물을 좋아하고 어진사람은 산을 좋아해 대부분 고요한 성격이라는 원래의 뜻이 있지만, 오늘날에는 경치가 좋아 자연을 사랑한 다는 뜻으로 쓰이는 말'],['우왕좌왕 ','오른쪽으로 갔다 왼쪽으로 갔다 한다는 뜻','결단력이 없어 일정한 방향을 잡지 못하고 입장을 바꾸는 모습을 가리키는 말'],['이구동성 ','입은 다르지만 하는 말은 같다는 뜻','여러 사람들의 의견이나 뜻이 하나로 모아질 때 쓰는 표현'],['이심전심 ','마음에서 마음으로 전한다는 뜻','말이나 글을 쓰지 않고도 서로 마음이 통한다는 뜻으로 텔레파시와 유사한 의미'],['일거양득 ','한 번에 두 가지의 이익을 얻는다는 뜻','한 가지 일을 하여 두 가지 이익을 얻음을 이르는 말'],['일구이언 ','한 입으로 두 말을 한다는 뜻','일관성 없이 말을 바꾸는 경우를 가리키는 말'],['일석이조 ','돌 하나를 던져 새 두 마리를 잡는다는 뜻','한 가지 일을 하여 두 가지 이익을 얻음을 이르는 말'],['일장일단 ','장점이 있으면 단점도 동시에 존재한다는 뜻','어떤 일이나 물건에 장점과 단점이 같이 있다는 말'],['일파만파 ','하나의 파도가 만 개의 파도를 일으킨다는 뜻','작은 한 사건이 큰 사건으로 번져감을 나타내는 뜻으로 쓰이는 말'],['일편단심','한 조각의 붉은 마음이라는 뜻','진정에서 우러나오는 변하지 않는 충성럽고 참된 마음을 가리키는 말'],['자수성가 ','스스로 집안을 일으켜 세우거나 큰 성과를 이루어 놓았다는 뜻','남의 도움이나 부모의 도움없이 어렵고 힘든 상황을 이겨내고 성공했을 때 쓰이는 말'],
['견물생심','물건을 실제로 보면 가지고 싶은 욕심이 생긴다는 뜻','좋은 물건을 보면 그것을 가지고 싶은 마음이 생기므로 욕심을 경계하라는 말'],['자신만만 ','스스로 자신을 믿는 마음이 가득가득 찼다는 뜻','무슨 일이든 할 수 있을 듯이 자신감이 가득 찬 모양을 가리키는 말']]




# 은경님 테스트 코드


#-*-coding:utf-8-*-
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

from random import *
CHO_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
def ko_word(word):
    r_lst = []
    for w in list(word.strip()):
        if '가' <= w <= '힣':
            ch1 = (ord(w) - ord('가')) // 588
            r_lst.append(CHO_LIST[ch1])
        else:
            r_lst.append([w])
    r_lst.append(' ') #맨뒤에.점을찍기위해 공백추가
    return r_lst

w_list = [['금시초문 ', '이제 비로소 처음 들었다는 뜻\t', '들은 소식이나 소문이 지금 처음 듣는 이야기라는 말'],
          ['기고만장 ','기운이 만 길이에 이를 만큼 치솟았다는 뜻','일이 잘 되어 그 기운이 하늘을 찌를 듯 높으며 흥분되어 있는 상태를 가리키는 말'],
          ['어부지리 ','두 사람이 다투는 사이에 엉뚱한 제 삼자가 얻게되는 예상치 못한 이익을 가리키는 표현','눈앞의 이익만 생각하다 보면 손해를 보는 경우도 생길 수 있으니 양보의 미덕을 발휘하라는 말']]


@app.route('/choicefourword', methods=['POST'])
def choicefourword():

    num = randint(0, len(w_list))

    w_cho = ko_word(fourWord)
    fourQuiz = ".".join(w_cho)
    response['output']['fourWord'] = w_list[num][0]  # 정답
    response['output']['fourMean'] = w_list[num][1]  # 뜻풀이
    response['output']['fourQuiz'] = fourQuiz
    response['output']['fourHint1'] = w_list[num][2]  # 힌트1.속뜻
    response['output']['fourHint2'] = w_list[num][0][:2]  # 힌트2.앞두글자
    del w_list[num]

    if not w_list:
        w_list = [['금시초문 ', '이제 비로소 처음 들었다는 뜻\t', '들은 소식이나 소문이 지금 처음 듣는 이야기라는 말'],['기고만장 ','기운이 만 길이에 이를 만큼 치솟았다는 뜻','일이 잘 되어 그 기운이 하늘을 찌를 듯 높으며 흥분되어 있는 상태를 가리키는 말'],['어부지리 ','두 사람이 다투는 사이에 엉뚱한 제 삼자가 얻게되는 예상치 못한 이익을 가리키는 표현','눈앞의 이익만 생각하다 보면 손해를 보는 경우도 생길 수 있으니 양보의 미덕을 발휘하라는 말']]  # 여기에 사자성어 전체갯수 또 넣어줘야함 슬랙에서 넘 길어지는것같아 생략했어요~



    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)


#은경님 서버코드 테스트 2= 중복x랜덤 전체코드

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



#사자성어


w_list = [['금시초문', '이제 비로소 처음 들었다는 뜻', '들은 소식이나 소문이 지금 처음 듣는 이야기라는 말'],
          ['기고만장', '기운이 만 길이에 이를 만큼 치솟았다는 뜻', '일이 잘 되어 그 기운이 하늘을 찌를 듯 높으며 흥분되어 있는 상태를 가리키는 말'],
          ['어부지리', '두 사람이 다투는 사이에 엉뚱한 제 삼자가 얻게되는 예상치 못한 이익을 가리키는 표현',
           '눈앞의 이익만 생각하다 보면 손해를 보는 경우도 생길 수 있으니 양보의 미덕을 발휘하라는 말'],
          ['요산요수', '산을 좋아하고 물을 좋아하다는 뜻',
           '지혜로운 사람은 물을 좋아하고 어진사람은 산을 좋아해 대부분 고요한 성격이라는 원래의 뜻이 있지만, 오늘날에는 경치가 좋아 자연을 사랑한 다는 뜻으로 쓰이는 말'],
          ['신토불이', '사람의 몸음 그 몸이 태어난 땅과 둘로 나뉠 수 없다는 뜻', '자기가 사는 땅에서 나고 자란 것을 먹어야 한다는 의미'],
          ['동서고금', '동양과 서양 그리고 옛날과 지금이라는 뜻', '언제, 어디서나의 의미로 시간과 공간의 경계없이 공통적으로 해당되는 경우에 사용되는 말']]
random.shuffle(w_list)  # 전체목록을 셔플1회 아주중요!ㅎㅎ



@app.route('/choicefourword', methods=['POST'])
def choicefourword():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    fourWord = w_list[0][0]
    w_cho = ko_word(fourWord)
    fourQuiz = ".".join(w_cho)
    response['output']['fourWord'] = w_list[0][0]  # 정답
    response['output']['fourMean'] = w_list[0][1]  # 뜻풀이
    response['output']['fourQuiz'] = fourQuiz
    response['output']['fourHint1'] = w_list[0][2]  # 힌트1.속뜻
    response['output']['fourHint2'] = w_list[0][0][:2]  # 힌트2.앞두글자
    del w_list[0]

    return json.dumps(response)


# 다음 사자성어

@app.route('/nextfourword', methods=['POST'])
def nextfourword():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    nextfourWord = w_list[0][0]
    w_cho = ko_word(nextfourWord)
    nextfourQuiz = ".".join(w_cho)
    response['output']['nextfourWord'] = w_list[0][0]  # 정답
    response['output']['nextfourMean'] = w_list[0][1]  # 뜻풀이
    response['output']['nextfourQuiz'] = nextfourQuiz
    response['output']['nextfourHint1'] = w_list[0][2]  # 힌트1.속뜻
    response['output']['nextfourHint2'] = w_list[0][0][:2]  # 힌트2.앞두글자
    del w_list[0]

    return json.dumps(response)



# 동물

a_list = [['고양이','야옹. 소리를 내요 '],  ['강아지', '멍멍. 소리를 내요'], ['거북이', '걸음이 느리지만 토끼와의 경주에서 이겼어요'],
          ['거위', '오리와 비슷하게 생겼는데 날지는 못해요'],['고래', '등에서 물을 분수처럼 뿜어내요 '],['고릴라', '주먹을 쥐고 땅을 짚으며 걸어요'],
          ['고슴도치', '등에 뾰족한 가시가 있어요'],['까마귀', '까악까악. 소리를 내고 반짝이는걸 좋아해요'],
          ['까치', '설날에 대한 노래에도 등장하고 이 동물이 울면 반가운 손님이 온다고 해요.'], ['낙타', '등에 혹을 달고 사막을 건너요'],
          ['너구리', '귀가 둥글고 꼬리가 통통해요'], ['늑대', '사냥을 잘하고 개와 비슷하게 생겼어요 '], ['다람쥐', '나무구멍이나 굴을 파서 겨울잠을 자고, 도토리를 좋아해요'],
          ['독수리', '새 중에서 하늘을 가장 높게 그리고 가장 오래 날아요'], ['돌고래', '미끈한 피부를 가지고 있고 수영을 잘해요'],
          ['돼지', '꿀꿀. 소리를 내요 '], ['두더지', '눈이 아주 작고 앞을 잘 보지 못하는데 땅굴을 잘 파요 '],
          ['딱따구리', '단단한 부리로 나무에 구멍을 내요 '], ['라마', '기분이 나쁠때 침을 뱉어요'],
          ['망아지', '어린 말을 이렇게 불러요'],['박쥐', '깜깜한 곳에 거꾸로 매달리는 걸 잘해요 '], ['반달가슴곰', '앞가슴에 반달모양의 하얀 털을 가지고 있어요'],
          ['백조', '우아한 모습이 멋져요, 러시아 발레의 모티프가 되기도 했어요'], ['병아리', '닭의 새끼로 삐약삐약. 소리를 내요'],
          ['부엉이', '밤에 활동하는 야행성이고 몸이 잘 돌아가요'], ['북극곰', '북극에 살아요'], ['비둘기', '구구. 소리를 내요'],
          ['사막여우', '머리보다 큰 귀로 체온을 조절해요, 여우 중에서는 가장 몸집이 작은 편이예요'], ['사슴', '크고 긴 뿔을 가지고 있어요.']]

random.shuffle(a_list)  # 전체목록을 셔플1회 아주중요!ㅎㅎ


@app.route('/choiceanimal', methods=['POST'])
def choiceanimal():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    aniWord = a_list[0][0]
    a_cho = ko_word(aniWord)
    aniQuiz = ".".join(a_cho)
    response['output']['aniWord'] = a_list[0][0]  # 정답
    response['output']['aniQuiz'] = aniQuiz
    response['output']['aniHint1'] = a_list[0][1]  # 힌트1.특징
    response['output']['aniHint2'] = a_list[0][0][:1]  # 힌트2.앞글자
    del a_list[0]

    return json.dumps(response)


# 다음 동물문제

@app.route('/nextanimal', methods=['POST'])
def nextanimal():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    nextaniWord = a_list[0][0]
    a_cho = ko_word(nextaniWord)
    nextaniQuiz = ".".join(a_cho)
    response['output']['nextaniWord'] = a_list[0][0]  # 정답
    response['output']['nextaniQuiz'] = nextaniQuiz
    response['output']['nextaniHint1'] = a_list[0][1]  # 힌트1.특징
    response['output']['nextaniHint2'] = a_list[0][0][:1]  # 힌트2.앞글자
    del a_list[0]

    return json.dumps(response)



# 과일

f_list = [['바나나','원숭이가 좋아해요'],['레몬','상큼하고 신맛이 강해요'],['사과','백설공주를 깊게 잠들게 했어요'],
          ['블루베리','알이 작고 보라색이에요'],['수박','껍질이 단단하고 과육이 빨간색이에요.'],['참외','노란색에 흰 줄무늬가 있어요'],
          ['두리안','냄새가 지독해요'],['감귤','제주도에서 많이 자라고 주황색이에요'],['딸기','빨간 색이고 작은 씨들이 꼼꼼이 박혀있어요'],
          ['복숭아','딱딱한 종류와 말랑한 종류가 있고 무척 달콤해요'],['메론','단단한 껍질을 자르면 안에 부드러운 연두색 과육이 있어요'],
          ['키위','솜털이 난 갈색 껍질이 둘러싸고 있어요']]


random.shuffle(f_list)  # 전체목록을 셔플1회 아주중요!ㅎㅎ


@app.route('/choicefruit', methods=['POST'])
def choicefruit():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    fruWord = f_list[0][0]
    f_cho = ko_word(fruWord)
    fruQuiz = ".".join(f_cho)
    response['output']['fruWord'] = f_list[0][0]  # 정답
    response['output']['fruQuiz'] = fruQuiz
    response['output']['fruHint1'] = f_list[0][1]  # 힌트1.특징
    response['output']['fruHint2'] = f_list[0][0][:1]  # 힌트2.앞글자
    del f_list[0]

    return json.dumps(response)


# 다음 과일문제

@app.route('/nextfruit', methods=['POST'])
def nextfruit():
    utteranceParameter = getUtteranceParameter
    response = commonResponse

    nextfruWord = f_list[0][0]
    f_cho = ko_word(nextfruWord)
    nextfruQuiz = ".".join(f_cho)
    response['output']['nextfruWord'] = f_list[0][0]  # 정답
    response['output']['nextfruQuiz'] = nextfruQuiz
    response['output']['nextfruHint1'] = f_list[0][1]  # 힌트1.특징
    response['output']['nextfruHint2'] = f_list[0][0][:1]  # 힌트2.앞글자
    del f_list[0]

    return json.dumps(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)




#도영팀장님



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