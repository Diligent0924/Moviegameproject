<template>
  <div>
    <h1>모험 기록 작성</h1>
    <h3>{{ clearMessage }}</h3>
    <b style="color: blueviolet;"><p><span>최종 보스 : {{ finalBoss }}</span> / <span>최종 스테이지 : {{ finalBossLevel }}</span></p></b>
    <h3>사용 카드</h3>
    <div style="display: flex;">
      <MyCard v-for="(card, index) in finalDeck" :key="index" :card="card" />
    </div>
    <br>
    <form @submit.prevent="createArticle">
      제목 : <input type="text" v-model.trim="title"><br>
      내용 : <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'


export default {
  name: 'CreateArticleView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const clearMessage = this.clearMessage
      const payload = {
        title, content, clearMessage
      }
      this.$store.dispatch('createArticle', payload)
      this.$router.push({ name: 'scoreboard' })
    }
  },
  computed: {
    finalDeck() {
      return this.$store.state.finalUserCard
    },
    finalBossLevel() {
      return this.$store.state.finalBossLevel
    },
    finalBoss() {
      return this.$store.state.bossCards[this.finalBossLevel-1].name
    },
    clearMessage() {
      if (this.finalBossLevel === 7) {
        return 'Cleared'
      } else {
        return 'Failed'
      }
    }
  },
  components: {
    MyCard
  }
}
</script>

<style>

</style>