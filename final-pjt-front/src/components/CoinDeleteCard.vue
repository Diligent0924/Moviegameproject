<template>
  <div>
    <h3>카드 삭제</h3>
    <div style="display: flex;">
      <CoinDeleteCardItem v-for="(card, index) in cards" :key="index" :card="card" @coinMinus="coinMinus" :coinLeft="coinLeft" :isOpened="isOpened" />    
    </div>
  </div>
</template>

<script>
import CoinDeleteCardItem from './CoinDeleteCardItem';

export default {
  name: 'CoinDeleteCard',
  components: {
    CoinDeleteCardItem,
  },
  computed: {
    cards() {
      return this.$store.state.userCards
    }
  },
  methods: {
    coinMinus() {
      this.$emit('coinMinus')
    }
  },
  props: {
    coinLeft: Number,
    isOpened: Boolean,
  }
}
</script>

<style>

</style>