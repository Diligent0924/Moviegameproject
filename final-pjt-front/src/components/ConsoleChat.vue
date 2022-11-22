<template>
  <div>
    <p>Player Hp: {{ playerHp }}</p>
    <!-- <p>gu{{turns}} 번째 턴</p> -->
    <p v-if="isPlayerTurn">{{playerTurn}}</p>
    <p v-if="!isPlayerTurn">{{bossTurn}}</p>
    <h3>{{battleLog}}</h3>
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