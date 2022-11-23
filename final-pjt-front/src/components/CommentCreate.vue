<template>
  <div>
    <form @submit.prevent="commentCreate" class="form-floating">
      <b-container class="bv-example-row">
        <b-row class="text-center">
          <b-col cols="9">
            <input type="text" v-model.trim="comment" class="form-control" placeholder="Leave a comment here" id="floatingTextarea">
          </b-col>
          <b-col>
            <button type="submit" class="btn btn-outline-success">작성하기</button>
          </b-col>
        </b-row>
      </b-container>
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