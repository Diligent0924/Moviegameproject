<template>
  <div>
    <b-progress :max="bossmaxhp" height="2rem" class="px-0 mb-3">
      <b-progress-bar :value="BossHp" class="fw-bold" variant="primary">
        <span>Hp: {{BossHp}} &nbsp; &nbsp;&nbsp;(LV {{bossLevel+1}} {{boss.name}})</span>
      </b-progress-bar>
    </b-progress>
    <img :src="boss.posterpath" alt="" style="width: 200px; height: 200px;" @click="attackTo" :class="{ 'in-attack' : inAttack }">
    <p><b><span style="color:red">AD {{boss.attackdamage}}</span> <span style="color:green;">HP {{boss.hp}}</span></b></p>
  </div>
</template>

<script>

export default {
  name: 'BossArea',
  data() {
    return {
      bossmaxhp : 0,
    }
  },
  props: {
    boss: Object,
    bossLevel: Number,
    inAttack: Boolean,
  },
  methods: {
    attackTo() {
      if (this.inAttack) {
        this.$emit('attackTo', this.boss)
      } else {
        alert('공격을 수행할 카드를 먼저 선택하세요.')
      }
    },
  },
  created() {
    this.bossmaxhp = this.boss.hp
  },
  computed: {
    BossHp(){
      return this.boss.hp
    },
  }
}
</script>

<style>
  .in-attack {
    border: 3px solid red;
  }
</style>