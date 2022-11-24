<template>
  <div>
    <div style="display: flex; justify-content: center;">
      <PlayerCardItem
        v-for="(card, index) in userHand"
        :key="`${index}-${card}inplayerarea`"
        :card=card
        @playCard="playCard" class="mx-2"
      />
    </div>
  </div>
</template>

<script>
import PlayerCardItem from '@/components/PlayerCardItem'

export default {
  name: 'PlayingArea',
  components: {
    PlayerCardItem
  },
  props: {
    userHand: Array,
  },
  methods: {
    playCard(payload) {
      this.$emit('play-card', payload)
    }
  }
}
</script>

<style>

</style>