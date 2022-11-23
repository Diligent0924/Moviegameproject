<template>
  <div>
    <p style="border-bottom:20px" :class="{'unique-card-color' : isUnique }" ><b>{{ card.name }}</b></p>
    <img :src="card.posterpath" alt="#" @click="pickCard" style="width: 80%; height: 80%;">
    <hr>
    <p v-if="!isSepll" class="text-danger"><b> AD : {{ card.attackdamage }} </b></p>
    <p class="text-success"><b>{{ hp }}</b></p>
    <p v-if="isUnique" class="text-primary"><b>{{ skillType }}</b></p>
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
      return this.card.skilltype ? this.card.skillcomment : 'Not Found'
    },
    cardNum() {
      return this.$store.getters.cardNum
    },
    hp() {
      return this.card.hp ? `HP : ${this.card.hp}` : '주문 카드'
    },
    isSepll() {
      return this.hp === '주문 카드' ? true : false
    },
    isUnique() {
      return this.card.movietype === 'unique' ? true : false
    },
  },
  methods: {
    pickCard() {
      if (!this.isOpened && this.coinLeft) {
        this.$store.dispatch('openCard')
        this.$emit('coin-minus')
        this.$emit('opening')
      } else if (this.coinLeft < 0) {
        alert('이미 4번의 기회를 모두 사용하였습니다')
      } else if (this.coinLeft === 0 && !this.isOpened) {
        alert('이미 4번의 기회를 모두 사용하였습니다')
      } else if (this.isOpened) {
        this.$store.dispatch('pickCard', this.card)
        this.$emit('picking')
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
  .unique-card-color {
    color: gold;
  }
</style>