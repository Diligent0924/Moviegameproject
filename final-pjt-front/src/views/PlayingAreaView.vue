<template>
  <div class="mt-3">
    <b-container class="bv-example-row">
      <b-row class="mb-5">
        <b-col cols="2">
          <DeadCards style="float: right; margin-right: 50px;" :deadCards="deadCards" />
        </b-col>
        <b-col cols="8">
          <b-row>
            <BossArea :boss="boss" :bossLevel="bossLevel" :inAttack="inAttack" @attackTo="attackTo" />
          </b-row>
          <b-row class="text-center ps-5" style="margin-left:20%">
              <BossConsoleChat :bossbattleLog="bossbattleLog" class="ms-5"/>
          </b-row>
        </b-col>
        <b-col cols="2">
        </b-col>
      </b-row>
      <b-row style="height:250px;">
        <InField :fieldCards="inFields" @attack="attack" @goToDie="goToDie" :onTarget="onTarget" @pickTarget="pickTarget" />
      </b-row>

      <b-row class="my-3">
        <b-col>
          <b-button :class="{disabled : !isPlayerTurn}" block variant="primary" @click="endTurn">턴 종료</b-button>&nbsp;&nbsp;&nbsp;&nbsp;
          <b-button :class="{disabled : !inAttack && !onTarget}" block variant="warning" @click="cancelAttack">취소</b-button>&nbsp;&nbsp;&nbsp;&nbsp;
          <b-button block variant="danger" @click="lose">항복</b-button>
        </b-col>
      </b-row>

      <b-row>
        <b-col>
          <ConsoleChat style="margin-left: 50px;" :bossLevel="bossLevel" :playCardCount="playCardCount" :leftCardNum="leftCardNum" :isPlayerTurn="isPlayerTurn" :battleLog="battleLog" :turns="turns" :playerHp="playerHp" />
        </b-col>
      </b-row>

      <b-row style="margin-top:1%; padding-bottom: 2%;">
        <b-col>
          <PlayerArea :userHand="startDeck" @play-card="playCard" />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ConsoleChat from '@/components/ConsoleChat'
import DeadCards from '@/components/DeadCards'
import PlayerArea from '@/components/PlayerArea'
import BossArea from '@/components/BossArea'
import _ from 'lodash'
import InField from '@/components/InField'
import BossConsoleChat from '@/components/BossConsoleChat.vue'

