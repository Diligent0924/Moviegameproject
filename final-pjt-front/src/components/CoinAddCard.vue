<template>
  <div>
    <h1 class="my-5 text-success">
      카드 추가
    </h1>
    <div style="display: flex;" class="justify-content-center">
      <CoinAddCardItem
        v-for="(card, index) in cards"
        :key="`${index}--${card}`"
        :card=card :coinLeft="coinLeft"
        style="margin-left: 20px; margin-right: 20px;"
        @picking="picking" :isOpened="isOpened"
        @coin-minus="coinMinus" @opening="opening"
      />
    </div>
  </div>
</template>

<script>
import CoinAddCardItem from '@/components/CoinAddCardItem'

export default {
  name: 'CoinAddCard',
  props: {
    coinLeft: Number,
    isOpened: Boolean,
  },
  components: {
    CoinAddCardItem,
  },
  methods: { 
    coinMinus() {
      this.$emit('coin-minus')
    },
    opening() {
      this.$emit('opening')
    },
    picking() {
      this.$emit('picking')
    }
  },
  computed: {
    cards() {
      return this.$store.state.randomCards
    }
  }
}
</script>

<style>

</style>