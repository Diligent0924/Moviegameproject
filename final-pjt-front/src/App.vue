<template>
  <div id="app">
    <nav class="navbar navbar-light justify-content-between mb-5" style="background-color: #e3f2fd;">
      <div>
        <router-link :to="{ name: 'inven' }" class="router-link-class">
          <img thumbnail rounded fluid src="./assets/SSasstone.png" alt="#" style="width: 50px; height: 50px;">
        </router-link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <b-button variant="success" v-if="isLogined && notInPlay" @click="logOut">로그 아웃</b-button>
      </div>
      <div>
        <div class="my-2 mx-3">
          <span class="mx-2">
            <router-link :to="{ name: 'login' }" class="router-link-class" v-if="!isLogined">로그인</router-link> 
          </span>
          <span class="mx-2">
            <router-link :to="{ name: 'signup' }" class="router-link-class" v-if="!isLogined">회원가입</router-link> 
          </span>
          <span class="mx-2">
            <router-link :to="{ name: 'scoreboard' }" class="router-link-class">랭킹</router-link>
          </span>
          <span class="mx-2">
            <router-link :to="{ name: 'inven' }" class="router-link-class">인벤</router-link>
          </span>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>
<script>

export default {
  name: 'App',
  computed: {
    isLogined() {
      if (this.$store.state.token) {
        return true;
      } else {
        return false; 
      }
    },
    notInPlay() {
      return this.$store.state.canGo
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logout');
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.router-link-class {
  font-size: x-large;
}
</style>
