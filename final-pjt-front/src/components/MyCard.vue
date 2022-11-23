<template>
  <b-list-group-item>
  <b-container class="bv-example-row">
    <b-row class="text-start bg-primary border border-dark rounded" v-if="card.movietype==='unique'">
      <b-col>{{card.movietype}}</b-col>
      <b-col cols="6">{{card.name}}</b-col>
      <b-col v-if="card.hp">Minion</b-col>
      <b-col v-else>Skill</b-col>
    </b-row>
    
    <b-row class="text-start rounded border border-dark" v-else>
      <b-col>{{card.movietype}}</b-col>
      <b-col cols="6">{{card.name}}</b-col>
      <b-col>Minion</b-col>
    </b-row>
  </b-container>
  </b-list-group-item>
  <!-- <div>
    <p>{{card}}</p>
    <p>{{card.name}}</p>
    <p>{{card.hp}}</p>
    <p v-if="card.hp">sss</p>
    <p v-else>스킬</p>
    <img :src="card.posterpath" alt="#" style="width: 150px; height: 200px;" @click="cardStat">
  </div> -->
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