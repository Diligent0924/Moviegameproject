<template>
  <div>
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col cols="2">{{ comment.user }}</b-col>
        <b-col cols="8" class="text-start">{{comment.content}}</b-col>
        <b-col cols="2">{{created_at}}</b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: {
    comment: Object,
  },
  computed: {
    created_at(){
      return this.comment.created_at.split("T")[0]
    }
  }
}
</script>

<style>

</style>