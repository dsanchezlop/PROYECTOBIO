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
  import Cookies from 'js-cookie';

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
        axios.post('http://127.0.0.1:5000/login', {
        username: this.username,
        password: this.password
      })
        .then(response => {
          // Handle successful login here
          console.log(response.data.message);
          // Set the cookies
          const twoHoursFromNow = new Date(Date.now() + 2 * 60 * 60 * 1000);
          Cookies.set('username', response.data.username, { expires: twoHoursFromNow });
          Cookies.set('role', response.data.role, { expires: twoHoursFromNow });
          Cookies.set('isLoggedIn', 'true', { expires: twoHoursFromNow })
          // Navigate to the home page
          this.$router.push('/');
        })
        .catch(error => {
          // Handle failed login here
          console.log(error.response.data.error);
        });
      }
    }
  }
  </script>

<style>
form {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 5px;
}

form label {
  font-weight: bold;
  margin-bottom: 10px;
}

form input[type="text"],
form input[type="email"],
form textarea {
  padding: 10px;
  margin-bottom: 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  background-color: #fff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

form textarea {
  height: 150px;
}

form button[type="submit"] {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
  width: fill;
}

form button[type="submit"]:hover {
  background-color: #3e8e41;
}
</style>