<template>
  <div>
    <h1>Edit User Data</h1>
    <form @submit.prevent="submit">
      <label>
        Name:
        <input type="text" v-model="name" />
      </label>
      <label>
        Email:
        <input type="email" v-model="email" />
      </label>
      <label>
        Password:
        <input type="password" v-model="password" />
      </label>
      <button type="submit">Save Changes</button>
    </form>
  </div>
</template>
  
  <script>
  import axios from 'axios'

export default {
  name:'Profile',
  data() {
    return {
      user: {},
      name: '',
      email: '',
      password: '',
    }
  },
  mounted() {
    this.getUserData()
  },
  methods: {
    getUserData() {
      axios.get('/api/user')
        .then(response => {
          this.user = response.data
          this.name = this.user.name
          this.email = this.user.email
        })
        .catch(error => {
          console.log(error)
        })
    },
    updateUser() {
      axios.put('/api/user', {
        name: this.name,
        email: this.email,
        password: this.password
      })
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
  </script>
  
  <style>

  </style>
  