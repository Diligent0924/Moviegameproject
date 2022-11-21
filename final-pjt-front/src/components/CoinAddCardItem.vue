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
  name: 'CoinAddCardItem',
  props: {
  card: Object,
  coinLeft: Number,
  isOpened: Boolean,
 },
 computed: {
  skillType() {
    if (this.card.skilltype) {
      return this.card.skilltype
      } else {
      return '스킬이 없음'
      }
    }
  },
  methods: {
  pickCard() {
    if (this.coinLeft < 0) {
      alert('이미 4번의 기회를 모두 사용하였습니다')
    } else if (this.isOpened) {
        this.$store.dispatch('pickCard', this.card)
        this.$emit('picking')
    } else {
      alert('카드 오픈 버튼을 눌러주세요.')
    }
    }
  },
}
</script>

<style>

</style>