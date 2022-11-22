<template>
  <div>
    <div>
      <p>작성자 : {{article.user}}</p>
      <p>제목 : {{article.title}}</p>
      <p>스테이지 : {{article.stage}}</p>
      <div style="display: flex;">
        <ScoreDetailItem v-for="(card, index) in article.moviecard_set" :key="index" :card="card" />
      </div>
      <p>내용 : {{article.content}}</p>
    </div>
    <hr>
    <div>
      <CommentCreate @add-comment="getArticleDetail" />
    </div>
    <hr>
    <div>
      <CommentList :comments="comments" />
    </div>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'
import ScoreDetailItem from '@/components/ScoreDetailItem'
import CommentCreate from '@/components/CommentCreate'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      comments: []
    }
  },
  components: {
    CommentList,
    ScoreDetailItem,
    CommentCreate,
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
          if (res.data.comment_set.length !== this.comments.length) {
            this.comments = res.data.comment_set
          } else {
            this.getArticleDetail()
          }
        })
        .catch(err => console.log(err))
    },
  },
}
</script>