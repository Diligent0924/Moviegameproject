<template>
  <div style="margin-left:20%; margin-right:20%;">
    <h1>
      Score Board
    </h1>
    <hr>
    <b-list-group>
    <ScoreBoardItem v-for="(score, index) in scores" :key="index" :score="score" />
    </b-list-group>
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