<template>
  <div id="app">
    <div id="whole">
      <nav class="navbar navbar-light justify-content-between mb-5">
        <div>
          <router-link :to="{ name: 'inven' }" class="router-link-class">
            <img thumbnail rounded fluid src="./assets/SSasstone.png" alt="#" style="width: 50px; height: 50px;">
          </router-link>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <button variant="success" v-if="isLogined && notInPlay" @click="logOut" type="button" class="btn btn-outline-warning">로그 아웃</button>
        </div>
        <div>
          <div class="my-2 mx-3">
            <span class="mx-2">
              <router-link :to="{ name: 'login' }" class="router-link-class text-decoration-none" v-if="!isLogined">로그인</router-link> 
            </span>
            <span class="mx-2">
              <router-link :to="{ name: 'signup' }" class="router-link-class text-decoration-none" v-if="!isLogined">회원가입</router-link> 
            </span>
            <span class="mx-2">
              <router-link :to="{ name: 'scoreboard' }" class="router-link-class text-decoration-none">랭킹</router-link>
            </span>
            <span class="mx-2">
              <router-link :to="{ name: 'inven' }" class="router-link-class text-decoration-none">인벤</router-link>
            </span>
          </div>
        </div>
      </nav>
      <router-view/>
    </div>
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

#whole{
  margin-left: 10%;
  margin-right: 10%;
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

body {
    background: linear-gradient(-45deg, #dbdfda, #25202063, #dbdfda, #25202063);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
    height: 100vh;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

</style>
