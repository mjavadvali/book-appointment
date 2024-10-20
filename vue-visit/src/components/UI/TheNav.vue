<template>
  <header>
      <h2>
          <router-link to="/doctors">
              Book Appointment
          </router-link>
      </h2>
      <div class="search">
        <form id="search-form" @submit.prevent="SearchDoctors" method="get">

          <input 
          v-model="q"
          id="search-input"
          type="text" 
          @input="SearchDoctors"
          placeholder="search for doctors ...">
          
        </form>

        <div class="search-result">
          <ul>
              <router-link
                v-for="doctor in searchResults"
                :key="doctor.pk"
                :to="{ name: 'doctorDetail', params: { id: doctor.pk } }"
                tag="li" 
              >
                {{ doctor.name }}
              </router-link>
          </ul>
        </div>
      </div>
      <button v-if="auth.isUserLoggedIn" @click="navigateToProfile">Profile</button>
      <button v-else @click="navigateToLogin()">Login</button>
  </header>
</template>

<script>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
import {userAuthStore} from '@/stores/auth';
import { useRouter, useRoute } from 'vue-router'; 
import axios from 'axios';
export default {
  setup() {
    const q = ref('');
    const searchResults = ref([]);
    const auth = userAuthStore();
    const isLoggedIn = ref(false);
    const router = useRouter(); 
    
      const navigateToLogin = () => {
        router.push('/user_auth');
      };
      
      const navigateToProfile = () => {
        console.log('profile is toggled');
        router.push('/profile');
      };
    
      const updateLoginStatus = () => {
        isLoggedIn.value = !!auth.isUserLoggedIn;
      };

      const SearchDoctors = async () => {
        try {
          
          const response = await axios.get('/api/search_view/', {
            params: {
              q: q.value  
              
            }
          });
          console.log(response);  
          searchResults.value = response.data
        } catch (error) {
          console.error("Failed to fetch doctor details:", error);
        }
      }

      const clearSearch = () => {
        q.value = '';       
        searchResults.value = []; 
      };

      onMounted(() => {
        console.log(auth.temp);
        isLoggedIn.value = auth.isUserLoggedIn === "true";
        window.addEventListener('storage', updateLoginStatus);
      });
      
      onBeforeUnmount(() => {
        window.removeEventListener('storage', updateLoginStatus);
      });

      router.beforeEach((to, from) => {
        clearSearch(); 
      });
      
      const route = useRoute();
      
      watch(route, (newValue, oldValue) => {
      
      });

      return {
        auth,
        isLoggedIn,
        navigateToLogin,
        navigateToProfile,
        q,
        SearchDoctors,
        searchResults,
        clearSearch,
        
      };
  },
};
</script>

<style scoped>
h1 {
  margin-left: 3rem;
  color: rgb(195, 214, 200);
}

h1.router-link {
  color: black;
}

h2 {
  margin-left: 2rem;
}
h2:hover {
  background: rgb(108, 230, 108);
}

header {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 5rem;
  background: rgb(108, 230, 108);
  position: relative;
  top: 0;
  margin: 0 auto;
}

button {
  width: 6rem;
  height: 2.5rem;
  border-radius: 15px;
  background: #99edb8;
  color: #000000;
  border: 1px #077825 solid;
  margin-right: 3rem;
  transition: transform 0.1s;
}
button:hover{
  transform: scale(1.05);
}


.search-result {
  position: absolute;
  top: 100%; 
  left: 0; 
  right: 0; 
  background-color: white;
  border: 1px solid #ccc; 
  border-radius: 4px; 
  max-height: 200px; 
  overflow-y: auto; 
  z-index: 1000; 
  /* padding-left: 11px; */
    width: 20rem;
    margin: auto;
    top: 57px;
    left: 100px;
}

.search-result ul {
  list-style-type: none; 
  margin: 0;
  padding: 0; 
  display: flex;
    flex-direction: column;
    gap: 10px;
  }

.search-result li {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.search-result li:hover {
  background-color: #f0f0f0;
}

.search-result li a {
  text-decoration: none; 
  color: inherit; 
}

.search-result a {
  width: 100%;
  color: rgb(6, 84, 6);
}



.search-result {
  position: absolute;
  top: 100%; /* Position it right below the input */
  left: 0; /* Align with the left of the input */
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 4px;
  max-height: 200px;
  overflow-y: auto;
  z-index: 1000;
  width: 100%; /* Set the width to match the input */
}

</style>
