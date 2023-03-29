<template>
    <div class="container">
        <h1>Login Page</h1>
        <form action="{{url_for('login')}}" method="POST">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" name="username" id="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" required>
            </div>
            <div class="form-group">
                <input type="submit" value="Login">
            </div>
        </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Login',
  }
  </script>
  
  <style>

  </style>
  