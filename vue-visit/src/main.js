import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'


import { createRouter, createWebHistory } from 'vue-router'
import TheDoctors from './components/Doctors/TheDoctors.vue'
import TheDoctorDetail from './components/Doctors/TheDoctorDetail.vue'
import BookAppointment from './components/Doctors/BookAppointment.vue'
import ReviewAppointment from './components/Doctors/ReviewAppointment.vue'

import BaseButton from './components/UI/BaseButton.vue'
import BaseDialog from './components/UI/BaseDialog.vue'
import BaseAuthButton from './components/UI/BaseAuthButton.vue'
import TheFooter from './components/UI/TheFooter.vue'

import UserAuth from './components/Authentication/UserAuth.vue'

import UserProfile from './components/Profile/UserProfile.vue'
import LogoutPage from './components/Profile/LogoutPage.vue'

// const auth = userAuthStore();

const routes = [
    { path: '/', redirect: '/doctors'},
    { path: '/user_auth', component: UserAuth},
    { path: '/doctors', components: { default:TheDoctors, footer:TheFooter} },
    { path: '/doctors/:id', component: TheDoctorDetail, name: 'doctorDetail', props: true },
    { path: '/book/appointment', component: BookAppointment, name: 'bookAppointment', props: true},
    
    { path: '/profile', 
        component:  UserProfile,
    //   beforeEnter: (to, from, next) => {
    //     const isAuthenticated = auth.isUserLoggedIn; // Check if user is logged in
    //     if (!isAuthenticated) {
    //         next('/user_auth'); // Redirect to login
    //     } else {
    //       next(); // Allow access
    //     }}
    },
    {
        path: '/profile/review/:id/:date',
        component: ReviewAppointment,
        name: 'reviewAppointment',
        props: true,
        
    },
    // { path: '/doctors/:id', component: TheDoctorDetail },
    // { path: '*', redirect: '/doctors' } // Redirects any unmatched routes
    // { path: '/doctors/:id', component: TheDoctorDetail, name: 'doctorDetail', props: (route) => ({ id: route.params.id, doctor: route.params.doctor }) },
    { path: '/:notfound(.*)', redirect: '/doctors'},

    { path: '/logout', component: LogoutPage}

]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior (_, _2, savedPosition) {
        if (savedPosition) {
            return savedPosition
        }
         return {left: 0, top: 0}
      }
  
})


// router.beforeEach((to, from, next) => {
//     const isAuthenticated = localStorage.getItem('UserIsLoggedIn')
    
//     if (to.path = '/profile' && !isAuthenticated) {
//         next('user_auth')
//     } else {
//         next()
//     }

// })
const pinia = createPinia()
const app = createApp(App)

app.component('base-button', BaseButton )
app.component('base-dialog', BaseDialog )
app.component('base-auth-button', BaseAuthButton )

import axios from 'axios'

axios.defaults.baseURL = 'http://0.0.0.0:8000'
app.use(pinia)
app.use(router)
app.mount('#app')
