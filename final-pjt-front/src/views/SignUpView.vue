<template>
  <div :style="{ backgroundImage: 'linear-gradient(rgba(31.5, 31.5, 52.5, 1) 0px, rgba(40.5, 35.5, 60.5, 0.84) -100%), url(' + backdroppath + ')', backgroundSize: 'cover', height:'1000px', marginLeft:0,}" class="text-white">
    <div style="padding-top:10%;">
      <h1>JSstone 회원가입</h1>
      <form @submit.prevent="signUp">
        <label for="username">USERNAME &nbsp;&nbsp;</label>
        <input type="text" id="username" v-model="username" class="upload-name"><br>

        <label for="password1"> 비밀번호 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
        <input type="password" id="password1" v-model="password1" class="upload-name"><br>

        <label for="password2"> 비밀번호 확인 &nbsp;</label>
        <input type="password" id="password2" v-model="password2" class="upload-name"><br>
        <b-button variant="outline-success" type="submit" style="width:500px;" class="mt-3">회원가입</b-button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      
      const payload = {
        username, password1, password2
      }
      this.username = null
      this.password1 = null
      this.password2 = null
      this.$store.dispatch('signUp', payload)
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