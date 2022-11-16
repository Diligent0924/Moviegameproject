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

export default {
  name: 'ScoreBoardView',
  components: {
    ScoreBoardItem
  },
}
</script>

<style>

</style>