<template>
  <div>
    <img :src="card.posterpath" alt="#" style="width: 150px; height: 200px;" @click="cardStat">
  </div>
</template>

<script>
export default {
  name: 'MyCard',
  props: {
    card: Object,
  },
  methods: {
    cardStat() {
      if (this.card.movietype === 'unique') {
        const skillComment = this.card.skillcomment
        if (!this.card.hp) {
          alert(`주문\n특수 효과 : ${skillComment}`)
        } else {
          const cardHP = this.card.hp
          const cardAD = this.card.attackdamage
          alert(`희귀카드\n공격력 : ${cardAD} 생명력 : ${cardHP}\n특수 효과 : ${skillComment}`)
        }
      } else {
        const cardHP = this.card.hp
        const cardAD = this.card.attackdamage
        alert(`일반 카드\n공격력 : ${cardAD}  생명력 : ${cardHP}`)
      }
    }
  }
}
</script>

<style>

</style>