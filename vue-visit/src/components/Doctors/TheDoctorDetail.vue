<template>
  <div>
    <div v-if="doctor" class="doctor-detail-wrapper">
      <div class="photo">
        <img :src="doctor.photo_ID" alt="" />
      </div>

      <h2>{{ doctor.first_name }} {{ doctor.last_name }}</h2>
      <h3>specialization: {{ doctor.specialization }}</h3>
      <div class="button">
        <base-button @click="toggleBookingShow">Book appointment</base-button>
      </div>
      <book-appointment
        v-if="showBookingInfo"
        :doctor="doctor"
      ></book-appointment>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import axios from "axios";
import BookAppointment from "./BookAppointment.vue";
import { userAuthStore } from "@/stores/auth";
export default {
  components: {
    BookAppointment,
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const doctor = ref(null);
    const showBookingInfo = ref(false);
    const auth = userAuthStore();
    const fetchDoctor = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/doctor/${props.id}/`
        );
        doctor.value = response.data;
      } catch (error) {
        console.error("Failed to fetch doctor details:", error);
      }
    };

    const toggleBookingShow = () => {
      showBookingInfo.value = !showBookingInfo.value;
    };

    onMounted(() => {
      fetchDoctor();

      const authToken = auth.authToken;
      const userPk = auth.user_pk;
  
    });

    watch(() => props.id, () => {
      fetchDoctor();
    });

    return {
      doctor,
      showBookingInfo,
      toggleBookingShow,
      auth,
    };
  },
};
</script>

<style scoped>
.doctor-detail-wrapper {
  padding-bottom: 3rem;
  margin: auto;
  width: 35rem;
  margin-top: 3rem;
  border: 1px solid;
  gap: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 27px;
  max-height: 55rem;
}

.button {
  margin-top: 1rem;
}

img {
  margin-top: 20px;
  width: 200px;
  height: 200px;
}
</style>
