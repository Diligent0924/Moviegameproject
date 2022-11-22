<template>
  <div>
    <p>
      {{ comment.user }} : {{comment.content}}
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