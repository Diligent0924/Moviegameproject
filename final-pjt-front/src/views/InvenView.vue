<template>
  <div>
    <h1>
      영화 추천 페이지
    </h1>
    <button @click="gameStart">gameStart</button>
    <InvenItem v-for="movie in movies" :key="`${movie.id}`" :movie="movie" />    
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
    }
  },
  computed: {
    isLogined() {
      if (this.$store.state.token) {
        return true
      } else {
        return false
      }
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

</style>