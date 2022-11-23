<template>
  <div class="my-5">
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
        <div class="hover-container g-4">
          <ScoreDetailItem class="item" v-for="(card, index) in article.moviecard_set" :key="index" :card="card" />
        </div>
        <!-- 여기는 사용한 카드를 넣는 곳 크기를 작게 해서 넣자.-->
      </b-row>
      <b-row>
        <h4>내용 : {{article.content}}</h4>
      </b-row>
      <b-row>
        <b-col cols="3"></b-col>
        <b-col cols="6"><CommentCreate @add-comment="getArticleDetail" /></b-col>
        <b-col cols="3"></b-col>
      </b-row>
      <b-row>
        <b-col coles="2"></b-col>
        <b-col coles="8"><CommentList :comments="comments" /></b-col>
        <b-col coles="2"></b-col>
      </b-row>
    </b-container>
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