<template>
  <div>
    <h2>
      처음 시작 덱 만드는 페이지
    </h2>
    <hr>
    <div style="float: left; margin-left: 300px;">
      <CardPack/>
    </div>
    <div style="float: right; margin-right: 400px;">
      <MyDeck/>
    </div>
    <button class="downsides" @click="goToDengeon">탐험 시작!</button>
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
    }
  }
}
</script>

<style>
  .downsides {
    position: fixed;
    bottom: 60px;
  }
</style>