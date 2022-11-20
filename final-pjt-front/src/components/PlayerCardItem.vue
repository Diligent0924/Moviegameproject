<template>
  <div >
    <b-card bg-variant="primary" text-variant="white" class="text-center" @click="playCard">
      <b-card-text>{{ card.name }}</b-card-text>
      <img :src="card.posterpath" alt="" style="width: 80px; height: 120px;">
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'PlayerCardItem',
  props: {
    card: Object,
  },
  methods: {
    playCard() {
      this.$emit('playCard', this.card)
    }
  }
}
</script>

<style>

</style>