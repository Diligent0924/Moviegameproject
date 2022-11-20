<template>
  <div>
    <span>남은 카드 수  : {{ copiedDeck.length }}</span>
    <hr>
    <b-button :class="{disabled : !isPlayerTurn}" block variant="danger" @click="endTurn">턴 종료</b-button>
    <b-button :class="{disabled : !inAttack}" block variant="warning" @click="cancelAttack">공격 취소</b-button>
    <BossArea :boss="boss" :bossLevel="bossLevel" :inAttack="inAttack" @attackTo="attackTo" />
    <ConsoleChat style="float: left; margin-left: 50px;" :isPlayerTurn="isPlayerTurn" :battleLog="battleLog" :turns="turns" :playerHp="playerHp" />
    <div>
      <!-- 무덤 -->
      <DeadCards style="float: right; margin-right: 50px;" :deadCards="deadCards" />
    </div>
    <PlayerArea class="downside" :userHand="startDeck" @play-card="playCard" />
    <InField :fieldCards="inFields" @attack="attack" @goToDie="goToDie" />
  </div>
</template>

<script>
import ConsoleChat from '@/components/ConsoleChat'
import DeadCards from '@/components/DeadCards'
import PlayerArea from '@/components/PlayerArea'
import BossArea from '@/components/BossArea'
import _ from 'lodash'
import InField from '@/components/InField'

export default {
  name: 'PlayingAreaView',
  components: {
    ConsoleChat,
    DeadCards,
    PlayerArea,
    BossArea,
    InField,
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
      turns: 1,
      boss: null,
      bossLevel: 0,
      inAttack: false,
      cardIndex : null,
      playerHp: 30,
    }
  },
  created() {
    this.deckCopy()
  },
  methods: {
    deckCopy() {
      this.boss = _.cloneDeep(this.$store.state.bossCards[this.bossLevel])
      this.copiedDeck = _.cloneDeep(this.$store.state.userCards)
      this.startDeck = _.sampleSize(this.copiedDeck, 5)
      this.startDeck.forEach((aCard) => {
        const index = this.copiedDeck.indexOf(aCard)
        this.copiedDeck.splice(index, 1)
      })
    },
    endTurn() {
      this.isPlayerTurn = !this.isPlayerTurn
      this.battleLog = null
      this.turns++
      
      setTimeout(() => {
        // 턴 회복
        this.playCardCount = 2
        // 카드 드로우
        if (this.copiedDeck.length > 0) {
          let drawCard = _.sample(this.copiedDeck)
          const index = this.copiedDeck.indexOf(drawCard)
          this.copiedDeck.splice(index, 1)
          this.startDeck.push(drawCard)
        }
        // 보스 공격
        this.bossAttack()

        this.inFields.forEach((aCard) => {
          aCard['canAttack'] = true
        })
        this.isPlayerTurn = !this.isPlayerTurn
      }, 1500)
    },
    playCard(card) {
      if (this.playCardCount > 0) {
        const index = this.startDeck.indexOf(card)
        this.startDeck.splice(index, 1)
        let newCard = card
        newCard['canAttack'] = false
        this.inFields.push(newCard)
        this.playCardCount--
      } else {
        alert('이미 두 장의 카드를 내려놓았습니다.\n 필드의 유닛을 클릭해 공격하거나 턴 종료 버튼을 눌러주세요.')
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
    },
    cancelAttack() {
      this.inAttack = false
      this.battleLog = '공격을 취소하였습니다. \n다음 행동을 선택해주세요'
    },
    win() {
      this.battleLog = '축하합니다. 승리하였습니다. 잠시 후 다음 단계로 이동합니다.'
      setTimeout(() => {
        this.$router.push({ name: 'coin' })
        this.$store.dispatch('win', { 'bossLevel': this.bossLevel+1, 'turns': this.turns })

        this.copiedDeck = null
        this.startDeck =  null
        this.deadCards = []
        this.inFields = []
        this.playCardCount = 2
        this.battleLog = '전투 시작! 필드에 내려놓을 카드를 클릭해주세요'
        this.turns = 1
        this.boss = null
        this.bossLevel++
        this.inAttack = false
        this.cardIndex = null,
        this.playerHp = this.playerHp+5
      }, 2000)
    },
    bossAttack() {
      const targets = this.inFields.length
      if (targets === 0) {
        this.playerHp -= this.boss.attackdamage
        this.battleLog = `${this.boss.name}가 플레이어에게 ${this.boss.attackdamage}의 피해를 입혔다.`
      } else {
        const atkNum = _.sample(_.range(1, targets+2))
        if (atkNum === targets+1) {
          this.playerHp -= this.boss.attackdamage
          this.battleLog = `${this.boss.name}가 플레이어에게 ${this.boss.attackdamage}의 피해를 입혔다.`
        } else {
          this.inFields[atkNum-1].hp -= this.boss.attackdamage
          this.battleLog = `${this.boss.name}가 ${this.inFields[atkNum-1].name}에게 ${this.boss.attackdamage}의 피해를 입혔다.`
        }
      }
      setTimeout(() => {
        this.battleLog = '손패를 클릭해 내려놓거나, 필드의 유닛을 클릭해 공격하세요'
      }, 1500)
    },
    lose() {
      this.battleLog = '안타깝게도 패배하였습니다. 잠시 후 게시글 작성 페이지로 이동합니다.'
      setTimeout(() => {
        this.$router.push({ name: 'createarticle' })
        this.$store.dispatch('lose', { 'turns': this.turns })

        this.copiedDeck = null
        this.startDeck =  null
        this.deadCards = []
        this.inFields = []
        this.playCardCount = 2
        this.battleLog = '전투 시작! 필드에 내려놓을 카드를 클릭해주세요'
        this.turns = 1
        this.boss = null
        this.bossLevel++
        this.inAttack = false
        this.cardIndex = null,
        this.playerHp = this.playerHp+5
      }, 2000)
    },
    goToDie(dyingCard) {
      const index = this.inFields.indexOf(dyingCard)
      this.inFields.splice(index, 1)
      this.deadCards.push(dyingCard)
    }
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
  .downside {
    position: fixed;
    bottom: 60px;
    width: 100%;
  }

</style>