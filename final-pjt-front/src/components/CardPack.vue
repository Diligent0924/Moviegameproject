<template>
  <div>
    <div style="display: flex;">
      <CardPackItem
        v-for="(card, index) in cards"
        :key="`${index}-${card}`"
        :card=card
        style="margin-left: 20px; margin-right: 20px;"
      />
    </div>
    <b-button :class="{disabled : cardNum}" variant="outline-primary" @click="openCard">카드 오픈!</b-button>
  </div>
</template>

<script>
import CardPackItem from '@/components/CardPackItem'

export default {
  name: 'CardPack',
  components: {
    CardPackItem
  },
  methods: {
    openCard() {
      this.$store.dispatch('openCard')
    }
  },
  computed: {
    cardNum() {
      return this.$store.state.userCards.length
    },
    cards() {
      return this.$store.state.randomCards
    }
  }
}
</script>

<style>

</style>