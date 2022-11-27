## Runserver 전 반드시 알아야 하는 일
- 처음 DB를 생성한 후 Boss가 안보이는 에러가 있을 수 있음
- 이럴 경우에는 위 버튼의 초기화를 누른 뒤 다시 회원가입하여 게임을 진행해야함.
- 또한 맨 처음에는 추천 영화가 없음 => 알고리즘이 카드를 많이 뽑은 순서대로 주기 때문임.

## 게임 설명
1. 처음 3장 중 1장을 뽑아 10장을 채우면 게임이 시작된다.
2. 액션은 아래 별 표시가 차 있는 것으로 나타나 있으며 기본적으로 매 턴마다 액션은 2이다.
    - 액션은 카드를 내는 것으로 판단한다. (하수인 / 스킬에 상관 없이 액션 1이 소모된다.)
    - 기존에 나와있던 하수인이 공격하는 것은 액션으로 치지 않는다.
3. 기본적으로 카드는 주문과 하수인으로 구분되며, 하수인은 일부 특수카드를 제외하면 필드에 나온 다음 턴부터 공격이 가능하다.. 
4. 아래의 콘솔 창으로 어떤 일이 일어나고 있는지를 알 수 있다.
5. 유저가 하나의 스테이지를 지나갈 때마다 4개의 토큰을 받는다.
    - 하나의 토큰은 카드 1개를 추가하거나, 기존 카드 1개를 삭제하는 데 사용할 수 있다.
6. 만약 유저가 7스테이지(마지막 스테이지)까지 가게 되면 Article 작성 후에 User 정보는 그대로 남는다.
7. 유저가 7스테이지 미만에서 게임이 끝날 경우 Article을 작성하게 되고 그 후에 유저 정보는 삭제된다. (로그라이크 응용)


## 팀원 정보 및 업무 분담 내역

### 박용찬

- DB Modeling (ERD)
- Backend (DRF)
- CSS
- 카드 게임 결과 기반 영화 추천 알고리즘 설계

### 최은성

- FrontEnd (Vue, JavaScripts)
- CSS
- 카드 처리 로직 작성

## 목표 서비스 구현 및 실제 구현 정도

- 최종적으로는 PVP 서비스 구현이 목적이였으며 현재는 PVE으로 구성된 상태이다.
- 유저의 덱 및 스킬 구현을 백엔드에서 구현했어야하나 PVE 특성 상 localstorage 사용이 더 빠르다고 판단되어 프론트에서 메서드를 구현하였다.
    
    ⇒ 향후 이 부분을 백엔드로 옮기면서 PVP 구현 예정이다.
    
- 일부 기능이 느리다고 판단하여 파티셔닝을 통하여 Modeling하였다.
    - 이후 카드가 추가된다면 효과적으로 사용할 수 있을 것이라고 판단된다.
- 현재 전체적으로 게임이 돌아가고 있으며 필요한 메서드는 구현했다고 판단된다.

## 데이터베이스 모델링 (ERD)

