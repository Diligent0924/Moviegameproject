<template>
  <div>
    <div style="display: flex;">
      <CardPackItem
        v-for="(card, index) in cards"
        :key="`${index}-${card}`"
        :card=card
        style="margin-left: 20px; margin-right: 20px;"
        :firstClick="firstClick" @afterFirst="afterFirst"
      />
    </div>
  </div>
</template>

<script>
import CardPackItem from '@/components/CardPackItem'

export default {
  name: 'CardPack',
  components: {
    CardPackItem
  },
  computed: {
    cards() {
      return this.$store.state.randomCards
    },
  },
  data() {
    return {
      firstClick: true,
    }
  },
  methods: {
    afterFirst() {
      this.firstClick = false
    }
  }
}
</script>

<style>

</style>