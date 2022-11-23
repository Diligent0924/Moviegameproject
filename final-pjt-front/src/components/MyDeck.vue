<template>
  <div>
    <h3>
      My Deck
    </h3>
    <b-list-group-item>
      <b-list-group-item>
        <b-row class="text-start mx-1 rounded">
          <b-col cols="2">card</b-col>
          <b-col cols="5">name</b-col>
          <b-col cols="2">type</b-col>
          <b-col cols="1">AD</b-col>
          <b-col cols="1">HP</b-col>
        </b-row>
      </b-list-group-item>
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