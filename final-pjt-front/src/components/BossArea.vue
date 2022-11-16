<template>
  <div>
    <h3>보스 공간</h3>
    <div style="display: flex; justify-content: center;">
      <CardItem/>
      <CardItem/>
      <CardItem/>
      <CardItem/>
      <CardItem/>
    </div>
  </div>
</template>

<script>
import CardItem from '@/components/CardItem'

export default {
  name: 'BossArea',
  components: {
      CardItem
  },
}
</script>

<style>

</style>