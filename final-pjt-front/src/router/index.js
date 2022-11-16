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
    path: '/inven',
    name: 'inven',
    component: InvenView,
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
        name:'playing',
        component: PlayingAreaView
      },
      {
        path: 'coin',
        name:'coin',
        component: CoinAreaView
      }
    ]
  },
  {
    path: '/scoreboard/detail',
    name: 'scoreboard-detail',
    component: ScoreDetailView,
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

export default router