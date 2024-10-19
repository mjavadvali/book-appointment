<template>
    <form @submit.prevent="login">

        <input v-model="username" type="text" placeholder="username" />
        <input v-model="password" type="password" placeholder="password" />
        <div style="    display: flex;
                        flex-direction: column-reverse;
                        align-items: center;
                        margin-top: 3rem;"> 
          <a href="">forgot your password?</a>
          <base-button>sign in</base-button>
        </div>
        
    </form>
     
</template>

<script>
import BaseAuthCard from '../UI/BaseAuthCard.vue';
import { userAuthStore } from '@/stores/auth';
import {ref, watch} from 'vue';
import { useRoute, useRouter } from 'vue-router'; 

export default {
    components: {
        BaseAuthCard
    },  
    setup() {
      const route = useRoute();
      const router = useRouter();

      const username = ref('');
      const password = ref('');

      const auth = userAuthStore();
      

      const login = () => {
        try {
          auth.loginUser(username.value, password.value);
          if (auth.authToken) {
            const nextUrl = route.query.next || '/doctors'; 
            router.push(nextUrl);
          }

        } catch (error) {
          console.error("Login failed:", error);
        }


        watch(() => auth.authToken, (newToken) => {
          if (newToken) {  
            const nextUrl = route.query.next || '/doctors'; 
            router.push(nextUrl);
          }
        }, { immediate: false });

      }
      return {
        username,
        password,
        auth,
        login
      }
    },
  
  
};
</script>


<style scoped>




/* body {
    background: rgb(203, 235, 220);
} */

form {display: flex;
  flex-direction: column;}


/* doctor review*/

.review {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 1.75rem;

}

.review form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 1.75rem;
}
.rating {
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    }
    
    
    .rating > input{ display:none;}
    
    .rating > label {
    position: relative;
    width: 1.1em;
    font-size: 5vw;
    color: #FFD700;
    cursor: pointer;
    }
    
    .rating > label::before{
    content: "\2605";
    position: absolute;
    opacity: 0;
    }
    
    .rating > label:hover:before,
    .rating > label:hover ~ label:before {
    opacity: 1 !important;
    }
    
    .rating > input:checked ~ label:before{
    opacity:1;
    }
    
    .rating:hover > input:checked ~ label:before{ opacity: 0.4; }
    
    
    
/* book-appointment */
.book-appointment form {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>