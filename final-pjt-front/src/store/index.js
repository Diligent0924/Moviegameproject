import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'
import _ from 'lodash'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    scores: null,
    bossCards: [],
    userCards: [],
    randomCards: ['1번 카드', '2번 카드', '3번 카드'],
    bossLevel: 0,
    useTurns: [],
    finalUserCard: [],
    finalBossLevel: 0,
  },
  getters: {
    cardNum(state) {
      return state.userCards.length
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'inven' })
    },
    DELETE_TOKEN(state) {
      state.token = null
    },
    PICK_CARD(state, pickedCard) {
      state.userCards.push(pickedCard)
    },
    MAKE_BOSSCARD(state, bossList) {
      state.bossCards = bossList
    },
    RANDOM_CARDS(state, payload) {
      state.randomCards = payload
    },
    WIN(state, payload) {
      state.bossLevel++
      state.useTurns.push(payload.turns)
    },
    LOSE(state, payload) {
      state.useTurns.push(payload.turns)
      state.finalUserCard = _.cloneDeep(state.userCards)
      state.finalBossLevel = _.cloneDeep(state.bossLevel)
      state.finalBossLevel++
      state.userCards = []
      state.bossLevel = 0
    }
  },
  // ACTIONS
  actions: {
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
      .then(() => {
        // console.log(res)
        context.commit('DELETE_TOKEN')
      })
      .catch(err => {
        console.log(err)
      })
    },
    createDeckList(context) {
      axios({
        method: 'post',
        url: `${API_URL}/moviecards/normalcard_list/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then(res => { console.log(res) })
        .catch(err => { console.log(err) })

      axios({
        method: 'post',
        url: `${API_URL}/moviecards/bosscard_list/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then(res => {
          console.log(res)
          context.commit('MAKE_BOSSCARD', res.data)
        })
        .catch(err => { console.log(err) })
    },
    pickCard(context, pickedCard) {
      context.commit('PICK_CARD', pickedCard)
    },
    openCard(context) {
      const API_URL = 'http://127.0.0.1:8000'

      axios({
        method: 'get',
        url: `${API_URL}/moviecards/plus/`
      })
        .then(res => {
          let payload = [res.data[0], res.data[1], res.data[2]]
          context.commit('RANDOM_CARDS', payload)
        })
        .catch(err => {
          console.log(err)
        })
    },
    win(context, payload) {
      context.commit('WIN', payload)
    },
    lose(context, payload) {
      context.commit('LOSE', payload)
    }
  },
  modules: {
  }
})