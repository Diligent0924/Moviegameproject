<template>
  <div>
    <h2>
      최초 덱 구성 페이지
    </h2>
    <hr>
    <div style="float: left; margin-left: 100px;">
      <CardPack @count-up="countUpdate" />
    </div>
    <div style="float: right; margin-right: 350px;">
      <MyDeck/>
    </div>
    <div>
      <b-button :class="{disabled : cardNum < 10}" block variant="danger" @click="goToDengeon">탐험 시작!</b-button>
    </div>
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
      this.$router.push({
        name: 'playing'
      })
      this.$store.dispatch('resetRandomCard')
    },
    countUpdate (newCount) {
      this.count = newCount
    },
    createDeckList() {
      this.$store.dispatch('createDeckList')
    }
  },
  computed: {
    cardNum() {
      return this.$store.getters.cardNum
    }
  },
  created() {
    this.createDeckList()
  },
}
</script>

<style>
  .downside {
    margin-top: 10px; 
  }
</style>