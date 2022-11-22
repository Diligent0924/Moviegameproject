<template>
  <div>
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col>
          <h4>작성자:  {{article.user}}</h4>
        </b-col>
        <b-col cols="8">
          <h4>제목:  {{article.title}} </h4>
        </b-col>
        <b-col>
          <h4>스테이지:  {{article.stage}} </h4>
        </b-col>
      </b-row>
      <b-row>
        <ScoreDetailItem v-for="(card, index) in article.moviecard_set" :key="index" :card="card" />
        <!-- 여기는 사용한 카드를 넣는 곳 크기를 작게 해서 넣자.-->
      </b-row>
      <b-row>
        <h4>내용 : {{article.content}}</h4>
      </b-row>
    </b-container>
    <!-- <div>
      <div style="display: flex;">
        <ScoreDetailItem v-for="(card, index) in article.moviecard_set" :key="index" :card="card" />
      </div>
      <p>내용 : {{article.content}}</p>
    </div> -->
    <!-- <hr> -->
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
      comments: [],
      cnt: 0,
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
          if (res.data.comment_set.length !== this.comments.length || this.cnt > 3) {
            this.article = res.data
            console.log(this.article)
            this.comments = res.data.comment_set
            this.cnt = 0
          } else {
            this.cnt++
            this.getArticleDetail()
          }
        })
        .catch(err => console.log(err))
    },
  },
}
</script>