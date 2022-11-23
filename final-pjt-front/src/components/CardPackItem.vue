<template>
  <div>
    <p style="border-bottom:20px" :class="{'unique-card-color' : isUnique }" ><b>{{ card.name }}</b></p>
    <img :src="card.posterpath" alt="#" @click="pickCard" style="width: 80%; height: 80%;">
    <hr>
    <p v-if="!isSepll">공격력 : {{ card.attackdamage }}</p>
    <p>{{ hp }}</p>
    <p v-if="isUnique"><b>{{ skillType }}</b></p>
  </div>
</template>

<script>
export default {
  name: 'CardPackItem',
  props: {
    card: Object,
    firstClick: Boolean,
  },
  computed: {
    skillType() {
      return this.card.skilltype ? this.card.skillcomment : 'Not Found'
    },
    cardNum() {
      return this.$store.getters.cardNum
    },
    hp() {
      return this.card.hp ? `생명력 : ${this.card.hp}` : '주문 카드'
    },
    isSepll() {
      return this.hp === '주문 카드' ? true : false
    },
    isUnique() {
      return this.card.movietype === 'unique' ? true : false
    },
  },
  methods: {
    pickCard() {
      if (this.firstClick) {
        this.$store.dispatch('openCard')
        this.$emit('afterFirst')
      } else if (this.cardNum >= 10) {
        alert('이미 10장의 카드를 선택하였습니다.')
      } else {
        this.$store.dispatch('pickCard', this.card)
        console.log('111')
      
        if (this.cardNum < 10) {
          this.$store.dispatch('openCard')
        }
      }
    }
  }
}
</script>

<style>
  img {
    width: 300px;
    height: 400px;
  }
  .unique-card-color {
    color: crimson;
  }
</style>