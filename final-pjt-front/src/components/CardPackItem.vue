<template>
  <div>
    <p style="color: crimson;"><b>{{ card.name }}</b></p>
    <img :src="card.posterpath" alt="#" @click="pickCard">
    <p>공격력 : {{ card.attackdamage }}</p>
    <p>생명력 : {{ card.hp }}</p>
    <p>특수 능력 : {{ skillType }}</p>
  </div>
</template>

<script>
export default {
  name: 'CardPackItem',
  props: {
    card: Object,
    coinLeft: Number,
  },
  computed: {
    skillType() {
      if (this.card.skilltype) {
        return this.card.skilltype
      } else {
        return '스킬이 없음'
      }
    },
    cardNum() {
      return this.$store.getters.cardNum
    }
   },
   methods: {
    pickCard() {
      if (this.coinLeft < 1) {
        alert('이미 4번의 기회를 모두 사용하였습니다')
      } else {
          this.$store.dispatch('pickCard', this.card)
       
          if (this.cardNum < 10) {
            this.$store.dispatch('openCard')
          }
        }
      }
    },
}
</script>

<style>
  img {
    width: 300px;
    height: 400px;
  }
</style>