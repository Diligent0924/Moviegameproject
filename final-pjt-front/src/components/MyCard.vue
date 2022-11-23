<template>
  <b-list-group-item>
  <b-container class="bv-example-row">
    <b-row class="text-start bg-primary border border-dark rounded" v-if="card.movietype==='unique'">
      <b-col cols="2">{{card.movietype}}</b-col>
      <b-col cols="5">{{card.name}}</b-col>
      <b-col cols="2" v-if="card.hp">Minion</b-col>
      <b-col cols="4" v-else>Skill</b-col>
      <b-col cols="1" v-if="card.hp">{{card.attackdamage}}</b-col>
      <b-col cols="1" v-if="card.hp">{{card.hp}}</b-col>
    </b-row>
    
    <b-row class="text-start rounded border border-dark" v-else>
      <b-col cols="2">{{card.movietype}}</b-col>
      <b-col cols="5">{{card.name}}</b-col>
      <b-col cols="2">Minion</b-col>
      <b-col cols="1">{{card.attackdamage}}</b-col>
      <b-col cols="1">{{card.hp}}</b-col>
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
      if (this.card.movietype === 'unique') {
        const skillComment = this.card.skillcomment
        if (!this.card.hp) {
          alert(`주문\n특수 효과 : ${skillComment}`)
        } else {
          const cardHP = this.card.hp
          const cardAD = this.card.attackdamage
          alert(`희귀카드\n공격력 : ${cardAD} 생명력 : ${cardHP}\n특수 효과 : ${skillComment}`)
        }
      } else {
        const cardHP = this.card.hp
        const cardAD = this.card.attackdamage
        alert(`일반 카드\n공격력 : ${cardAD}  생명력 : ${cardHP}`)
      }
    }
  }
}
</script>

<style>

</style>