import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/LoginView'
import SignUpView from '@/views/SignUpView'
import InvenView from '@/views/InvenView'
import ScoreBoardView from '@/views/ScoreBoardView'
import NotFound404 from '@/views/NotFound404'
import GamePageView from '@/views/GamePageView'
import FirstDeckView from '@/views/FirstDeckView'
import PlayingAreaView from '@/views/PlayingAreaView'
import CoinAreaView from '@/views/CoinAreaView'
import ScoreDetailView from '@/views/ScoreDetailView'
import CreateArticleView from '@/views/CreateArticleView'
import InvenDetailView from '@/views/InvenDetailView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView,
  },
  {
    path: '/scoreboard',
    name:'scoreboard',
    component: ScoreBoardView,
  },
  {
    path: '/scoreboard/:id',
    name:'scoredetail',
    component: ScoreDetailView,
  },
  {
    path: '/inven',
    name: 'inven',
    component: InvenView,
  },
  {
    path: '/inven/:movieid',
    name: 'invendetail',
    component: InvenDetailView,
  },
  {
    path: '/createarticle',
    name: 'createarticle',
    component: CreateArticleView,
  },
  {
    path: '/game',
    name: 'game',
    component: GamePageView,
    children: [
      {
        path: 'start',
        name:'start',
        component: FirstDeckView,
      },
      {
        path: 'playing',
        name: 'playing',
        component: PlayingAreaView
      },
      {
        path: 'coin',
        name: 'coin',
        component: CoinAreaView
      }
    ]
  },
  {
    path: '*',
    name: '404',
    component: NotFound404,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes

})

// const canOut = ['start', 'playing', 'coin', 'createarticle']
// router.beforeEach(function (to, from, next) {
//   if (window.localStorage.vuex) {
//     const locals = JSON.parse(window.localStorage.vuex)
//     if (locals.canGo) {
//       next()
//     } else{
//       alert('끝까지 플레이 하세요 ^-^')
//     }
//   } else {
//     next()
//   }
// })


export default router