<template>
  <div class="my-5">
    <h2>
      탐험을 위한 최초의 덱을 구성하세요! 
      <b-button :class="{disabled : cardNum < 10}" block variant="outline-danger" @click="goToDengeon">탐험 시작!</b-button>
    </h2>
    <h3 class="text-cenrer text-danger">이 카드게임은 가챠게임으로 오늘 하루 기분이 좋고 싶으신 분은 뒤로가기를 눌러주세요.</h3>
    <hr>
    <b-container class="bv-example-row">
      <b-row class="text-center" style="height:700px;">
        <b-col cols="8">
          <CardPack @count-up="countUpdate" />
        </b-col>
        <b-col>
          <MyDeck/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import CardPack from '@/components/CardPack'
import MyDeck from '@/components/MyDeck'


export default {
  name: 'FirstDeckView',
  components: {
    CardPack,
    MyDeck
  },
  methods: {
    goToDengeon () {
      this.$store.dispatch('canGoChange')
      this.$router.push({
        name: 'playing'
      })
      this.$store.dispatch('resetRandomCard')
      this.$store.dispatch('canGoChange')
    },
    countUpdate (newCount) {
      this.count = newCount
    },
  },
  computed: {
    cardNum() {
      return this.$store.getters.cardNum
    }
  }
}
</script>

<style>
  .downside {
    margin-top: 10px; 
  }
</style>