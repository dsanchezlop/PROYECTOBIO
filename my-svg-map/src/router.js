import { createRouter, createWebHistory } from 'vue-router';
import hello from "./components/HelloWorld.vue";
import map from "./components/SVGMap.vue";
import login from "./components/Login.vue";
import map_flora from "./components/FloraMaps.vue";
import database from "./components/Database.vue";
import register from "./components/Register.vue";
import profile from "./components/Profile.vue";
import logout from "./components/Logout.vue";


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
    component:login
},
{
    path:"/map_flora",
    name:"map_flora",
    component:map_flora
},
{
    path:"/database",
    name:"database",
    component:database
},
{
    path:"/register",
    name:"register",
    component:register
},
{
    path:"/profile",
    name:"profile",
    component:profile
},
{
    path:"/logout",
    name:"logout",
    component:logout
}
];

//Create router
const router = createRouter({
    history:createWebHistory(),
    routes: _routes,
});

//Export router
export default router;