export default {
  name: 'PlayingAreaView',
  components: {
    ConsoleChat,
    DeadCards,
    PlayerArea,
    BossArea,
    InField,
    BossConsoleChat
},
  data() {
    return {
      copiedDeck: null,
      startDeck: null,
      deadCards: [],
      isPlayerTurn: true,
      inFields: [],
      playCardCount: 2,
      battleLog: '전투 시작! 필드에 내려놓을 카드를 클릭해주세요',
      bossbattleLog : '',
      turns: 1,
      boss: null,
      bossLevel: 0,
      inAttack: false,
      cardIndex : null,
      playerHp: 40,
      isFreezed: false,
      playerFreezed: 0,
      onTarget: false,
      atkCard: null,
      willDie: null,
      canDraw: 0,
      canUseUnique: 0,
      alreadyWin: false,
    }
  },
  created() {
    this.deckCopy()
  },
  computed: {
    leftCardNum(){
      return this.copiedDeck.length
    }
  },
  methods: {
    deckCopy() {
      this.bossLevel = this.$store.state.bossLevel
      this.playerHp = this.$store.state.playerHp
      this.boss = _.cloneDeep(this.$store.state.bossCards[this.bossLevel])
      this.copiedDeck = _.cloneDeep(this.$store.state.userCards).map((card) => {
        card.canAttack = false
        return card
      })
      this.startDeck = _.sampleSize(this.copiedDeck, 5)
      this.startDeck.forEach((aCard) => {
        const index = this.copiedDeck.indexOf(aCard)
        this.copiedDeck.splice(index, 1)
      })
    },
    drawCard() {
      if (this.copiedDeck.length > 0) {
        let drawCard = _.sample(this.copiedDeck)
        const index = this.copiedDeck.indexOf(drawCard)
        this.copiedDeck.splice(index, 1)
        
        if (this.startDeck.length < 6) {
          this.startDeck.push(drawCard)
        } else {
          alert('손패는 최대 6장 입니다!')
        }
      }
    },
    endTurn() {
      this.isPlayerTurn = !this.isPlayerTurn
      this.battleLog = null
      this.turns++
      
      if (this.willDie) {
        this.goToDie(this.willDie)
        this.willDie = null
      }

      setTimeout(() => {
        // 턴 회복
        if (this.playerFreezed) {
          this.playerFreezed--
          this.battleLog = '빙결 상태이기 때문에 행동력을 회복하지 않습니다.'
        } else {
          this.playCardCount = 2
        }
        // 카드 드로우
        if (this.canDraw) {
          this.canDraw--
          this.battleLog = '카드를 뽑을 수 없습니다.'
        } else {
          this.drawCard()
        }
        // 보스 공격
        if (this.isFreezed) {
          this.isFreezed = false
        } else {
          this.bossAttack()
        }

        // 디버프 잔여 턴 감소
        if (this.canUseUnique) {
          this.canUseUnique--
        }

        this.inFields.forEach((aCard) => {
          aCard.canAttack = true
        })
        this.isPlayerTurn = !this.isPlayerTurn
      }, 1500)
    },
    playCard(card) {
      if (this.playCardCount > 0) {

        if (card.movietype === 'unique') {
          if (this.canUseUnique) {
            alert(`유니크 카도의 사용이 ${this.canUseUnique}턴 동안 불가합니다!`)
          } else {
            this.battleLog = card.skillcomment
            if (card.hp === 0) {
              // 주문
              if (card.skillcomment === '얼어 붙어라!') {
                // 보스에게 20의 피해를 주고 빙결 상태로 만듭니다.
                this.boss.hp -= card.skillrange
                this.isFreezed = true
                this.handToDie(card)
              } else if (card.skillcomment === '나는 밑에서 한장 너는 위에서 한장') {
                this.drawCard()
                this.drawCard()
                this.handToDie(card)
              } else if (card.skillcomment === '나는 필연적 존재이다!') {
                // 플레이어와 보스 중 한명의 체력이 반으로 줄어듭니다.
                let whodie = _.sample(_.range(2))
                if (whodie) {
                  const newhp = Math.floor(this.boss.hp / 2);
                  this.battleLog = `보스의 체력이 ${this.boss.hp-newhp}만큼 감소합니다.`
                  this.boss.hp = newhp;
                } else {
                  const newhp = Math.floor(this.playerHp / 2);
                  this.battleLog = `플레이어의 체력이 ${this.playerHp-newhp}만큼 감소합니다.`
                  this.playerHp = newhp;
                }
                this.handToDie(card)
              } else if (card.skillcomment === 'Manners maketh man') {
                // 이번턴에 추가 액션을 획득합니다.
                this.playCardCount += 3
                this.handToDie(card)
              } else if (card.skillcomment === 'We will find a way. we always have.') {
                // 모든 아군 체력 10 증가
                this.handToDie(card)
                this.inFields.forEach((inField) => {
                  inField.hp += card.skillrange
                })
              } else if (card.skillcomment === '프로틴-바') {
                // 플레이어의 체력이 30 증가합니다.
                this.handToDie(card)
                this.playerHp += card.skillrange
              } else if (card.skillcomment === 'I am Iron man') {
                // 모든 하수인의 공격력이 + 10이 됩니다.
                this.handToDie(card)
                this.inFields.forEach((inField) => {
                  inField.attackdamage += card.skillrange
                })
              } else if (card.skillcomment === '친구는 가까이 두고, 적은 더 가까이 두어야 한다.') {
                // 적이 한턴 공격을 쉽니다.
                this.isFreezed = true
                this.handToDie(card)
              } else if (card.skillcomment === '내가 왕이 될 상인가') {
                // 하수인을 선택합니다. 공격력 60 or 공격력 1이 됩니다.
                this.setTarget(card)
              } else if (card.skillcomment === '키미노 나마에와') {
                // 하수인을 선택합니다. 보스와 이름을 바꿉니다. 10의 생명력과 공격력을 얻습니다.
                this.setTarget(card)
              } else if (card.skillcomment === '하지만, 내가 돌아가면, 다시 날씨가..!') {
                // 필드가 바뀝니다. 보스의 공격력이 5만큼 감소합니다.
                this.boss.attackdamage -= card.skillrange
                this.handToDie(card)
              } else if (card.skillcomment === '넌 내 꿈이구 어머니 희망이야. 어서 가.') {
                // 하수인을 선택합니다. 해당 하수인이 손으로 돌아갑니다. 필드 하수인들의 체력이 +10이 됩니다.
                this.setTarget(card)
              } else if (card.skillcomment === '아무도 없으면 외롭지 않으니까요.') {
                // 필드에 아무것도 없다면 50/50짜리 김씨를 소환합니다.
                if (!this.inFields.length) {
                const KimSsi = {
                    'attackdamage': 50,
                    'hp': 50,
                    'movietype': 'normal',
                    'posterpath': card.posterpath,
                    'skillcomment': null,
                    'skillrange': null,
                    'skilltype': null,
                    'canAttack': false
                  }
                  this.inFields.push(KimSsi)
                }
                this.handToDie(card)
              } else if (card.skillcomment === '우린 노빠꾸다!') {
                // 하수인을 선택합니다. 하수인의 공격력이 40, 체력이 1이 됩니다.
                this.setTarget(card)
              } else if (card.skillcomment === '지나간 일에 새로운 눈물을 낭비하지 말자') {
                // 모든 하수인이 +20 회복됩니다.
                this.handToDie(card)
                this.inFields.forEach((inField) => {
                  inField.hp += card.skillrange
                })
              } else if (card.skillcomment === '신에게는 아직 12척의 배가 남아있습니다') {
                // 모든 하수인의 공격력이 +10 증가합니다.
                this.handToDie(card)
                this.inFields.forEach((inField) => {
                  inField.attackdamage += card.skillrange
                })
              } else if (card.skillcomment === '이 사람들 빨리 내보내야돼. 안 그러면 우리까지 위험해져') {
                this.handToDie(card)
                this.drawCard()
                this.drawCard()
                this.drawCard()
              } else if (card.skillcomment === '착해서 돈이 많은 게 아니라 돈이 많으니까 착한 거야') {
                this.handToDie(card)
                this.drawCard()
                this.drawCard()
                this.drawCard()
              } else if (card.skillcomment === '경찰이 고문해서 대학생이 죽었는데, 보도지침이 대수야?') {
                this.handToDie(card)
                this.drawCard()
                this.drawCard()
                this.drawCard()
              } else if (card.skillcomment === '왕갈비통닭 한마리요~') {
                // 하수인을 선택합니다. 체력이 +40 증가합니다.
                this.setTarget(card)
              } else if (card.skillcomment === '작별인사는 하고 가야지') {
                // 하수인을 선택합니다. 이번턴에 하수인의 공격력이 +40 증가합니다.
                this.setTarget(card)
              } else if (card.skillcomment === '아빠 딸로 태어나줘서 고맙습니다.') {
                // 내 캐릭터의 체력이 +40 증가합니다.
                this.handToDie(card)
                this.playerHp += card.skillrange
              } else if (card.skillcomment === '나 지금 이거 일생일대 기횐 거 같애') {
                this.handToDie(card)
                this.drawCard()
                this.drawCard()
                this.drawCard()
              } else if (card.skillcomment === '비벼~ 막비벼~') {
                // 하수인을 선택합니다. 해당 하수인의 양 옆의 체력이 +10 증가합니다.
                this.setTarget(card)
              } else if (card.skillcomment === '두려움은 직시하면 그 뿐. 바람은 계산하는 것이 아니라 극복하는 것이다.') {
                // 보스의 체력이 30 이하라면 즉사합니다. 아니라면 10의 데미지를 줍니다.
                this.handToDie(card)
                if (this.boss.hp <= 30) {
                  this.boss.hp -= 10000000
                } else {
                  this.boss.hp -= 10
                }
              } else if (card.skillcomment === '내일을 사는 놈은 오늘만 사는 놈을 못이긴다.') {
                // 하수인을 선택합니다. 해당 하수인의 공격력이 +40 증가합니다. 이번턴에 사망합니다.
                this.setTarget(card)
              }
            } else if (this.inFields.length < 6) {
              // 토템
              if (card.skillcomment === '대중들은 개,돼지 입니다. 적당히 짖어대다 알아서 조용해질 겁니다.') {
                // 자신을 제외한 모든 유닛의 체력이 10이 됩니다.
                this.inFields.forEach((inField) => { inField.hp = 10 })
                this.realPlay(card)
              } else if (card.skillcomment === '백엔드의 신') {
                // DB를 조작해 즉시 공격이 가능합니다.
                const index = this.startDeck.indexOf(card)
                this.startDeck.splice(index, 1)
                let newCard = card
                newCard['canAttack'] = true
                this.inFields.push(newCard)
                this.playCardCount--
              } else if (card.skillcomment === '누가 50이야?') {
                // 그냥 강합니다.
                this.realPlay(card)
              } else if (card.skillcomment === '이런 고병원성 바이러스에 늑장 대응하다가 구제역 사태처럼 전국으로 퍼지기라도 한다면 큰일입니다') {
                // 다른 모든 하수인의 체력이 10 감소합니다.
                this.inFields.forEach((inField) => {
                  inField.hp -= card.skillrange
                })
                this.realPlay(card)
              } else if (card.skillcomment === '사람은 어떤 일이 터진 후에야 후회해. 이건 인간이 멍하거나 나약해서가 아니라. 본능 때문이야') {
                // 필드의 모든 하수인을 파괴합니다.
                this.inFields.forEach((inField) => {
                  this.goToDie(inField)
                })
                this.realPlay(card)
              } else if (card.skillcomment === '음 머~') {
                // 이 소를 죽이지 말아주세요...
                this.realPlay(card)
              }
            } else {
              alert('필드의 최대 장수는 6장 입니다.')
            }
          }
        } else if (this.inFields.length < 6) {
          // 일반 카드
          this.realPlay(card)
        } else{
          alert('필드의 최대 장수는 6장 입니다.')
        }
      } else {
        alert('이미 두 번의 행동을 수행했습니다.\n필드의 유닛을 클릭해 공격하거나 턴 종료 버튼을 눌러주세요.')
      }
    },
    pickTarget(card) {
      console.log(card)
      if (card === this.atkCard) {
        alert('자기 자신은 대상으로 지정할 수 없습니다. 다른 대상을 선택하거나 취소 버튼을 눌러주세요.')
      } else {
        const index = this.inFields.indexOf(card)
        
        if (this.atkCard.skillcomment === '내가 왕이 될 상인가') {
          // 하수인 공격력이 60 or 1
          const luck = _.sample(_.range(2))
          if (luck) {
            this.inFields[index].attackdamage = 60
          } else {
            this.inFields[index].attackdamage = 1
          }
        } else if (this.atkCard.skillcomment === '키미노 나마에와') {
          // 보스와 이름을 바꿉니다.
          const bname = this.boss.name
          const cname = this.inFields[index].name
          this.inFields[index].name = bname
          this.boss.name = cname
          this.inFields[index].attackdamage += 10
          this.inFields[index].hp += 10
        } else if (this.atkCard.skillcomment === '넌 내 꿈이구 어머니 희망이야. 어서 가.') {
          // 하수인을 손으로 불러들임. 다른 모든 하수인 체력 + 10
          this.inFields.splice(index, 1)
          let newCard = card
          newCard.canAttack = false
          this.startDeck.push(newCard)
          this.inFields.forEach((inField) => { inField.hp += 10 })
        } else if (this.atkCard.skillcomment === '우린 노빠꾸다!') {
          // 하수인 공격력 40, 체력 1로 만듬
          this.inFields[index].attackdamage = 40
          this.inFields[index].hp = 1
        } else if (this.atkCard.skillcomment === '왕갈비통닭 한마리요~') {
          // 하수인 체력 +40
          this.inFields[index].hp += 40
        } else if (this.atkCard.skillcomment === '작별인사는 하고 가야지') {
          // 이번턴에 하수인 공격력 +25
          this.inFields[index].attackdamage += 25
        } else if (this.atkCard.skillcomment === '비벼~ 막비벼~') {
          // 바로 옆 하수인 체력 +10
          if (this.inFields.length >= index+2) {
            this.inFields[index+1].hP += 10
          }
          if (index !== 0) {
            this.inFields[index-1].hp += 10
          }
        } else if (this.atkCard.skillcomment === '내일을 사는 놈은 오늘만 사는 놈을 못이긴다.') {
          // 공격력 +40, but 이번턴 끝나고 죽음
          this.inFields[index].attackdamage += 40
          this.willDie = card
        }
        this.playCardCount--
        const atkIndex = this.startDeck.indexOf(this.atkCard)
        this.startDeck.splice(atkIndex, 1)
        this.deadCards.push(this.atkCard)
        this.atkCard = null
        this.onTarget = false
      }
    },
    attack(attackFrom) {
      this.cardIndex = this.inFields.indexOf(attackFrom)
      this.battleLog = '공격할 대상을 선택하세요.\n 공격을 취소하시려면 공격 취소 버튼을 눌러주세요.'
      this.inAttack = true
    },
    attackTo() {
      this.inFields[this.cardIndex]['canAttack'] = false
      const attacking = this.inFields[this.cardIndex]['name']
      const damage = this.inFields[this.cardIndex]['attackdamage']
      this.boss.hp -= damage
      this.battleLog = `${attacking}이 ${this.boss.name}에게 ${damage}의 피해를 입혔다.\n 다음 행동을 수행하세요.`
      this.inAttack = false
    },
    cancelAttack() {
      if (this.inAttack) {
        this.inAttack = false
        this.battleLog = '공격을 취소하였습니다. \n다음 행동을 선택해주세요'
      }
      if (this.onTarget) {
        this.onTarget = false
        this.battleLog = '특수 행동을 취소하였습니다. \n다음 행동을 선택해주세요.'
      }
    },
    win() {
      if (this.alreadyWin) {
        return
      } else {
        this.alreadyWin = true;
        if (this.bossLevel === 6) {
          this.battleLog = '축하합니다. 모든 스테이지를 클리어하였습니다! 잠시 후 게시글 작성 페이지로 이동합니다.'
          setTimeout(() => {
            this.$store.dispatch('canGoChange')
            this.$router.push({ name: 'createarticle' })
            this.$store.dispatch('win', { 'turns': this.turns })
          }, 1000)
        } else {
          this.$store.dispatch('canGoChange')
          this.battleLog = '축하합니다. 승리하였습니다. 잠시 후 다음 단계로 이동합니다.'
          setTimeout(() => {
            this.$router.push({ name: 'coin' })
            this.$store.dispatch('win', { 'turns': this.turns })
            this.$store.dispatch('canGoChange')
          }, 2000)
        }
      }
    },
    bossAttack() {
      // 일반 공격을 할지, 스킬을 쓸 지 결정
      const skillNum = this.boss.bossskill_set.length
      const whichSkill = _.sample(_.range(skillNum+3))
      const targets = this.inFields.length
      const atkNum = _.sample(_.range(targets+1))
      console.log(whichSkill)
      // 일반 공격
      if (whichSkill >= skillNum) {
        if (targets === 0 || atkNum === targets) {
          this.playerHp -= this.boss.attackdamage
          this.battleLog = `${this.boss.name}가 플레이어에게 ${this.boss.attackdamage}의 피해를 입혔다.`
          this.bossbattleLog = `플레이어에게 ${this.boss.attackdamage}의 피해를 입혔다.`
        } else {
          this.inFields[atkNum].hp -= this.boss.attackdamage
          this.battleLog = `${this.boss.name}가 ${this.inFields[atkNum].name}에게 ${this.boss.attackdamage}의 피해를 입혔다.`
          this.bossbattleLog = `${this.inFields[atkNum].name}에게 ${this.boss.attackdamage}의 피해를 입혔다.`
        }
        setTimeout(() => {
          this.battleLog = '손패를 클릭해 내려놓거나, 필드의 유닛을 클릭해 공격하세요'
        }, 1000)
      } else {
        // 스킬 공격
        const skillMessage = this.boss.bossskill_set[whichSkill]['skillcomment']
        const skillType = this.boss.bossskill_set[whichSkill]['skilltype']
        const skillRange = this.boss.bossskill_set[whichSkill]['skillrange']
        this.battleLog = `${skillMessage}`
        this.bossbattleLog = `${skillMessage}`

        if (skillType === 'heal') {
          this.boss.hp += skillRange
          this.battleLog += `\n${this.boss.name}가 체력을 ${skillRange}만큼 회복하였다.`

        } else if (skillType === 'buff') {
          this.boss.attackdamge += skillRange
          this.battleLog += `\n${this.boss.name}의 공격력이 ${skillRange}만큼 증가합니다.`
        } else if (skillType === 'deal' || skillType === 'healnuff') {
            if (targets === 0 || atkNum === targets) {
            this.playerHp -= skillRange
            this.battleLog += `\n${this.boss.name}가 플레이어에게 ${skillRange}의 피해를 입혔다.`
          } else {
              this.inFields[atkNum].hp -= skillRange
              this.battleLog += `\n${this.boss.name}가 ${this.inFields[atkNum].name}에게 ${skillRange}의 피해를 입혔다.`
            }
        } else if (skillType === 'alldeal') {
          this.inFields.forEach((fieldcard) => {
            fieldcard.hp -= skillRange
          })
          this.playerHp -= skillRange
          this.battleLog += `\n${this.boss.name}가 모든 카드와 플레이어에게 ${skillRange}의 데미지를 입혔다!`

        } else if (skillType === 'attacknuff') {
          if (targets === 0 || atkNum === targets) {
            setTimeout(() => {
              this.battleLog += `\n공격력 감소의 적용 대상이 없습니다!`
            })
          } else {
            if (this.inFields[atkNum].attackdamage - skillRange >= 0) {
              this.inFields[atkNum].attackdamage -= skillRange
            } else {
              this.inFields[atkNum].attackdamage = 0
            }
            this.battleLog = `${this.boss.name}가 ${this.inFields[atkNum].name}의 공격력을 ${skillRange}만큼 감소시켰다.`
          }
        } else {
          // 보스 기타 스킬
          if (skillMessage === '입 닥 쳐 말포이') {
            // 플레이어 한 턴 빙결
            this.playerFreezed = 1
          } else if (skillMessage === 'Expecto Patronum') {
            // 플레이어 카드 1장 태움
            const len = this.startDeck.length
            const randomIndex = _.sample(_.range(len))
            let willDead = this.startDeck[randomIndex]
            this.startDeck.splice(randomIndex, 1)
            this.deadCards.push(willDead)
          } else if (skillMessage === '아씨오 론 위즐리') {
            // 유니크 카드 1턴 사용 불가
            this.canUseUnique = 2
            this.battleLog = '유니크 카드의 사용이 1턴동안 제한됩니다.'
          } else if (skillMessage === '구리퓐도르!') {
            // 2턴간 드로우 불가
            this.canDraw = 2
          } else if (skillMessage === '임페리오') {
            // 10% 확률로 플레이어 즉사, 아니면 체력 -20
            const tenUnderDie = _.sample(_.range(100))
            if (tenUnderDie < 10) {
              this.lose()
            } else {
              this.playerHp -= 20
            }
          }
        }
        setTimeout(() => {
          this.battleLog = '손패를 클릭해 내려놓거나, 필드의 유닛을 클릭해 공격하세요'
        }, 2000)
      }
    },
    lose() {
      this.battleLog = '안타깝게도 패배하였습니다. 잠시 후 게시글 작성 페이지로 이동합니다.'
      setTimeout(() => {
        this.$store.dispatch('canGoChange')
        this.$router.push({ name: 'createarticle' })
        this.$store.dispatch('lose', { 'turns': this.turns })
        this.$store.dispatch('canGoChange')
      }, 2000)
    },
    goToDie(dyingCard) {
      const index = this.inFields.indexOf(dyingCard)
      this.inFields.splice(index, 1)
      this.deadCards.push(dyingCard)
    },
    handToDie(dyingCard) {
      this.playCardCount--
      const index = this.startDeck.indexOf(dyingCard)
      this.startDeck.splice(index, 1)
      this.deadCards.push(dyingCard)
      this.atkCard = null
    },
    setTarget(atkCard) {
      this.battleLog = '스킬 적용 대상을 선택하세요. \n취소를 원하시면 취소 버튼을 눌러주세요.'
      this.onTarget = true
      this.atkCard = atkCard
    },
    realPlay(card) {
      if (card === this.atkCard) {
        this.atkCard = null
      }
      const index = this.startDeck.indexOf(card)
      this.startDeck.splice(index, 1)
      let newCard = card
      newCard.canAttack = false
      this.inFields.push(newCard)
      this.playCardCount--
    },
  },
  watch: {
    'boss.hp' (nowHp) {
      if (nowHp <= 0) {
        this.win()
      }
    },
    playerHp (nowHp) {
      if (nowHp <= 0) {
        this.lose()
      }
    }
  }
}
</script>

<style>

</style>