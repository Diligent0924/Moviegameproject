<template>
  <div>
    <p>{{ card.name }}</p>
    <img :src="card.posterpath" alt="#" style="width: 150px; height: 200px;">
  </div>
</template>

<script>

export default {
  name: 'DeadCardItem',
  props: {
    card: Object,
  }
}

</script>

<style>

</style>