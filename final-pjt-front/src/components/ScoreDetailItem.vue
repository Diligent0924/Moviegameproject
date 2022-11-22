<template>
  <div>
    <div style="height:50px;"><p>{{card.name}}</p></div>
    <div><img :src="card.posterpath" alt=""></div>
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