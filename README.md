# chosung_game with AI Speaker
> ### SKT의  NUGU AI Speaker를 활용한 초성게임 앱 제작 프로젝트

이 프로젝트는 SKT와 함께하는 인재양성 교육을 통해 진행되었습니다.
프로젝트의 참여인원은 강지윤, 정은경, 이기암, 김만재입니다.
<br/>
- 팀 훈민정음의 PM/기획/개발로 참여하였습니다.

<br/>

### 프로젝트 주제 : SKT NUGU AI Speaker 음성인식을 기반으로 한 아동 대상 언어능력 향상 초성게임 서비스

<br/>

## 1. 초성게임 앱 기능

초성게임 앱은 다음과 같은 기능을 가지고 있습니다.

1. 주제별 문제 제공 : [동물], [과일], [사자성어] 세가지 주제로 게임 가능
2. 틀렸을 때 힌트 제공 : 첫번째 힌트로는 정답인 단어의 특징, 두번째 힌트로는 '첫 글자'를 제공함.
3. 칭찬멘트와 응원멘트 제시 : 정답을 맞혔을땐 칭찬멘트, 틀렸을땐 응원멘트로 성취감과 동기부여 제공
4. 다음 문제 기능 : "다음 문제"라고 발화하면 연속적으로 게임 진행 가능
5. 게임 결과 안내 기능 : 사용자가 "게임종료"를 원하면 푼 문제수와 맞힌 문제수를 안내함.

<br/><br/>

> ### nugu play와 서버 구조의 세부 기능은 다음과 같습니다.

![서비스 세부 기능 정의](https://user-images.githubusercontent.com/102462534/165879022-c6db267e-0346-4558-895f-8b5b76b9931b.png)

<br/><br/>

> ### 앱 기능에 대한 flow chart는 다음과 같습니다.

![초성게임 flow chart](https://user-images.githubusercontent.com/102462534/165879471-e56b8dca-16d0-485a-b162-4afee3388d67.png)

<br/><br/>

> ### 각 기능에 대한 VUX 시나리오는 다음과 같습니다.

![vux 시나리오 1](https://user-images.githubusercontent.com/102462534/165879479-f31667a9-7b96-4f71-b4eb-2502d1497e60.png)
![vux 시나리오 2](https://user-images.githubusercontent.com/102462534/165879486-6a405f30-a345-4285-95cb-1acdd50beaf4.png)


<br/><br/>

## 2. 초성게임 Nugu play 앱 구조
<br/>

> ### Nugu play의 구조는 다음과 같습니다.


![play구조 1](https://user-images.githubusercontent.com/102462534/165883408-02fa5925-0072-4eb1-859c-7aee5e8e43e0.png)
![play구조 2](https://user-images.githubusercontent.com/102462534/165883410-fead96c0-3650-4ff8-bf12-b7ba7da47454.png)
![play구조 3](https://user-images.githubusercontent.com/102462534/165883412-318cf080-5fbe-4f45-8700-084e177da7a4.png)

<br/><br/>

## 3. API 서버 구현

Python3 Flask를 이용한 API 서버를 구현하였습니다. github를 통해 관리되는 소스코드는 Nugu play에서 사용하기 위한 API 서버 및 DB 관련 코드입니다. 웹서버는 아마존 AWS에서 Flask를 통해 동작합니다. Nugu play로부터 정의된 요청(POST방식)이 오면, 그에 대한 응답을 json형태로 반환하게 됩니다.

<br/><br/>

## 4. 기타
해당 프로젝트에 대한 문의사항이 있으시면 vywns4569@gmail.com으로 문의 가능합니다.


