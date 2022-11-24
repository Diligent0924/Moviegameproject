<template>
  <div @click="deleteCard">
    <p v-if="IsSkill" class="text-warning">{{ card.name }}</p>
    <p v-else>{{ card.name }}</p>
    <img :src="card.posterpath" alt="#" style="width: 150px; height: 200px;">
    <p v-if="IsSkill" class="text-center text-warning fw-bold">스킬 카드</p>
    <p v-else class="fw-bold"><span class="text-danger">AD : {{ card.attackdamage }}</span> &nbsp;&nbsp; <span class="text-success">HP : {{ card.hp }}</span></p>
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
  computed: {
    cardNum() {
      return this.$store.state.userCards.length
    },
    IsSkill(){
      return this.card.hp === 0 ? true : false 
    }
  },
  methods: {
    deleteCard() {
      if (this.isOpened) {
        alert('오픈된 카드 중 한장을 먼저 선택하세요.')
      } else if (this.cardNum <= 5) {
        alert('카드의 최소 장수는 5장입니다!')
      } else if (this.coinLeft > 0) {
        this.$store.dispatch('deleteCard', this.card)
        this.$emit('coinMinus')
      } else {
        alert('이미 4번의 기회를 모두 사용하셨습니다.')
      }
    }
  },
}
</script>

<style>

</style>