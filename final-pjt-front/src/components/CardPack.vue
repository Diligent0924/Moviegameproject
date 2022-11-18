<template>
  <div>
    <h3>
      카드 팩 까는 곳
    </h3>
    <div style="display: flex;">
      <CardPackItem
        v-for="(card, index) in cards"
        :key="`${index}-${card}`"
        :card=card
        style="margin-left: 20px; margin-right: 20px;"
      />
    </div>
    <b-button variant="outline-primary" @click="openCard">카드 오픈!</b-button>
  </div>
</template>

<script>
import CardPackItem from '@/components/CardPackItem'
import axios from 'axios'

export default {
  name: 'CardPack',
  data() {
    return {
      count: 0,
      cards: ['1번카드', '2번카드', '3번카드']
    }
  },
  components: {
    CardPackItem
  },
  methods: {
    openCard() {
      const API_URL = 'http://127.0.0.1:8000'
      this.count++
      this.$emit('count-up', this.count)

      axios({
        method: 'get',
        url: `${API_URL}/moviecards/plus/`
      })
        .then(res => {
          console.log(res)
          let temp = [res.data[0].name, res.data[1].name, res.data[2].name]
          this.cards = temp
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>