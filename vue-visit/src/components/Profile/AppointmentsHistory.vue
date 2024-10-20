<template>
    <div>
        <div class="appointments">
        <h2>Booked Appointments</h2>
        <div v-for="appointment in appointmentsHistory"
         class="appointment-card" 
         :key="appointment.id">
            
            <h3>Dr. {{ appointment.doctor.first_name }} {{ appointment.doctor.last_name }}</h3>
            <p><strong>Date:</strong> {{ appointment.date }}</p>
            <p><strong>Time:</strong> {{ appointment.time }}</p>
            <p><strong>Visit Status:</strong> 
                <span :class="{'status-visited': appointment.visited, 'status-not-visited': !appointment.visited}">
                    {{ appointment.visited ? ' Visited' : ' Not Visited' }}
                </span>
            </p>
            <base-button @click.prevent="goToReview(appointment)"
            v-if="appointment.visited"
            >
            Review Appointment
            </base-button>    
            </div>
           
    </div>
    </div>
</template>



<script>
import { useRouter } from 'vue-router';
import axios from 'axios';
import BaseButton from '../UI/BaseButton.vue';
export default {
  components: { BaseButton },
    props: {
        appointmentsHistory: {
            type: Array,
            required: true
        }
    },
    setup(props) {
        const router = useRouter();
          
        const checkIfAppointmentIsReviewed = async (appointment) => {
            let url = '/api/check_app_reviewed/';
            try {
                const response = await axios.get(url, {
                    params: {
                        id: appointment.id
                    }
                });
                return response.data.is_reviewed;  
            } catch (error) {
                console.error("Error fetching review status:", error);
                return false; 
            }
        };

        const goToReview = async (appointment) => {
            if (!appointment.visited) {
                console.log('This appointment has not been visited.');
                return;
            }

            const isReviewed = await checkIfAppointmentIsReviewed(appointment);

            if (isReviewed === true) {
                console.log('This appointment has been reviewed.');
                alert('You have reviewed this appointment before.');
            } else {
                router.push({
                    name: 'reviewAppointment',
                    params: { id: appointment.id, date: appointment.date },
                    query: {
                        firstNameDoctor: appointment.doctor.first_name,
                        lastNameDoctor: appointment.doctor.last_name,
                        visited: appointment.visited
                    }
                });
            }
        };

        
    return {
        goToReview,
        checkIfAppointmentIsReviewed
    };
}}

</script>

<style scoped>

.appointments-container {
    padding: 20px;
    background-color: #f9f9f9;
    font-family: 'Arial', sans-serif;
}

.appointments h2 {
    margin-top: 15px;
    margin-right: 1rem;
    font-size: 1.8rem;
    color: #2c3e50;
    border-bottom: 2px solid #00aaff;
    padding-bottom: 10px;
}

.appointment-card {
    background-color: white;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(8, 111, 44, 0.688);
    transition: transform 0.2s ease;
}

.appointment-card:hover {
    transform: translateY(-5px);
}

.appointment-card h3 {
    font-size: 1.4rem;
    margin-bottom: 8px;
    color: #34495e;
}

.appointment-card p {
    font-size: 1rem;
    margin: 5px 0;
    color: #555;
}

.appointment-card strong {
    color: #2c3e50;
}

.status-visited {
    color: #27ae60;
    font-weight: bold;
}

.status-not-visited {
    color: #e74c3c;
    font-weight: bold;
}
h2 {
    margin-left: 1rem;
}

</style>