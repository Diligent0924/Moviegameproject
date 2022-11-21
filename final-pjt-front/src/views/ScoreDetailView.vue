<template>
  <div>
    <div>
      <p>작성자 : {{article.user}}</p>
      <p>제목 : {{article.title}}</p>
      <p>스테이지 : {{article.stage}}</p>
      <div>
        <ScoreDetailItem v-for="(card, index) in article.moviecard_set" :key="index" :card="card" />
      </div>
      <p>내용 : {{article.content}}</p>
    </div>
    <div>
      <CommentList/>
    </div>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'
import ScoreDetailItem from '@/components/ScoreDetailItem'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
    }
  },
  components: {
    CommentList,
    ScoreDetailItem,
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/scoreboard/${this.$route.params.id}/`
      })
        .then((res) => {
          // console.log(res.data)
          this.article = res.data
        })
        .catch(err => console.log(err))
    }
  }
}
</script>