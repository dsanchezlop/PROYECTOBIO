<template>
    <div class="container">
        <h1>Registration Page</h1>
        <form action="" method="post">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" name="username" id="username" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" name="email" id="email" required>
            </div>
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name" required>
            </div>
            <div class="form-group">
                <label for="surname">Surname:</label>
                <input type="text" name="surname" id="surname" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" required>
            </div>
            <div class="form-group">
                <label for="confirm-password">Confirm Password:</label>
                <input type="password" name="confirm-password" id="confirm-password" required>
            </div>
            <div class="form-group">
                <input type="submit" value="Register">
            </div>
        </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Register',
  }
  </script>
  
  <style>

  </style>
  