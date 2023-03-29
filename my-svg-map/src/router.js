//1. Create a router and export it.
import hello from "./components/HelloWorld.vue";
import map from "./components/SVGMap.vue";
import { createRouter, createWebHistory } from 'vue-router';

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
}
];

//Create router
const router = createRouter({
    history:createWebHistory(),
    routes: _routes,
});

//Export router
export default router;