<template>
  <div>
    <h3>댓글 작성</h3>
    <form @submit.prevent="commentCreate">
      <input type="text" v-model.trim="comment">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
export default {
  name: 'CommentCreate',
  data() {
    return {
      comment: null
    }
  },
  methods: {
    commentCreate() {
      if (this.comment) {
        const content = this.comment
        const boardId = this.$route.params.id
        const payload = {
          content, boardId
        }

        this.$store.dispatch('commentCreate', payload)
        this.comment = null
        this.$emit('add-comment')

      } else {
        alert('빈 댓글은 등록할 수 없습니다')
      }
    }
  }
}
</script>

<style>

</style>