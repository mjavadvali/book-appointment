<template>
    <div>
      <ProfileBaseCard>
        <div v-if="!route.query.visited" class="not-visited">
          <h3>
            You haven't visited the doctor.
            So you cannot review the appointment.
          </h3>
        </div>
        <div v-else>
          <form @submit.prevent="sendReviewForm">
            <div class="rating">
              <input type="radio" name="rating" v-model="score" value="5" id="5" /><label for="5">☆</label>
              <input type="radio" name="rating" v-model="score" value="4" id="4" /><label for="4">☆</label>
              <input type="radio" name="rating" v-model="score" value="3" id="3" /><label for="3">☆</label>
              <input type="radio" name="rating" v-model="score" value="2" id="2" /><label for="2">☆</label>
              <input type="radio" name="rating" v-model="score" value="1" id="1" /><label for="1">☆</label>
            </div>
            <label for="">Score</label>
            <div class="feedback">
              <label for="feedback" class="feedback-label">Your Feedback:</label>
              <textarea v-model="feedback" name="feedback" id="feedback" cols="30" rows="10"></textarea>
            </div>
            <base-button>Submit</base-button>
          </form>
        </div>
      </ProfileBaseCard>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import axios from 'axios';
  import ProfileBaseCard from '../Profile/ProfileBaseCard.vue';
  import { userAuthStore } from '@/stores/auth';

  export default {
    components: {
      ProfileBaseCard
    },
    setup() {
      const score = ref(null);
      const feedback = ref('');
      const route = useRoute();
      const router = useRouter();
      const auth = userAuthStore();
      const sendReviewForm = async () => {
        console.log('Score:', score.value);
        console.log('Feedback:', feedback.value);
        try {
          const url = 'http://127.0.0.1:8000/appointment/review/';
          const token = auth.authToken;
          console.log(token);
  
          const data = {
            appointment: parseInt(route.params.id, 10),
            rating: parseInt(score.value, 10),
            feedback: feedback.value,
          };
          console.log(data);
  
          const response = await axios.post(url, data, {
            headers: {
              'Authorization': `Token ${token}`,
              'Content-Type': 'application/json',
            },
          });
          console.log(response.data);
          router.push('/profile');
        } catch (error) {
          console.error('Error:', error, error.res ? error.res.data : error.message);
        }
      };
  
      return {
        score,
        feedback,
        sendReviewForm,
        route,
        auth
      };
    }
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  div {
    margin-top: 2rem;
    align-content: center;
    text-align: -webkit-center;
  }
  .rating {
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    align-items: center;
  }
  .rating > input {
    display: none;
  }
  .rating > label {
    position: relative;
    width: 1.1em;
    font-size: 3vw;
    color: #ffd700;
    cursor: pointer;
  }
  .rating > label::before {
    content: "\2605";
    position: absolute;
    opacity: 0;
  }
  .rating > label:hover:before,
  .rating > label:hover ~ label:before {
    opacity: 1 !important;
  }
  .rating > input:checked ~ label:before {
    opacity: 1;
  }
  .rating:hover > input:checked ~ label:before {
    opacity: 0.4;
  }
  .feedback {
    margin-top: 1rem;
    text-align: left;
  }
  .feedback-label {
    display: block;
    margin-bottom: 0.5rem;
  }
  .feedback textarea {
    margin: auto;
  }
  </style>
  