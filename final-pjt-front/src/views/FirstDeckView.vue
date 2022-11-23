<template>
  <div>
    <h2>
      탐험을 위한 최초의 덱을 구성하세요!
    </h2>
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

      <b-row>
        <b-col>
          <b-button :class="{disabled : cardNum < 10}" block variant="danger" @click="goToDengeon">탐험 시작!</b-button>
        </b-col>
      </b-row>
    </b-container>
    <!-- <div style="float: left; margin-left: 100px;">
      <CardPack @count-up="countUpdate" />
    </div>
    <div style="float: right; margin-right: 350px;">
      <MyDeck/>
    </div> -->
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