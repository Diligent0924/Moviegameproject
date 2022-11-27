<template>
  <div>
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col cols="6"><b>{{bossbattleLog}}</b></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'BossConsoleChat',
  data() {
    return {
      playerTurn: '플레이어 턴',
      bossTurn: '보스의 턴',
    }
  },
  props: {
    bossbattleLog: String,
  },
}
</script>

<style>

</style>