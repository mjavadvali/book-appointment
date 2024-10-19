<template>
  <div class="select-wrapper">
    <label for="referrer">Select a specialization</label>
    <select 
      name="specialization" 
      id="referrer"
      @change="handleSpecializationChange">
      <option value="all">All</option>
      <option v-for="speciality in specialtyChoices" :key="speciality" :value="speciality">
        {{ speciality }}
      </option>
    </select>
  </div>

  <div v-if="doctors.length > 0" class="docters-cards">
    <base-card v-for="doctor in doctors" :key="doctor.id">
      <template #header>

        <img :src="doctor.photo_ID" alt="">
        
      </template>
      <template #default>
        <h2>{{ doctor.first_name }} {{ doctor.last_name }}</h2>
        <p>{{ doctor.specialization }}</p>
      </template>

      <template #footer>
        <router-link :to="{ name: 'doctorDetail', params: { id: doctor.id } }">
          View details
        </router-link>
      </template>
    </base-card>
  </div>

  <div v-else class="no-doctor-message">
    <h1>Sorry, no doctors in this specialization</h1>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import BaseCard from '../UI/BaseCard.vue';
import { userAuthStore } from '@/stores/auth';

export default {
  components: {
    BaseCard,
  },
  setup() {
    const doctors = ref([]);
    const specialtyChoices = ref([]);
    const selectedSpecialty = ref('all');
    const route = useRoute();
    const router = useRouter();

    const fetchDoctors = async (speciality) => {
      try {
        let url = 'http://localhost:8000/doctors/';
        if (speciality !== 'all') {
          url += `${speciality}/`;
        }
        const response = await axios.get(url);
        doctors.value = response.data;
        console.log(doctors);
        
      } catch (error) {
        console.error('Failed to fetch doctors:', error);
      }
    };

    const getSpecialtyChoices = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/specialty_choices/');
        specialtyChoices.value = response.data;
      } catch (error) {
        console.error('Failed to fetch specialty choices:', error);
      }
    };

    const handleSpecializationChange = (event) => {
      selectedSpecialty.value = event.target.value;
      router.push({ query: { specialization: selectedSpecialty.value } });
      localStorage.setItem('selectedSpecialty', selectedSpecialty.value);
      fetchDoctors(selectedSpecialty.value);
    };

    onMounted(() => {
      const storedSpecialty = route.query.specialization || 'all';
      selectedSpecialty.value = storedSpecialty;
      fetchDoctors(storedSpecialty);
      getSpecialtyChoices();
    });

  

    return {
      doctors,
      specialtyChoices,
      selectedSpecialty,
      handleSpecializationChange,
    };
  },
};
</script>

<style scoped>
.select-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.docters-cards {
    display: grid;
    grid-template-columns: repeat(3, 21rem);
    gap: 1rem;
    justify-content: center;
    margin-block: 5rem;
    padding-bottom: 5rem;
}
.no-doctor-message {
  text-align: center;
  margin-top: 13rem;
}

img {
    width: 158px;
    height: 158px;
}

@media (max-width: 1036px) {
    .docters-cards {
      display: grid;
    grid-template-columns: repeat(2, 21rem);
    gap: 1rem;
    justify-content: center;
    margin-block: 5rem;
    padding-bottom: 5rem;
    }
}

@media (max-width: 740px) {
    .docters-cards {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
}
</style>
