<template>
  <div :class="{ 'can-attack' : canAttack,  'can-choose' : canChoose}">
    <b-card bg-variant="default" text-variant="black" :header="name" class="text-center mx-0 px-0" style="width:250px;" @click="attack" >
      <img :src="fieldCard.posterpath" alt="" style="width: 220px; height: 150px;" >
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
    },
  },
  computed: {
    name() {
      return this.fieldCard.name.length > 15 ? this.fieldCard.name.slice(0,15) : this.fieldCard.name
    },
    canChoose() {
      return this.onTarget ? true : false
    },
    canAttack() {
      return this.fieldCard.canAttack
    }
  },
}
</script>

<style>
  .can-attack {
    border: 5px solid green;
  }
  .can-choose {
    border: 5px solid red;
  }
</style>