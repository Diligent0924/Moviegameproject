<template>
  <div>
    <img :src="card.posterpath" alt="">
  </div>
</template>

<script>
export default {
  name: 'CreateArticleItem',
  props: {
    card: Object,
  },
} 
</script>

<style>

</style>