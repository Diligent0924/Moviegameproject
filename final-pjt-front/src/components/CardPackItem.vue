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
      if (this.cardNum >= 10) {
        alert('이미 10장의 카드를 선택하였습니다.')
      } else if (this.card.name === '카드명') {
        alert('카드 오픈 버튼을 눌러주세요.')
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