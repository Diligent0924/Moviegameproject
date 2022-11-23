<template>
  <div>
    <h3>
      My Deck
    </h3>
    <b-list-group-item>
      <MyCard
       v-for="(card, index) in userCards"
       :key="`${card.id}-${index}`"
       :card="card"
      />
    </b-list-group-item>
    <!-- <div>
      <MyCard
       v-for="(card, index) in userCards"
       :key="`${card.id}-${index}`"
       :card="card"
      />
    </div> -->
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