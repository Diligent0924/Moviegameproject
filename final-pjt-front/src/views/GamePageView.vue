<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'GamePageView',
  created() {
    this.$store.dispatch('createDeckList')
  }
}
</script>

<style>

</style>