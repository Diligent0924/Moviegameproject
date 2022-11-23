<template>
  <div>
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col cols="8"><b>{{battleLog}}</b></b-col>
        <b-col style="color:crimson;"><b>Player Hp: {{ playerHp }}</b></b-col>
        <b-col v-if="isPlayerTurn">{{playerTurn}}</b-col>
        <b-col v-if="!isPlayerTurn">{{bossTurn}}</b-col>
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
  }
}
</script>

<style>

</style>