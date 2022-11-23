<template>
  <div>
    <div class="my-3">
      <p style="color: crimson; border-bottom:20px"><b>{{ card.name }}</b></p>
    </div>
    <div>
      <img :src="card.posterpath" alt="#" @click="pickCard" style="width: 80%; height: 80%;">
    </div>
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
  },
  computed: {
    skillType() {
      if (this.card.skilltype) {
        return this.card.skillcomment
      } else {
        return 'Not Found'
      }
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
    }
  },
  methods: {
   pickCard() {
     if (this.cardNum >= 10) {
       alert('이미 10장의 카드를 선택하였습니다.')
     } else if (this.card.name === '카드명') {
       alert('카드 오픈 버튼을 눌러주세요.')
     } else {
         this.$store.dispatch('pickCard', this.card)
      
         if (this.cardNum < 10) {
           this.$store.dispatch('openCard')
         }
       }
     }
   },
}
</script>

<style>
  img {
    width: 300px;
    height: 400px;
  }
</style>