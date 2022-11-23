<template>
  <div @click="movieDetail">
  <b-card
    :img-src="posterpath"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem; height: 25rem;"
    class="mb-2"
  >
    <!-- <b-card-text>
      {{ movie.tagline }}
    </b-card-text> -->
  </b-card>
</div>
</template>

<script>
export default {
  name: 'InvenItem',
  props: {
    movie: Object,
  },
  computed: {
    posterpath() {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    }
  },
  methods: {
    movieDetail() {
      this.$router.push({ name: 'invendetail', params: { movieid: this.movie.id } })
    }
  }
}
</script>

<style>

</style>