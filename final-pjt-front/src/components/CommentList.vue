<template>
  <div>
    <b-list-group v-if="comments.length">
      <b-list-group-item>
        <b-row class="text-center">
          <b-col cols="2" class="ms-2">작성자</b-col>
          <b-col cols="7" style="text-start">내용</b-col>
          <b-col cols="2">생성일자</b-col>
        </b-row>
        <hr>
        <CommentItem v-for="(comment, index) in comments" :key="`${comment}${index}`" :comment="comment" />
      </b-list-group-item>
    </b-list-group>
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