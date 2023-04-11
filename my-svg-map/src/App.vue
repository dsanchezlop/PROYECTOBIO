<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light prio">
      <a class="navbar-brand" href="#">FertImpact</a>
      <!-- <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button> -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/" onclick="location.href=this.href; location.reload(true); return false;">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/map">Maps</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/map_flora" onclick="location.href=this.href; location.reload(true); return false;">Flora maps</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="showDatabaseOption" class="nav-link" to="/database" onclick="location.href=this.href; location.reload(true); return false;">User database</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/contact" onclick="location.href=this.href; location.reload(true); return false;">Contact</router-link>
          </li>
          <li v-if="!loggedIn" class="nav-item">
            <router-link class="nav-link" to="/login" onclick="location.href=this.href; location.reload(true); return false;">Login</router-link>
          </li>
          <li v-if="!loggedIn" class="nav-item">
            <router-link class="nav-link" to="/register" onclick="location.href=this.href; location.reload(true); return false;">Register</router-link>
          </li>
          <li v-if="loggedIn" class="nav-item">
            <router-link class="nav-link" to="/profile" onclick="location.href=this.href; location.reload(true); return false;">Profile</router-link>
          </li>
          <li v-if="loggedIn" class="nav-item">
            <router-link class="nav-link" to="/logout" @click="logout"
              >Logout</router-link
            >
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  computed: {
    loggedIn() {
      return document.cookie.includes("isLoggedIn=true");
    },
    showDatabaseOption() {
      const roleCookie = document.cookie
        .split(";")
        .find((c) => c.trim().startsWith("role="));
      if (roleCookie && roleCookie.split("=")[1] === "1") {
        return true;
      } else {
        return false;
      }
    },
  },
  watch: {
    loggedIn() {
      // Update the navbar on every change to isLoggedIn
      this.$forceUpdate();
    },
  },
  methods: {
    logout() {
      // Gets all the cookies
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i];
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
      }
      window.location.href = "/";
    },
  },
};
</script>

<style>
.navbar-brand {
  font-weight: bold;
}

.nav-link {
  color: #333;
}

.nav-link:hover {
  color: #fff;
  background-color: #a5a5a5;
}

.active {
  color: #fff;
  background-color: #a5a5a5;
}

.prio {
  position: relative;
  z-index: 1;
  margin-right: auto;
  width: fit-content;
  height: fit-content;
}
/* Style for the #about section */
#about {
  padding: 50px;
  background-color: #F5F5F5;
}

/* Style for the #research section */
#research {
  padding: 50px;
  background-color: #FFF;
}

/* Style for the #publications section */
#publications {
  padding: 50px;
  background-color: #F5F5F5;
}

/* Style for the #contact section */
#contact {
  padding: 50px;
  background-color: #FFF;
}

/* Style for section headings */
section h2 {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: bold;
}

/* Style for section paragraphs */
section p {
  margin-bottom: 20px;
  font-size: 16px;
  line-height: 1.5;
}

/* Style for publication links */
section a {
  display: block;
  margin-bottom: 10px;
  font-size: 16px;
  line-height: 1.5;
  color: #42b983;
  text-decoration: none;
}

/* Style for publication links on hover */
section a:hover {
  text-decoration: underline;
}

h1{
  text-align: center;
}
</style>
