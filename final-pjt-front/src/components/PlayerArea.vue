<template>
  <div>
    <div style="display: flex; justify-content: center;">
      <PlayerCardItem
        v-for="(card, index) in cards"
        :key="`${index}-${card}inplayerarea`"
        :card=card
      />

    </div>
    <h3>
      플레이어 공간
    </h3>
  </div>
</template>

<script>
import PlayerCardItem from '@/components/PlayerCardItem'

export default {
  name: 'PlayingArea',
  components: {
    PlayerCardItem
  },
  data() {
    return {
      cards: ['card1', 'card2', 'card3', 'card4', 'card5']
    }
  }
}
</script>

<style>

</style>