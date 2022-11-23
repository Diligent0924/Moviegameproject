<template>
  <div style="display: flex; justify-content: center;">
    <InFieldItem v-for="(fieldCard, index) in fieldCards" :key="index" :fieldCard="fieldCard"
      @attack="attack" @goToDie="goToDie" style="margin-left:15px; margin-right:15px;"
    />
  </div>
</template>

<script>
import InFieldItem from './InFieldItem';

export default {
  name: 'InField',
  components: {
    InFieldItem,
  },
  props: {
    fieldCards: Array,
  },
  methods: {
    attack(attackFrom) {
      this.$emit('attack', attackFrom)
    },
    goToDie(card) {
      this.$emit('goToDie', card)
    }
  }
}
</script>

<style>

</style>