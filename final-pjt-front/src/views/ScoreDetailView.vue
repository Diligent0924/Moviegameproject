<template>
  <div>
    <h2>
      스코어보드 디테일 페이지
    </h2>
    <p>사용 덱</p>
    <p>카드 카드 카드 카드</p>
    <p>카드 카드 카드 카드</p>
    <hr>
    <h3>스테이지</h3>
    <hr>
    <p>글</p>
    <p>글</p>
    <p>글</p>
    <p>글</p>
    <hr>
    <br>
    <CommentList/>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'

export default {
  name: 'ScoreDetailView',
  components: {
    CommentList
  },
}
</script>

<style>

</style>