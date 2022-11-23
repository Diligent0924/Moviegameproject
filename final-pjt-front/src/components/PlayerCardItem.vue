<template>
  <div >
    <b-card bg-variant="primary" text-variant="white" class="text-center" @click="playCard" style="width:250px;">
      <b-card-text>{{ name }}</b-card-text>
      <img :src="card.posterpath" alt="" style="width: 160px; height: 150px;">
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
  },
  computed: {
    name() {
      return this.card.name.length > 15 ? this.card.name.slice(0,20) : this.card.name
    }
  }
}
</script>

<style>

</style>