<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="registerUser">
        <div>
          <label for="username">Username: </label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">Password: </label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div>
          <label for="name">Name: </label>
          <input type="text" id="name" v-model="name" required>
        </div>
        <div>
          <label for="surname">Surname: </label>
          <input type="text" id="surname" v-model="surname" required>
        </div>
        <div>
          <label for="email">Email: </label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <button type="submit">Register</button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
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
      // Name checks
      registerUser() {
        if (!/^[a-zA-Z\s]+$/.test(this.name)) {
        this.error = 'Name must not contain numbers';
        return;
      }

      if (!/^[a-zA-Z\s]+$/.test(this.surname)) {
        this.error = 'Surname must not contain numbers';
        return;
      }
        // API POST Calling
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
form input[type="password"],
form textarea {
  padding: 10px;
  margin-bottom: 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  background-color: #fff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  width: fill;
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
}

form button[type="submit"]:hover {
  background-color: #3e8e41;
}
</style>