<template>
  <div>
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col cols="6"><b>{{battleLog}}</b></b-col>
        <b-col><b-form-rating v-model="turnCounter" color="indigo" class="mb-2" readonly></b-form-rating></b-col>
        <b-col>남은 카드 수 : {{leftCardNum}}</b-col> 
        <b-col v-if="isPlayerTurn">{{playerTurn}}</b-col>
        <b-col v-if="!isPlayerTurn">{{bossTurn}}</b-col>
      </b-row>
      <b-row>
        <b-progress :max="maxHp" height="2rem" class="px-0">
          <b-progress-bar :value="playerHpBar" class="fw-bold" variant="danger">
            <span>Hp: <strong>{{playerHpBar}}</strong></span>
          </b-progress-bar>
        </b-progress>
      </b-row>
    </b-container>
    <!-- <p style="color:crimson;">Player Hp: {{ playerHp }}</p>
    <p v-if="isPlayerTurn">{{playerTurn}}</p>
    <p v-if="!isPlayerTurn">{{bossTurn}}</p>
    <h5>{{battleLog}}</h5> -->
  </div>
</template>

<script>
export default {
  name: 'ConsoleChat',
  data() {
    return {
      playerTurn: '플레이어 턴',
      bossTurn: '보스의 턴',
    }
  },
  props: {
    isPlayerTurn: Boolean,
    battleLog: String,
    turns: Number,
    playerHp: Number,
    playCardCount : Number,
    leftCardNum : Number,
    bossLevel : Number,
  },
  computed: {
    turnCounter() {
      return this.playCardCount
    },
    maxHp() {
      return 40 + this.bossLevel * 5
    },
    playerHpBar(){
      return this.playerHp
    }
  }
}
</script>

<style>

</style>