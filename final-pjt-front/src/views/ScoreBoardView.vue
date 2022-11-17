<template>
  <div>
    <h1>
      스코어 보드 전체
    </h1>
    <ScoreBoardItem/>
    <hr>
    <ScoreBoardItem/>
    <hr>
    <ScoreBoardItem/>
    <hr>
    <ScoreBoardItem/>
    <hr>
    <ScoreBoardItem/>

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
  // methods: {
  //   getScoreBoard() {
  //     axios({
  //       methods: 'post',
  //       url: 'https://www.google.com/'
  //     })
  //       .then(response => {
  //         console.log(response.data);
  //       })
  //       .catch(error => {
  //         console.log(error);
  //       });
  //   }
  // },
  // created() {
  //   this.getScoreBoard()
  // },
  computed: {
    scores() {
      return this.$store.state.scores;
    }
  }
}
</script>

<style>

</style>