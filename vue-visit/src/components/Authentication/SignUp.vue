<template>
   
<form @submit.prevent="signup">

    <input v-model="username" type="text" placeholder="username" />
    <input v-model="email" type="text" placeholder="email" />
    
    <input v-model="password" type="password" placeholder="password" />
    <input v-model="password_repeat" type="password" placeholder="repeat password" />
    
    <div style="margin-top: 2rem;">
      <base-button>sign up</base-button>
    </div>
</form>

</template>


<script>
import axios from 'axios';
import BaseAuthCard from '../UI/BaseAuthCard.vue';
import { userAuthStore } from '@/stores/auth';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'; 
export default {
    components: {
        BaseAuthCard
    },  

    setup() {

      const route = useRoute();
      const router = useRouter();

      const username = ref('')
      const email = ref('')
      const password = ref('')
      const password_repeat = ref('')
      const errorMessage = ref('')
      const auth = userAuthStore();

      const signup = async () => {
      let url = 'http://127.0.0.1:8000/accounts/signup/';

      try {
        const response = await axios.post(
          url,
          {
            username: username.value,
            email: email.value,
            password: password.value,
            password_repeat: password_repeat.value,
          },
          {
            headers: {
              'Content-Type': 'application/json',
            }
          }
        );

        if (response.status === 200) {
          console.log('user created');
          
          await auth.loginUser(username.value, password.value);

          // Check if user is authenticated and token exists
          if (auth.authToken) {
            const nextUrl = route.query.next || '/doctors'; // Redirect to /doctors or the next URL
            router.push(nextUrl);
          }
        }
      } catch (error) {
        console.error('Failed to sign up:', error);
        if (error.response && error.response.data) {
          errorMessage.value = Object.values(error.response.data).flat().join(', ');
        } else {
          errorMessage.value = 'Failed to sign up. Please try again later.';
        }
      }
    };
      
      return {
        signup,
        username, 
        email, 
        password, 
        password_repeat, 

      }
    }
};
</script>


<style scoped>

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>>