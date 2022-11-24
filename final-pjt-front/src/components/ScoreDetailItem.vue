<template>
  <div @click="movieDetail">
    <img :src="card.posterpath" alt="">
  </div>
</template>

<script>
export default {
  name: 'ScoreDetailItem',
  props: {
    card: Object,
  },
  methods: {
    movieDetail() {
      this.$router.push({ name: 'invendetail', params: {movieid: this.card.movie_id} })
    }
  },
} 
</script>

<style>

</style>