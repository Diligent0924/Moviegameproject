<template>
  <div>
    <h3>보스 공간</h3>
    <p>{{boss}}</p>
    <div style="display: flex; justify-content: center;">
      <BossCardItem
        v-for="(card, index) in cards"
        :key="`${index}-${card}-inbossarea`"
        :card=card
      />
    </div>
  </div>
</template>

<script>
import BossCardItem from '@/components/BossCardItem'

export default {
  name: 'BossArea',
  components: {
      BossCardItem
  },
  data() {
    return {
      cards: ['card1', 'card2', 'card3', 'card4', 'card5'],
      
    }
  },
  computed: {
    bossLevel() {
      return this.$store.state.bossLevel
    },
    boss() {
      return this.$store.state.bossCards[this.bossLevel]
    }
  }
}
</script>

<style>

</style>