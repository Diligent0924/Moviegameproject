<template>
  <div>
    <h3>
      댓글 폼
    </h3>
    <CommentItem/>
    <CommentItem/>
    <CommentItem/>
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem'

export default {
  name: 'CommentList',
  components: {
    CommentItem
  }
}
</script>

<style>

</style>