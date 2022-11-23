<template>
  <div :style="{ backgroundImage: 'linear-gradient(to right, rgba(31.5, 31.5, 52.5, 1) 150px, rgba(31.5, 31.5, 52.5, 0.84) 100%), url(' + backdroppath + ')', backgroundSize: 'cover', height:'1000px', }">
    <b-container class="bv-example-row" style="color:white">
      <b-row>
        <b-col sm="4"><img :src="posterpath" alt=""></b-col>
        <b-col sm="8">
          <b-row>
            {{movie.title}}
          </b-row>
          <b-row>
            {{movie.tagline}}
          </b-row>
          <b-row>
            평점 : {{movie.vote_average}}
          </b-row>
          <b-row>
            장르 : {{genres}}
          </b-row>
          <b-row>
            장르 : {{movie.overview}}
          </b-row>
        </b-col>
      </b-row>
    </b-container>
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
    },
    backdroppath() {
      return 'https://image.tmdb.org/t/p/original'+this.movie.backdrop_path
    }
  }
}
</script>

<style>
</style>