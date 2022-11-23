<template>
  <div class="my-5">
    <div class="fixed-bottom my-5">
      <b-container class="bv-example-row">
        <b-row class="text-center">
          <b-col>1 of 3</b-col>
          <b-col cols="8"></b-col>
          <b-col>
            (남은 기회 : {{ coinLeft }}번) 
            <b-button :class="{disabled : coinLeft}" variant="outline-primary" @click="nextStage">다음 스테이지로</b-button>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <h2>
      추가 카드를 획득하거나, 사용하지 않는 카드를 삭제하세요. (남은 기회 : {{ coinLeft }}번)
    </h2>
    <b-button :class="{disabled : coinLeft}" variant="outline-primary" @click="nextStage">다음 스테이지로</b-button>
    <hr>
    <div>
      <CoinAddCard :coinLeft="coinLeft" @coin-minus="coinMinus" :isOpened="isOpened" @picking="picking" @opening="opening" />
    </div>
    <hr class="border border-dark border-3 opacity-75">
    <div style="display: flex;">
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