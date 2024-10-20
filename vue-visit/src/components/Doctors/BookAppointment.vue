<template>
    <div>
      <div class="book-appointment">
        <form @submit.prevent="book">
          <div class="input-wrapper">
            <h3 style="margin-bottom: 2rem;">Book appointment</h3>
            <label for="">Doctor</label>
            <select v-if="!doctor" v-model="enteredDoctor" name="doctors">
              <option v-for="doctor in doctorsList" :key="doctor.id" :value="doctor">
                {{ doctor.first_name }} {{ doctor.last_name }}
              </option>
            </select>
            <input v-else type="text" v-model="enteredDoctorName" disabled />
          </div>
  
          <div class="input-wrapper">
            <label for="">Date</label>
            <input v-model="enteredDate" type="date" id="" name="" />
          </div>
  
          <div class="input-wrapper">
            <label for="">Time</label>
            <select v-model="enteredTime" name="timeslot" id="s">
              <option v-for="(timeslot, index) in availableTimeSlots" :key="index" :value="{ index: index, time: timeslot[1] }">
                {{ timeslot[1] }}
              </option>
            </select>
          </div>
  
          <base-button :disabled="showBookingDialog">Book</base-button>
        </form>
      </div>
  
      <teleport to="body">
        <base-dialog v-if="showBookingDialog">
          <template #header>
            <h3 
            style="
              margin-left: 1.5rem;
              margin-top: 11px;
              ">

              Book appointmnet alert
            </h3>
          
          </template>
          <template #default>
            <p>You have booked an appointment with Dr. {{ doctor.first_name }} {{ doctor.last_name }}
              on {{ enteredDate }} between {{ enteredTime.time  }}
            </p>
          </template>
          <template #button>
            <button class="confirm-button" @click="BookedAppointmentConfirm">
              Confirm
            </button>
          </template>
        
        </base-dialog>
      </teleport>

      <teleport to="body">
        <base-dialog v-if="showUnAuthenticatedDialog">
          <template #header>
            <h3 
            style="
              margin-left: 1.5rem;
              margin-top: 11px;
              ">

              Book appointmnet alert
            </h3>
          
          </template>
          
          <template #default>
            <p>You need to login before booking an appointment.
              <a href="/user_auth">click here to login</a>
            </p>
          </template>
          <template #button>
            <button class="confirm-button" @click="unAuthenticatedConfirm">
              OK
            </button>
          </template>
        
        </base-dialog>
      </teleport>
    </div>
  </template>
  
  <script>
  import { ref, watch, computed, onMounted } from 'vue';
  import axios from 'axios';
  import BaseDialog from '../UI/BaseDialog.vue';
  import { userAuthStore } from '@/stores/auth';

  
  export default {
    props: ['doctor'],
    components: {
      BaseDialog,
    },
    setup(props) {
      const enteredDoctor = ref('');
      const enteredDate = ref(null);
      const enteredTime = ref(null);
      const availableTimeSlots = ref([]);
      const showBookingDialog = ref(false);
      const showUnAuthenticatedDialog = ref(false)

      const doctorsList = ref([]);
      const doctorId = ref(null);
      

      const auth = userAuthStore();

      
     

      const fetchDoctors = async () => {
        if (!props.doctor) {
          try {
            const url = '/doctors/';
            const response = await axios.get(url);
            doctorsList.value = response.data;
          } catch (error) {
            console.error('Failed to fetch doctors:', error);
          }
        } else {
          doctorId.value = props.doctor.id;
        }
      };
  
      const getEmptyTimeSlots = async (date) => {
        try {
          const url = `/api/get_empty_time_slots/?doctor_id=${doctorId.value}&date=${date}`;
          const response = await axios.get(url);
          availableTimeSlots.value = response.data.available_slots;
        } catch (error) {
          console.error('Error fetching empty time slots:', error);
        }
      };
  
      const book = async () => {
        const url = '/appointment/booking/';

        if (enteredDate.value === null || enteredTime.value === null) {
          alert('Date and Time need to be filled')
        }
        else {
          if (!auth.authToken) {
            showUnAuthenticatedDialog.value = true
          } else {
            const data = {
              patient: parseInt(auth.user_pk, 10),
              doctor: doctorId.value,
              date: enteredDate.value,
              timeslot: enteredTime.value.index,
            };
            try {

              const res = await axios.post(url, data, {
                headers: {
                  Authorization: `Token ${auth.authToken}`,
                  'Content-Type': 'application/json',
                },
              });
            } catch (error) {
              console.log('error', error);
              
            }
            showBookingDialog.value = true;
          }

        }

      };
      const BookedAppointmentConfirm = () => {
        console.log('confirm is toggled');
        showBookingDialog.value = false
        window.location.reload();
      };
  
      const enteredDoctorName = computed(() => {
        if (props.doctor) {
          return `${props.doctor.first_name} ${props.doctor.last_name}`;
        }
        return `${enteredDoctor.value.first_name} ${enteredDoctor.value.last_name}`;
      });

      const unAuthenticatedConfirm = () => {
        showUnAuthenticatedDialog.value = false
      };
  
      watch(enteredDoctor, (newDoctor) => {
        if (newDoctor) {
          doctorId.value = newDoctor.id;
        }
      });
  
      watch(enteredDate, (newDate) => {
        if (enteredDoctorName.value && newDate) {
          getEmptyTimeSlots(newDate);
        }
      });
  
      onMounted(fetchDoctors);
  
      return {
        auth,
        enteredDoctor,
        enteredDate,
        enteredTime,
        availableTimeSlots,
        showBookingDialog,
        doctorsList,
        enteredDoctorName,
        book,
        BookedAppointmentConfirm,
        showUnAuthenticatedDialog,
        unAuthenticatedConfirm
      };
    },
  };
  </script>
  
  <style scoped>
  .book-appointment {
    margin: 2rem auto;
    width: 30rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center
  }
  
  .input-wrapper {
    margin-bottom: 1.5rem;
    width: 20rem;
  }
  
  input,
  select {
    width: 100%;
    padding: 0.5rem;
    margin-top: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .base-button {
    margin-top: 1rem;
  }

.confirm-button {
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
}

  </style>
  