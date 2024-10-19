import axios from 'axios';
import { defineStore } from 'pinia';

export const userAuthStore = defineStore('auth', {
  state: () => ({
    
    authToken: localStorage.getItem('authToken') || null,
    isUserLoggedIn: localStorage.getItem('isUserLoggedIn') || null,
    username: localStorage.getItem('username') || '',
    password: localStorage.getItem('password') || '',
    user_pk: localStorage.getItem('user_pk') || null,
  }),
  actions: {
    async loginUser(username, password) {
        console.log('this method is toggled');
        try {

            const response = await axios.post(
                'http://127.0.0.1:8000/api/authentication/login/',
                {
                username: username,
                password: password
            }, 
            {
                headers: {
                  'Content-Type': 'application/json',
                }
            }
        );
        if (response.status === 200) {
            console.log('status 200');
            
            console.log(response);
            
            const {key} = response.data
            localStorage.setItem('authToken', key)
            this.authToken = key
            localStorage.setItem('isUserLoggedIn', true)
            this.isUserLoggedIn = true
            localStorage.setItem('username', username)
            this.username = username
            localStorage.setItem('password', password)
            this.password = password
            const res = await axios.get('http://127.0.0.1:8000/accounts/get_user_pk/', {
                params: {
                    username: this.username
                }
            });
            localStorage.setItem('user_pk', res.data)
            this.user_pk = res.data
        } else {
            console.log('request is not 200');
            
        }
        } catch (error) {
            console.log('an error occured');
            
        } 
        
    },
    logoutUser() {
        this.authToken = null;
        localStorage.removeItem('authToken'); 
        
        this.isUserLoggedIn = null;
        localStorage.removeItem('isUserLoggedIn');
        
        this.username = '';
        localStorage.removeItem('username');

        this.password = '';
        localStorage.removeItem('password');
    }
  },
});