<template>
  <div>
    <div></div>
    <hr>
    <BossArea/>
    <ConsoleChat style="float: left; margin-left: 100px;"/>
    <div>
      <!-- 무덤 -->
      <DeadCards style="float: right; margin-right: 100px;"/>
    </div>
    <PlayerArea class="downside"/>
  </div>
</template>

<script>
import ConsoleChat from '@/components/ConsoleChat'
import DeadCards from '@/components/DeadCards'
import PlayerArea from '@/components/PlayerArea'
import BossArea from '@/components/BossArea'

export default {
  name: 'PlayingAreaView',
  components: {
    ConsoleChat,
    DeadCards,
    PlayerArea,
    BossArea,
  },
}
</script>

<style>
  .downside {
    position: fixed;
    bottom: 60px;
    width: 100%;
  }

</style>