<template>
  <div class="mx-5 mt-4">
    <p id="name"><b id="h">영화 게임 기반 추천 페이지</b>
    (만약 추천 알고리즘에 보고 싶은 영화가 없다면 눌러보세요! <b-button pill variant="outline-danger" @click="gameStart">추천받기!</b-button>)</p>
    <div class="mt-5" v-if="!movies.length">
      <h1>
        추천 영화가 없다면, 상단의 추천받기 버튼을 눌러보세요!
      </h1>
    </div>
    <div v-else class="row row-cols-1 row-cols-md-4 g-4">
      <InvenItem v-for="movie in movies" :key="`${movie.id}`" :movie="movie" />  
    </div>
  </div>
</template>

<script>
import InvenItem from '@/components/InvenItem'

export default {
  name: 'InvenView',
  components: {
      InvenItem
  },
  methods: {
    gameStart() {
      if (this.isLogined) {
        this.$router.push({ name: 'start' })
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
      this.$store.dispatch('canGoChange')
    },
  },
  computed: {
    isLogined() {
      return this.$store.state.token ? true : false
    },
    movies() {
      return this.$store.state.inven
    }
  },
  created() {
    this.$store.dispatch('getInven')
  }
}
</script>

<style>
#name{
  color: aliceblue;
  text-align: left;
  font-size: 20px;
}

#h{
  font-size: 40px;
}

</style>