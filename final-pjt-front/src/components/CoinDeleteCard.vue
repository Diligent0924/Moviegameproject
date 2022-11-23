<template>
  <div>
    <h1 class="text-danger my-5">카드 삭제</h1>
    <div class="row row-cols-1 row-cols-md-6 g-4">
      <CoinDeleteCardItem v-for="(card, index) in cards" :key="index" :card="card" @coinMinus="coinMinus" :coinLeft="coinLeft" :isOpened="isOpened" />    
    </div>
    <div style="display: flex;">
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