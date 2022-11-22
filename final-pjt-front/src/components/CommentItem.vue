<template>
  <div>
    <p>
      {{ comment.id }} : {{comment.content}}
    </p>
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>