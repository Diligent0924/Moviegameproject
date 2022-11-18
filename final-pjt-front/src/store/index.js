import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    scores: null,
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'inven' })
    },
    DELETE_TOKEN(state) {
      state.token = null
    },
  },
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
      context
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
        .then(res => { console.log(res) })
        .catch(err => { console.log(err) })
    },
  },
  modules: {
  }
})