![ERD](https://lab.ssafy.com/sdc00035/final-pjt/-/raw/main/ssafy-pjt-pjt.png)

## 영화 추천 알고리즘에 대한 기술적 설명

- 게임을 통하여 사용자가 가장 많이 사용하는 영화 카드를 확인한 후 group by / Sorting을 통하여 사용자에게 영화를 추천한다. (처음 DB가 없는 경우에는 추천 알고리즘이 없으므로 반드시 게임을 한판 시작한 상태여야한다.)
- 해당 알고리즘은 게임과 결합하여 영화를 추천해주는 서비스로 게임의 재미와 영화의 재미를 동시에 느끼게 해준다.

## 서비스 대표 기능에 대한 설명

- Gamification을 통한 영화 추천을 하였다.
- 영화 정보(평점, 인기도 등)를 기반으로 제작한 카드를 토대로 게임을 진행하여 자연스럽게 흥미를 유도하고, 결과적으로 영화 추천으로 이어지게 하였다.

## 배포 서버 URL

- Ngrok를 통해서 배포를 시도하였으나, https 관련 에러로 추정되는 사유로 실패함

## 기타 (느낀 점, 후기)

### 박용찬

- 기존에 ngrok에서 Vue + django를 띄어본 적이 있으나 이번 프로젝트에서는 서버 배포에 실패하였음.
    - Vue router와 연관되어 Error가 발생된 것이라고 생각되는데 너무 아쉬웠다.
    - 프로젝트 기간이 조금 더 길었으면 배포까지 가능하지 않았을까 하는 아쉬움이 너무 컸다.
- 영화 추천 사이트와는 아예 다르게 프로젝트를 진행하니 정말 많은 것들을 배울 수 있었다.
    - 실제 처음부터 ERD를 전부 다 짜고 논리구조를 생각하며 백엔드를 할 수 있어서 너무 좋았다.
    - git에 대한 중요성을 배울 수 있었으며 git branch/merge 등을 정확히 배울 수 있어 이후 팀 프로젝트 시에 많은 도움이 될 것이라고 생각했다.
- 초기에 ERD나 구조를 먼저 확실하게 짜고 프로젝트를 진행해야 된다는 것을 뼈져리게 느꼈다.
    - 초기에 간단하다고 생각했던 것보다 더 많은 것들을 생각해야 되었으며 중간중간에 변경이 있었다.
    - 처음 구조를 잘 짜고 시작했다고 생각했지만 다른 여러가지 부분들에서 좀 더 구조를 잘 짜고 진행해야겠다는 생각이 들었다.
    - 프로젝트 기간에 비해 많은 것들을 하고자 하는 욕심 때문에 나중에는 ERD를 축소하거나 다른 부분들을 줄여서 너무 아쉬웠으며 다음부터는 기간 내 완성을 할 수 있는지도 구조를 짤 때 필요함을 느꼈다.
- 다른 모든 것들을 배울 수 있어서 너무 좋았으며 내가 좋아하는 장르를 할 수 있어서 너무 좋았다.
    - 이런 프로젝트를 같이 해준 팀원에게 너무 감사하다.
- 새로운 프로젝트가 시작하기 전에 해당 프로젝트를 좀 더 많이 구현해보고 싶다.
    - Socket / PVP 등을 구현하여 이전의 나보다 더 많이 성장하고 싶다고 생각했다.

### 최은성

- 주먹구구식으로 시작한 프로젝트이다보니, 작업 과정에서 잦은 구조 변경이 발생한것이 아쉬웠다.
- 메서드를 어느 곳에서 사용하는 것이 효율적인지, 어떠한 정보가 DB에 들어가고 어떤 필드값을 가지는게 효과적인지 등 많은 것을 배우고 느낄 수 있었다.
- 어떤 정보를 백엔드 단에서 처리하고 어떤 상황을 프론트 단에서 처리해야 하는지에 대한 감각을 잡을 수 있었다.
- 초기에 교수님이 MVP와 핵심 기능에 대한 정의 및 설계가 중요하다고 말하셨는데, 정말 생각이상으로 그것들이 중요함을 실감했고, 다음 프로젝트를 진행할 땐 다소 시간이 걸리더라도 사소한 부분 하나하나까지 정의하고 설계한 뒤에 프로젝트를 진행하는 것이 좋을것 같다.
- 다른 팀들과는 조금 다른 프로젝트를 진행했기 때문에 동료들을 통해 많이 배우지 못한 것이 아쉽지만, 남들과는 다른 부분에서 공부를 많이 한 것 같다.
- 절대적 시간이 부족해 작동하는 것에만 초점을 두고 작업을 진행하여 코드가 많이 복잡해진게 아쉽다.
    - 차후에 시간이 허락된다면 기능 단위로 메서드를 더 효율적으로 작성하여 이용해보고 싶다.
- **※아무튼 결과를 떠나서 과정 내내 즐거웠고, 이상한 프로젝트 제안했는데도 믿고 같이 해준 팀원에게 고맙다.**
