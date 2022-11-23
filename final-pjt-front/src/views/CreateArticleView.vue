<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <h1>모험 기록 작성</h1>
      </b-row>
      <b-row>
        <h3>{{ clearMessage }}</h3>
      </b-row>
      <b-row>
        <b style="color: blueviolet;"><p><span>최종 보스 : {{ finalBoss }}</span> / <span>최종 스테이지 : {{ finalBossLevel }}</span></p></b>
      </b-row>

      <b-row>
       <h3>사용 카드</h3>
       <hr>
      </b-row>

      <b-row>
        <div class="hover-container g-4 px-0">
          <MyCard class="item" v-for="(card, index) in finalDeck" :key="index" :card="card" />
        </div>
      </b-row>
      <b-row class="my-5">
        <form @submit.prevent="createArticle" class="form-floating">
          <input type="text" v-model.trim="title" class="form-control py-0" placeholder="제목을 입력해주세요!" id="floatingTextarea">
          <textarea v-model.trim="content" class="form-control py-3 my-4" placeholder="글을 입력해주세요!" id="floatingTextarea_2"></textarea>
          <button type="submit" class="btn btn-outline-success">작성하기</button>
        </form>
      </b-row>
    </b-container>
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
      this.$store.dispatch('canGoChange')
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
.hover-container {
  display: flex;
  padding: 0;
}

.item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
}

.hover-container:focus-within .item,
.hover-container:hover .item {
  transform: translateX(-25%);
}

.item:focus ~ .item,
.item:hover ~ .item {
  transform: translateX(25%);
}

.hover-container .item:focus,
.hover-container .item:hover {
  transform: scale(1.5);
  z-index: 1;
}

.item img {
  display: block;
  max-width: 100%;
}
</style>