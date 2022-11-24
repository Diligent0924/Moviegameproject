<template>
  <div class="my-5">
    <h2>
      추가 카드를 획득하거나, 사용하지 않는 카드를 삭제하세요. (남은 기회 : {{ coinLeft }}번)
    </h2>
    <b-button :class="{disabled : coinLeft}" variant="outline-primary" @click="nextStage">다음 스테이지로</b-button>
    <hr>
    <div>
      <CoinAddCard :coinLeft="coinLeft" @coin-minus="coinMinus" :isOpened="isOpened" @picking="picking" @opening="opening" />
    </div> 
    <hr class="border border-dark border-1 opacity-75">
    <div style="display: flex;" class="mt-5">
      <CoinDeleteCard @coinMinus="coinMinus" :coinLeft="coinLeft" :isOpened="isOpened" />
    </div>
  </div>
</template>

<script>
import CoinAddCard from '@/components/CoinAddCard'
import CoinDeleteCard from '@/components/CoinDeleteCard'


export default {
  name: 'CoinAreaView',
  components: {
    CoinAddCard,
    CoinDeleteCard,
  },
  data() {
    return {
      coinLeft: 4,
      isOpened: false,
    }
  },
  methods: {
    coinMinus() {
      this.coinLeft--
    },
    picking() {
      this.isOpened = false
      this.$store.dispatch('resetRandomCard')
    },
    opening() {
      this.isOpened = true
    },
    nextStage() {
      this.$store.dispatch('canGoChange')
      this.$router.push({ name: 'playing' })
      this.$store.dispatch('resetRandomCard')
      this.$store.dispatch('canGoChange')
    }
  },
}
</script>

<style>

</style>