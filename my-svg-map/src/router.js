import { createRouter, createWebHistory } from 'vue-router';
import hello from "./components/HelloWorld.vue";
import map from "./components/SVGMap.vue";
import login from "./components/Login.vue";
import database from "./components/Database.vue";
import register from "./components/Register.vue";
import logout from "./components/Logout.vue";
import charts from "./components/Charts.vue";
import contact from "./components/Contact.vue";


//Routes
const _routes = [
{
    path:"/",
    name:"hello",
    component:hello,
},
{
    path:"/map",
    name:"map",
    component:map
},
{
    path:"/login",
    name:"login",
    component:login,
    meta: {
        requiresGuest: true // add this meta property to mark this route as requiring a guest user
      }
},
{
    path: '/database',
    name: 'database',
    component: database,
    beforeEnter: (to, from, next) => {
        const isLoggedIn = document.cookie.includes('isLoggedIn=true');
        const userRoleCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('role='));
        
        if (isLoggedIn && userRoleCookie) {
          const userRole = parseInt(userRoleCookie.split('=')[1].trim());
          if (userRole === 1) {
            next();
            return;
          }
        }
      
        next('/login');
      },
  },
{
    path:"/register",
    name:"register",
    component:register,
    meta: {
        requiresGuest: true // add this meta property to mark this route as requiring a guest user
      }
},
{
    path:"/logout",
    name:"logout",
    component:logout
},
{
    path:"/charts",
    name:"charts",
    component:charts
},
{
    path:"/contact",
    name:"contact",
    component:contact
}

];

//Create router
const router = createRouter({
    history:createWebHistory(),
    routes: _routes,
});

// authentication check
router.beforeEach((to, from, next) => {
    const loggedIn = document.cookie.includes('isLoggedIn=true');
  
    // redirect to login page if user is not logged in and trying to access a protected page
    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
      next('/login');
      return;
    }
  
    // redirect to home page if user is logged in and trying to access login/register page
    if (to.matched.some(record => record.meta.requiresGuest) && loggedIn) {
      next('/');
      return;
    }
  
    next();
  });

//Export router
export default router;