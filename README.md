# chosung_game with AI Speaker

![image](https://user-images.githubusercontent.com/102462534/181045065-4c42cbf4-5291-4de5-9513-0d55705fa342.png)
<br>

> ### SKT의  NUGU AI Speaker를 활용한 초성게임 앱 제작 프로젝트

<br>

이 프로젝트는 SKT와 함께하는 인재양성 교육을 통해 진행되었습니다.<br>
프로젝트의 참여인원은 강지윤, 정은경, 이기암, 김만재입니다. 팀 훈민정음의 PM/기획/개발로 참여하였습니다.

<br/>

#### :bulb: 프로젝트 주제 : SKT NUGU AI Speaker 음성인식을 기반으로 한 아동 대상 언어능력 향상 초성게임 서비스
#### ✅ 프로젝트 목적 : 아동의 집중력, 순발력, 언어능력 등의 향상과 흥미 유발 기대 
#### 📆 프로젝트 구현 기간 : 2021년 11월 9일 ~ 2021년 12월 3일
#### 🦉 서비스 제공 스펙 : 알버트 AI에 탑재하여 제공, 지역 및 언어는 국내 / 한국어를 대상으로 함.
|서비스 분류|제공 경로|상세 내용
|-|-|-|
| 디바이스 | 알버트 AI | NUGU 앱에서 확인 |
| Voice AI cloud | SKT TTS |  기본: 한국 여자 20 ~ 30세 목소리 |
| 제공 플랫폼 | Nugu APP | Nugu Play - 정보/생활 |
| 지역과 시간대 | 국내 | GMT 9:00 |
| 특정 IP (어뷰징) 제한 | 알버트 AI/ Nugu 스피커 유입 | 없음 |


<br/>

#### 🛠 기술 스택
- Python
- AWS - EC2
- Python3 Flask

#### 💻 개발 환경 및 툴
- windows
- pycharm
- vim
- SKT NUGU developers
- Slack

<br>
<br>


### 👨🏻‍🔧 Nugu Developers

NUGU developers는 SK텔레콤이 보유한 최고 수준의 음성 인식, 음성 합성, 자연어 이해 등의 기술력을 기반으로 NUGU 혹은 제휴사의 디바이스와 앱 사용자에게 AI 서비스를 제공할 수 있는 플랫폼입니다. NUGU 플랫폼 기반의 AI 서비스를 편리하게 개발할 수 있도록 다양한 Tool과 개발 문서를 제공합니다.

**NUGU play kit**는 NUGU 플랫폼에서 동작하는 AI 서비스의 단위인 NUGU play를 만들고 관리 수 있도록 서비스 사업자나 개인 개발자를 위해 제공하는 툴입니다. **NUGU play kit**는 간단한 코드 정의와 예시 문장 입력만으로 손쉽게 NUGU play를 만들 수 있는 Play Builder와 생성한 NUGU play를 관리, 배포하고 사용 통계를 조회할 수 있는 콘솔로 구성되어 있습니다. 
<br>


**Nugu Play Builder**는 NUGU play를 생성하는 개발 도구로 이용자의 발화를 이해하는 User Utterance Model, 이를 기반으로 기능을 수행하는 Action을 조합하여 하나의 완결된 Play를 생성합니다.
<br>
<br>

<br>


## 1. 초성게임 앱 기능

초성게임 앱은 다음과 같은 기능을 가지고 있습니다.

1. 주제별 문제 제공 : [동물], [과일], [사자성어] 세가지 주제로 게임 가능
2. 틀렸을 때 힌트 제공 : 첫번째 힌트로는 정답인 단어의 특징, 두번째 힌트로는 '첫 글자'를 제공함.
3. 칭찬멘트와 응원멘트 제시 : 정답을 맞혔을땐 칭찬멘트, 틀렸을땐 응원멘트로 성취감과 동기부여 제공
4. 다음 문제 기능 : "다음 문제"라고 발화하면 연속적으로 게임 진행 가능
5. 게임 결과 안내 기능 : 사용자가 "게임종료"를 원하면 푼 문제수와 맞힌 문제수를 안내함.

<br/><br/>

> ###  nugu play와 서버 구조의 세부 기능은 다음과 같습니다.

![서비스 세부 기능 정의](https://user-images.githubusercontent.com/102462534/165879022-c6db267e-0346-4558-895f-8b5b76b9931b.png)

<br/><br/>

> ### 앱 기능에 대한 flow chart는 다음과 같습니다.

![초성게임 flow chart](https://user-images.githubusercontent.com/102462534/165879471-e56b8dca-16d0-485a-b162-4afee3388d67.png)

<br/><br/>

> ### 각 기능에 대한 VUX 시나리오는 다음과 같습니다.

기본 초성게임 진행 1  |   기본 초성게임 진행 2
:-------------------------:|:-------------------------:
![vux 시나리오 1](https://user-images.githubusercontent.com/102462534/165879479-f31667a9-7b96-4f71-b4eb-2502d1497e60.png) | ![vux 시나리오 2](https://user-images.githubusercontent.com/102462534/165879486-6a405f30-a345-4285-95cb-1acdd50beaf4.png)



<br>



<br/><br/>

## 2. 초성게임 Nugu play 앱 구조
<br/>

> ### Nugu play의 구조는 다음과 같습니다.


![play구조 1](https://user-images.githubusercontent.com/102462534/165883408-02fa5925-0072-4eb1-859c-7aee5e8e43e0.png)
![play구조 2](https://user-images.githubusercontent.com/102462534/165883410-fead96c0-3650-4ff8-bf12-b7ba7da47454.png)
![play구조 3](https://user-images.githubusercontent.com/102462534/165883412-318cf080-5fbe-4f45-8700-084e177da7a4.png)

<br>

<br>


## 3. API 서버 구현

Python3 Flask를 이용한 API 서버를 구현하였습니다. github를 통해 관리되는 소스코드는 Nugu play에서 사용하기 위한 API 서버 및 DB 관련 코드입니다. 웹서버는 아마존 AWS에서 Flask를 통해 동작합니다. Nugu play로부터 정의된 요청(POST방식)이 오면, 그에 대한 응답을 json형태로 반환하게 됩니다.

<br/><br/>



## 4. 기타 

프로젝트의 자세한 내용은 서비스 기획서, 상세기획서에서 확인할 수 있습니다. <br>
시연 영상이 궁금하거나 해당 프로젝트에 대한 문의사항이 있으신 분은 vywns4569@gmail.com으로 문의 주시면 감사하겠습니다.


