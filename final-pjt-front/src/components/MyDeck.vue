<template>
  <div>
    <h3>
      My Deck
    </h3>
    <div style="display: flex;">
      <MyCard
       v-for="(card, index) in userCards"
       :key="`${card.id}-${index}`"
       :card="card"
      />
    </div>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'

export default {
  name: 'MyDeck',
  components: {
    MyCard
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