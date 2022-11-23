<template>
  <div>
    <img :src="card.posterpath" alt="#" style="width: 150px; height: 200px;" @click="cardStat">
  </div>
</template>

<script>
export default {
  name: 'MyCard',
  props: {
    card: Object,
  },
  methods: {
    cardStat() {
      const cardHP = this.card.hp
      const cardAD = this.card.attackdamage
      alert(`공격력 : ${cardAD}  생명력 : ${cardHP}`)
    }
  }
}
</script>

<style>

</style>