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
      this.$router.push({ name: 'start' })
    }
  }
}
</script>

<style>

</style>