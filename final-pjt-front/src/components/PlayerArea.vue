<template>
  <div>
    <div style="display: flex; justify-content: center;">
      <PlayerCardItem
        v-for="(card, index) in userCards"
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
  computed: {
    userCards() {
      return this.$store.state.userCards
    }
  }
}
</script>

<style>

</style>