<template>
  <div>
    <h3>
      카드 추가
    </h3>
    <div style="display: flex;">
      <CoinAddCardItem
        v-for="(card, index) in cards"
        :key="`${index}--${card}`"
        :card=card :coinLeft="coinLeft"
        style="margin-left: 20px; margin-right: 20px;"
        @picking="picking" :isOpened="isOpened"
      />
    </div>
    <b-button :class="{disabled : coinLeft < 1 || isOpened}" variant="outline-primary" @click="openCard">카드 오픈!</b-button>
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
    openCard() {
      if (this.isOpened) {
        alert('오픈된 카드 중 한장을 먼저 선택하세요!')
      } else {
        this.$store.dispatch('openCard')
        this.$emit('coin-minus')
        this.$emit('opening')
      }
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