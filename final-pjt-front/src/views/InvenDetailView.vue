<template>
  <div>
    <h2>{{movie.title}} </h2>
    <img :src="posterpath" alt="">
    <p>{{movie.tagline}}</p>
    <hr>
    <h3>평점 : {{movie.vote_average}} </h3>
    <h3>장르 : {{genres}} </h3>
    <br>
    <p>{{movie.overview}}</p>
  </div>
</template>

<script>
export default {
  name: 'InvenDetailView',
  created() {
    this.$store.dispatch('getInvenDetail', this.$route.params.movieid)
  },
  computed: {
    movie() {
      return this.$store.state.invenDetail[0]
    },
    genres() {
      const gen = []
      this.movie.genres.forEach((genre) => {
        gen.push(genre.name)
      })
      return gen
    },
    posterpath() {
      return 'https://image.tmdb.org/t/p/w500'+this.movie.poster_path
    }
  }
}
</script>

<style>

</style>