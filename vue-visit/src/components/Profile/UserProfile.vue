<template>
    <div>
    <header-wrapper>
        <base-button 
        @click="changeComponent('user-info')"
        :mode="'profile'">You information</base-button>
        <base-button 
        @click="changeComponent('appointments-history')"
        :mode="'profile'">Appointments history</base-button>
    
    </header-wrapper>
        <profile-base-card>
            <div class="loading" v-if="isLoading">Loading ...</div>
            <user-info
            :userInfo="userInfo"
            v-if="CurrentComponent === 'user-info' && !isLoading" 
            ></user-info>
            <appointments-history
            :appointmentsHistory="appointmentsHistory"
            v-if="CurrentComponent === 'appointments-history' && !isLoading" 
            ></appointments-history>
           
        </profile-base-card>
    </div>
</template>

<script>
import axios from 'axios';
import HeaderWrapper from './headerWrapper.vue'
import ProfileBaseCard from './ProfileBaseCard.vue'
import UserInfo from './UserInfo.vue'
import AppointmentsHistory from './AppointmentsHistory.vue'



export default {
    components: {
        HeaderWrapper, 
        ProfileBaseCard,
        UserInfo,
        AppointmentsHistory,
      
    },  
    data() {
        return {
            userInfo: '',
            appointmentsHistory: '',
            
            CurrentComponent: 'user-info',

            isLoading: true
        }
    },
    mounted() {
        this.getUserIno()
    },
    methods: {
        async getUserIno() {
            const user_pk = localStorage.getItem('user_pk')
            let url = `/accounts/get_user_info/?user_pk=${user_pk}`
            const response = await axios.get(url,
                {
                params: {  
                    user_pk: user_pk  
                }
            } 
            )
            console.log(url);
            
            this.userInfo = response.data.user_info[0]
            localStorage.setItem('userInfo', this.userInfo)
            this.appointmentsHistory = response.data.appointments
            console.log(this.userInfo.username);
            console.log(this.appointmentsHistory);
            this.isLoading = false
            console.log('loading is finished');
            

            // console.log(this.userInfo.appointments[0].doctor.first_name);
            
        },
        changeComponent(cmp) {            
            this.CurrentComponent = cmp
        }
    },
  
}

</script>


<style scoped>

.loading {
   text-align: center;
   padding-top: 6rem;
}

</style>