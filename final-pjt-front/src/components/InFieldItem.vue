<template>
  <div @click="attack" :class="{ 'can-attack' : fieldCard.canAttack }">
    <b-card bg-variant="info" text-variant="white" :header="fieldCard.name" class="text-center">
      <img :src="fieldCard.posterpath" alt="" style="width: 80px; height: 120px;" >
      <b-card-text><span style="">{{ fieldCard.attackdamage }}</span> / <span>{{ fieldCard.hp }}</span></b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'InFieldItem',
  props: {
    fieldCard: Object,
  },
  methods: {
    attack() {
      if (this.fieldCard.canAttack) {
        this.$emit('attack', this.fieldCard)
      } else {
        alert('다음 턴에 공격할 수 있습니다.')
      }
    },
  },
  watch: {
    'fieldCard.hp'(nowHp) {
      if (nowHp <= 0) {
        this.$emit('goToDie', this.fieldCard)
      }
    }
  }
}
</script>

<style>
  .can-attack {
    border: 5px solid green;
  }
</style>