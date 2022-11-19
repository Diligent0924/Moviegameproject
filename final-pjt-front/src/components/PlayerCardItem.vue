<template>
  <div>
    <b-card bg-variant="primary" text-variant="white" header="Player" class="text-center">
      <b-card-text>{{ card.name }}</b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
name: 'PlayerCardItem',
props: {
  card: Object,
}
}
</script>

<style>

</style>