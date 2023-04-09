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
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login() {
        console.log("Making login request to /api/login endpoint...");
        axios.post('/login', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          // Handle successful login here
          console.log(response.data.message);
        })
        .catch(error => {
          // Handle failed login here
          console.log(error.response.data.error);
        });
      }
    }
  }
  </script>