<template>
  <div :style="{ backgroundImage: 'linear-gradient(rgba(31.5, 31.5, 52.5, 1) 0px, rgba(40.5, 35.5, 60.5, 0.84) -100%), url(' + backdroppath + ')', backgroundSize: 'cover', height:'1000px', marginLeft:0,}" class="text-white">
    <div style="padding-top:10%;">
      <h1 id="login_head">JSstone</h1>
      <form @submit.prevent="logIn">
        <label for="username">USERNAME &nbsp;&nbsp;</label>
        <input type="text" id="username" v-model="username" class="upload-name"><br>

        <label for="password"> PASSWORD &nbsp;&nbsp;</label>
        <input type="password" id="password" v-model="password" class="upload-name"><br>
        <b-button variant="outline-success" type="submit" value="logIn" style="width:500px;" class="mt-3">로그인</b-button>
        <!-- <input type="submit" value="logIn"> -->
      </form>
      <b-button block variant="outline-danger" @click="signUp" style="width:500px;" class="mt-3">회원 가입</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
    },
    signUp() {
      this.$router.push({ name: 'signup' })
    }
  },
  computed: {
    backdroppath(){
      return "https://img.freepik.com/free-photo/a-person-facing-the-purgatory-world-illustration_456031-40.jpg?size=626&ext=jpg&ga=GA1.2.1125130295.1667449114"
    }
  }
}
</script>

<style>
  .upload-name {
      display: inline-block;
      height: 40px;
      padding: 0 10px;
      vertical-align: middle;
      border: 1px solid #dddddd;
      width: 20%;
      color: #999999;
      border-radius: 5px;
      margin-bottom: 10px;
      margin-top: 10px;
  }

  input[type=submit] {
  background-color: #04AA6D;
  border: none;
  color: white;
  padding: 16px 32px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
  }

</style>
