<template>
  <div :style="{ backgroundImage: 'linear-gradient(rgba(31.5, 31.5, 52.5, 1) 0px, rgba(40.5, 35.5, 60.5, 0.84) -300%), url(' + backdroppath + ')', backgroundSize: 'cover', height:'1000px', marginLeft:0,}">
    <b-container class="bv-example-row" style="color:white">
      <b-row style="height:1000px" align-v="center">
        <b-col sm="4"><img :src="posterpath" alt=""></b-col>
        <b-col sm="8" class="text-start">
          <b-row>
            <h1>{{movie.title}}</h1>
          </b-row>
          <b-row style="display: flex;">
            <p>
              <span>개봉일자 : {{movie.release_date}}</span> &nbsp; &nbsp; &nbsp; 장르 :
              <span v-for="(genre, index) in genres" :key="index">{{genre}} &nbsp;</span>
            </p>
            <p>평점 : {{vote_average}}</p>
          </b-row>
          <b-row>
            <p>{{overview}}</p>
          </b-row>
          <b-row>
            <a :href="`https://www.themoviedb.org/movie/${movie.id}?language=ko`">
              <b-button variant="outline-primary">
                추가적인 영화정보를 얻고 싶다면 눌러보세요!
              </b-button>
              </a>
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
    },
    vote_average(){
      return this.movie.vote_average === 0 ?  "이 영화는 개봉예정작이므로 평점이 없습니다.": this.movie.vote_average
    },
    overview(){
      return this.movie.overview.length === 0 ? "이 영화는 안타깝게도 개요가 없습니다.." : this.movie.overview
    }
  }
}
</script>

<style>
</style>