<template>
  <div >
    <h3>Lv.{{bossLevel+1}} {{boss.name}}</h3>
    <img :src="boss.posterpath" alt="" style="width: 200px; height: 200px;" @click="attackTo" :class="{ 'in-attack' : inAttack }">
    <p ><b><span style="color:red">AD {{boss.attackdamage}}</span> <span style="color:green;">HP {{boss.hp}}</span></b></p>
    <!-- <div style="display: flex; justify-content: center;">
      <BossCardItem
        v-for="(card, index) in cards"
        :key="`${index}-${card}-inbossarea`"
        :card=card
      /> -->
    <!-- </div> -->
  </div>
</template>

<script>
// import BossCardItem from '@/components/BossCardItem'

export default {
  name: 'BossArea',
  // components: {
  //     BossCardItem
  // },
  data() {
    return {
      cards: ['card1', 'card2', 'card3', 'card4', 'card5'],
    }
  },
  props: {
    boss: Object,
    bossLevel: Number,
    inAttack: Boolean,
  },
  methods: {
    attackTo() {
      if (this.inAttack) {
        this.$emit('attackTo', this.boss)
      } else {
        alert('공격을 수행할 카드를 먼저 선택하세요.')
      }
    }
  }
}
</script>

<style>
  .in-attack {
    border: 3px solid red;
  }
</style>