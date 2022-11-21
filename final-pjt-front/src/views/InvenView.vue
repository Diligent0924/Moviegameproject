<template>
  <div>
    <h1>
      InvenView
    </h1>
    <button @click="gameStart">gameStart</button>
    
  </div>
</template>

<script>
export default {
  name: 'InvenView',
  methods: {
    gameStart() {
      if (this.isLogined) {
        this.$router.push({ name: 'start' })
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  },
  computed: {
    isLogined() {
      if (this.$store.state.token) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style>

</style>