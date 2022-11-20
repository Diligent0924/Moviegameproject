<template>
  <div>
    <h3>플레이어 체력 : {{ playerHp }}</h3>
    <h3>
      {{turns}} 번째 턴
    </h3>
    <p v-if="isPlayerTurn">{{playerTurn}}</p>
    <p v-if="!isPlayerTurn">{{bossTurn}}</p>
    <p>{{battleLog}}</p>
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