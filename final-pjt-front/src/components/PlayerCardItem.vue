<template>
  <div>
    <b-card bg-variant="primary" text-variant="white" header="Player" class="text-center">
      <b-card-text>{{ card }}</b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
name: 'PlayerCardItem',
props: {
  card: String,
}
}
</script>

<style>

</style>