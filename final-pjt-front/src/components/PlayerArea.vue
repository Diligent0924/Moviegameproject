<template>
  <div>
    <div style="display: flex; justify-content: center;">
      <CardItem/>
      <CardItem/>
      <CardItem/>
      <CardItem/>
      <CardItem/>
    </div>
    <h3>
      플레이어 공간
    </h3>
  </div>
</template>

<script>
import CardItem from '@/components/CardItem'

export default {
  name: 'PlayingArea',
  components: {
    CardItem
  },
}
</script>

<style>

</style>