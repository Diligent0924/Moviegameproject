<template>
  <div @click="goToDetail">
    <span>{{ score.user }} | {{ score.title }} | {{ score.stage }}</span>
    <hr>
  </div>
</template>

<script>


export default {
  name: 'ScoreBoardItem',
  props: {
    score: Object,
  },
  methods: {
    goToDetail() {
      this.$router.push({ name: 'scoredetail', params: {'id': this.score.id} })
    }
  }
}
</script>

<style>

</style>