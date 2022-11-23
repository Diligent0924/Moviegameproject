<template>
  <div>
  <b-card
    :title="movie.title"
    :img-src="posterpath"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem; height: 40rem;"
    class="mb-2"
  >
    <!-- <b-card-text>
      {{ movie.tagline }}
    </b-card-text> -->
  <hr>
  <b-button href="#" variant="primary" @click="movieDetail">자세히보기</b-button>
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