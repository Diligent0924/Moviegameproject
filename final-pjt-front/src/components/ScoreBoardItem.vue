<template>
  <div @click="goToDetail">
    <b-list-group-item class="rounded">
      <b-container class="bv-example-row">
        <b-row>
          <b-col> 등수</b-col>
          <b-col>{{ score.user }}</b-col>
          <b-col cols="8">{{ score.title }}</b-col>
          <b-col>{{ score.stage }}</b-col>
        </b-row>
      </b-container>
    </b-list-group-item>
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