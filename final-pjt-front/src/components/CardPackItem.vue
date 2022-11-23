<template>
  <div>
    <div style="height:70px;">
      <p style="border-bottom:20px" :class="{'unique-card-color' : isUnique }" ><b>{{ card.name }}</b></p>
    </div>
    <img :src="card.posterpath" alt="#" @click="pickCard" style="width: 80%; height: 80%;">
    <hr>
    <p v-if="!isSepll" class="text-danger"><b>AD : {{ card.attackdamage }}</b></p>
    <p class="text-success"><b>{{ hp }}</b></p>
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
      return this.card.hp ? `HP : ${this.card.hp}` : '주문 카드'
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
      } else if (this.card.name === '카드명') {
        alert('로딩중입니다. 잠시만 기다려주세요.')
      } else {
        this.$store.dispatch('pickCard', this.card)
      
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