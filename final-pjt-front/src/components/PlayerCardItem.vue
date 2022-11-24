<template>
  <div>
    <b-card border-variant="info" class="text-center" @click="playCard" style="width:250px;">
      <b-card-text v-if="isnormal">{{ name }}</b-card-text>
      <b-card-text v-else class="text-warning">{{ name }}</b-card-text>
      <img :src="card.posterpath" alt="" style="width: 160px; height: 150px;">
      <div style="height:60px;">
        <b-card-text v-if="isnormal" class="text-danger fw-bold">AD : {{card.attackdamage}} &nbsp; &nbsp; &nbsp;<span class="text-success"> HP : {{card.hp}}</span></b-card-text>
        <p class="text-primary fw-bold">{{card.skilldescription}}</p>
      </div>
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
      return this.card.name.length > 15 ? this.card.name.slice(0,15) : this.card.name
    },
    isnormal() {
      return this.card.movietype === 'normal' ? true : false
    },
  }
}
</script>

<style>

</style>