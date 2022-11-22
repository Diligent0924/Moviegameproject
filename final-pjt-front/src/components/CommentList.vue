<template>
  <div>
    <h3>
      댓글 폼
    </h3>
    <CommentItem v-for="(comment, index) in comments" :key="`${comment}${index}`" :comment="comment" />
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem'

export default {
  name: 'CommentList',
  components: {
    CommentItem
  },
  props: {
    comments: Array,
  }
}
</script>

<style>

</style>