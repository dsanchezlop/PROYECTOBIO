<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label>Username</label>
        <input type="text" v-model="username" required>
      </div>
      <div>
        <label>Password</label>
        <input type="password" v-model="password" required>
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    // API POST Login
    login() {
      console.log("Making login request to /api/login endpoint...");
      axios.post('http://127.0.0.1:5000/login', {
        username: this.username,
        password: this.password
      })
        .then(response => {
          // Handle successful login here
          console.log(response.data.message);
          // Set the cookies
          const twoHoursFromNow = new Date(Date.now() + 2 * 60 * 60 * 1000);
          Cookies.set('user_id', response.data.user_id, { expires: twoHoursFromNow });
          Cookies.set('username', response.data.username, { expires: twoHoursFromNow });
          Cookies.set('role', response.data.role, { expires: twoHoursFromNow });
          Cookies.set('isLoggedIn', 'true', { expires: twoHoursFromNow })
          // Navigate to the home page
          window.location.href = "/";
        })
        .catch(error => {
          // Handle failed login here
          console.log(error.response.data.error);
          this.errorMessage = error.response.data.error;
        });
    }
  }
}
</script>

<style>
/* Your styles here */
</style>
