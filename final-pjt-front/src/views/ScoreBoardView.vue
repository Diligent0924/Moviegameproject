<template>
  <div>
    <h1>
      스코어 보드
    </h1>
    <hr>
    <ScoreBoardItem v-for="(score, index) in scores" :key="index" :score="score" />

  </div>
</template>

<script>
import ScoreBoardItem from '@/components/ScoreBoardItem';
// import axios from 'axios';

export default {
  name: 'ScoreBoardView',
  components: {
    ScoreBoardItem
  },
  methods: {
    getScoreBoard() {
      this.$store.dispatch('getScoreBoard')
    }
  },
  created() {
    this.getScoreBoard()
  },
  computed: {
    scores() {
      return this.$store.state.scores;
    }
  }
}
</script>

<style>

</style>