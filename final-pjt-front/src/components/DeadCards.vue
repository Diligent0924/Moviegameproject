<template>
  <div>
    <h3>
      묘지
    </h3>
    <div style="display: flex;">
      <DeadCardItem v-for="(card, index) in deadCards" :key="index" :card="card" />
    </div>
  </div>
</template>

<script>
import DeadCardItem from './DeadCardItem';

export default {
  name: 'DeadCards',
  components: {
    DeadCardItem
  },
  props: {
    deadCards: Array,
  }
}
</script>

<style>

</style>