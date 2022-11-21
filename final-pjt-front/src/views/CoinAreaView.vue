<template>
  <div>
    <h2>
      추가 카드를 획득하거나, 사용하지 않는 카드를 삭제하세요.
    </h2>
    <b-button :class="{disabled : coinLeft}" variant="outline-primary" @click="nextStage">다음 스테이지로</b-button>
    <hr>
    <p>남은 기회 : {{ coinLeft }}번</p>
    <div>
      <CoinAddCard :coinLeft="coinLeft" @coin-minus="coinMinus" :isOpened="isOpened" @picking="picking" @opening="opening" />
    </div>
    <div style="display: flex; margin-top: 200px;">
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
    },
    opening() {
      this.isOpened = true
    },
    nextStage() {
      this.$router.push({ name: 'playing' })
    }
  },
}
</script>

<style>

</style>