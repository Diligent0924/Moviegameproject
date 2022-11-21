<template>
  <div>
    <p>{{card.name}}</p>
    <img :src="card.posterpath" alt="">
  </div>
</template>

<script>
export default {
  name: 'ScoreDetailItem',
  props: {
    card: Object,
  }
} 
</script>

<style>

</style>