<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light prio">
      <a class="navbar-brand" href="#">FertImpact</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/map">Maps</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/map_flora">Flora maps</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/database">Database</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/register">Register</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/profile">Profile</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/logout">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<style>
  .navbar-brand {
    font-weight: bold;
  }

  .nav-link {
    color: #333;
  }

  .nav-link:hover {
    color: #fff;
    background-color: #333;
  }

  .active {
    color: #fff;
    background-color: #333;
  }

  .prio {
   position: relative;
   z-index: 1;
   margin-right: auto;
   width: fit-content;
   height: fit-content;
}
</style>
