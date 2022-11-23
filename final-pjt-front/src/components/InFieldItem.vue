<template>
  <div @click="attack" :class="{ 'can-attack' : fieldCard.canAttack || onTarget }">
    <b-card bg-variant="default" text-variant="black" :header="name" class="text-center;" style="width:250px;">
      <img :src="fieldCard.posterpath" alt="" style="width: 100px; height: 100px;" >
      <b-card-text>
        <span style="color:crimson;"><b>AD {{ fieldCard.attackdamage }}</b></span>  &nbsp;
        <span style="color:green;"><b>HP {{ fieldCard.hp }}</b></span>
      </b-card-text>
    </b-card>
  </div>  
</template>

<script>
export default {
  name: 'InFieldItem',
  props: {
    fieldCard: Object,
    onTarget: Boolean,
  },
  methods: {
    attack() {
      if (this.onTarget) {
        this.$emit('pickTarget', this.fieldCard)
        return
      }

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
  },
  computed: {
    name() {
      return this.fieldCard.name.length > 15 ? this.fieldCard.name.slice(0,15) : this.fieldCard.name
    }
  }
}
</script>

<style>
  .can-attack {
    border: 5px solid green;
  }
</style>