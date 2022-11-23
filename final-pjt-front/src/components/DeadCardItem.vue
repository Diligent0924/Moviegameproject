<template>
  <div>
    <!-- <p>{{ name }}</p> -->
    <img :src="card.posterpath" alt="#" style="width: 100px; height: 100px;">
  </div>
</template>

<script>

export default {
  name: 'DeadCardItem',
  props: {
    card: Object,
  },
  computed: {
    name() {
      return this.card.name.length > 15 ? this.card.name.slice(0,20) : this.card.name
    }
  }
}

</script>

<style>

</style>