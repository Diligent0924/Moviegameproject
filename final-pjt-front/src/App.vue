<template>
  <div id="app">
    <div v-if="toSmall" class="justify-content-center" style="margin-top: 250px">
      <h1>
        원활한 게임 진행을 위해 화면을 키워주세요.
      </h1>
    </div>
    <div v-else>
      <nav class="navbar navbar-light justify-content-between" style="background-color:#FFFAFA">
        <div class="mx-5">
          <router-link :to="{ name: 'inven' }" class="router-link-class">
            <img thumbnail rounded fluid src="./assets/SSasstone.png" alt="#" style="width: 50px; height: 50px;">
          </router-link>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <button variant="success" v-if="isLogined && notInPlay" @click="logOut" type="button" class="btn btn-outline-warning">로그 아웃</button>
          <b-button variant="danger" @click="allReset" >초기화</b-button>
        </div>
        <div class="mx-5">
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
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch('logout');
      this.$router.push({ name: 'login' });
    },
    allReset() {
      if (confirm('정말 초기화 하시겠습니까?\n로그인 정보를 포함한 모든 상태가 초기화됩니다.')) {
        this.$store.dispatch('allReset')
        alert('모든 정보가 초기화되었습니다. 회원가입 페이지로 이동합니다.')
        this.$router.push({ name: 'signup' })
      }
    },
    resizeHandler()  {
        this.height =  window.innerHeight;
        this.width =  window.innerWidth;
    },
  },
  data() {
    return {
      toSmall: false,
      height: 0,
      width: 0
    }
  },
  watch: {
    height (newHeight) {
      if (newHeight <= 900) {
        this.toSmall = true
      } else {
        this.toSmall = false
      }
    },
    width (newWidth) {
      if (newWidth <= 1200) {
        this.toSmall = true
      } else {
        this.toSmall = false
      }
    }
  },
  created()  {
    window.addEventListener("resize", this.resizeHandler);
  },
  destroyed()  {
    window.removeEventListener("resize", this.resizeHandler);
  },
  mounted()  {
    this.height = window.innerHeight;
    this.width = window.innerWidth;
  },
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
  margin-left: 5%;
  margin-right: 5%;
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
    background: linear-gradient(-45deg, #FFFAFA, #02020263, #FFFAFA, #02020263);
    background-size: 400% 400%;
    animation: gradient 5s ease infinite;
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
