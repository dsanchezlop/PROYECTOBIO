<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>Email</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.user_id">
          <td>{{ user.user_id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>
            <button type="button" @click="deleteUser(user.user_id)">Delete user</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch("http://localhost:5000/users")
        .then((response) => response.json())
        .then((data) => {
          this.users = data.users;
        });
    },
    deleteUser(userId) {
      fetch(`http://localhost:5000/delete-user/${userId}`, {
        method: 'DELETE'
      })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
        this.fetchData();
      })
      .catch((error) => {
        console.error(error);
      });
    }
  },
};
</script>

<style>
button[type="button"] {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

button[type="button"]:hover {
  background-color: #3e8e41;
}

table {
  border-collapse: separate;
  border-spacing: 0 10px;
}
</style>
