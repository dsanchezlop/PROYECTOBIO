<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="registerUser">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="name" required>
        </div>
        <div>
          <label for="surname">Surname:</label>
          <input type="text" id="surname" v-model="surname" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: '',
        name: '',
        surname: '',
        email: '',
        error: '',
      };
    },
    methods: {
      registerUser() {
        if (!/^[a-zA-Z]+$/.test(this.name)) {
          this.error = 'Name must not contain numbers';
          return;
        }

        if (!/^[a-zA-Z]+$/.test(this.surname)) {
          this.error = 'Surname must not contain numbers';
          return;
        }

        axios.post('http://127.0.0.1:5000/register', {
          username: this.username,
          password: this.password,
          name: this.name,
          surname: this.surname,
          email: this.email,
        })
          .then(response => {
            console.log(response);
            this.$router.push('/login');
          })
          .catch(error => {
            console.log(error);
            this.error = error.response.data.error;
          });
      },
    },
  };
  </script>