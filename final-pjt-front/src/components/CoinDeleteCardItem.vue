<template>
  <div @click="deleteCard">
    <p>{{ card.name }}</p>
    <img :src="card.posterpath" alt="#" style="width: 150px; height: 200px;">
    <b><p><span>공격력 : {{ card.attackdamage }}</span> / <span>생명력 : {{ card.hp }}</span></p></b>
  </div>
</template>

<script>
export default {
  name: 'CoinDeleteCardItem',
  props: {
    card: Object,
    coinLeft: Number,
    isOpened: Boolean,
  },
  methods: {
    deleteCard() {
      if (this.isOpened) {
        alert('오픈된 카드 중 한장을 먼저 선택하세요.')
      } else if (this.coinLeft > 0) {
          this.$store.dispatch('deleteCard', this.card)
          this.$emit('coinMinus')
      } else {
          alert('이미 4번의 기회를 모두 사용하셨습니다.')
      }
    }
  }
}
</script>

<style>

</style>