<template>
    <div>
        <div class="oldInfo">
            <div class="new_email" v-if="newEmailInput">
                <label>Your new Email:</label>
                <input type="email" ref="newEmail">
                <label>Your password</label>
                <input type="password" ref="oldPassword">
                <base-button @click="changeEmail">Save</base-button>
                <span></span>
                <base-button @click="showEmail" :mode="'flat'">Cancel</base-button>
            </div>
            <div class="oldEmailWrapper" v-else>
                <label>Your email:</label>
                <input class="oldEmail" type="text" disabled :value="userInfo.email">
            </div>
            <button class="change" @click="showEmail">change</button>
        </div>
        
        <div class="oldInfo">
            <div class="new_password" v-if="newPasswordInput">
                <label>Your old password:</label>
                <input type="password" ref="oldPasswordPass">
                <label>Your new password:</label>
                <input type="password" ref="newPassword1">
                <label>Your new password again:</label>
                <input type="password" ref="newPassword2">
                <base-button @click="resetPassword">Save</base-button>
                <span></span>
                <base-button @click="showPassword" :mode="'flat'">Cancel</base-button>
            </div>
            <div class="oldPasswordWrapper" v-else>
                <label>Your password:</label>
                <input class="oldPassword" type="text" disabled value="xxxxxxxxxx">
            </div>
            <button class="change" @click="showPassword">change</button>
        </div>
        
        <div class="logout">
            <base-button :mode="'alert'" @click="logout">Logout</base-button>
        </div>
    </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { userAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

export default {
    props: ['userInfo'],
    
    setup() {
        
        const router = useRouter();
        const auth = userAuthStore();
    
        
        const newEmailInput = ref(false);
        const newPasswordInput = ref(false);
        
        const newEmail = ref('');
        const oldPassword = ref('');
        const oldPasswordPass = ref('');
        const newPassword1 = ref('');
        const newPassword2 = ref('');

        // Function to validate email
        const isValidEmail = (email) => {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        };

        const showEmail = () => {
            newEmailInput.value = !newEmailInput.value;
        };

        const showPassword = () => {
            newPasswordInput.value = !newPasswordInput.value;
        };

        const changeEmail = async () => {
            const enteredEmail = newEmail.value;
            const enteredPassword = oldPassword.value;

            if (enteredEmail.trim() === '' && enteredPassword.trim() === '') {
                console.log('Empty input');
            } else if (isValidEmail(enteredEmail)) {
                console.log('Valid email');
                if (enteredPassword === auth.password) {
                    if (enteredEmail !== props.userInfo.email) {
                        await sendNewEmail(enteredEmail);
                        newEmail.value = '';
                        oldPassword.value = '';
                    } else {
                        console.log('This is your current email');
                    }
                } else {
                    console.log('Invalid password');
                }
            } else {
                console.log('Invalid email');
            }
        };

        const sendNewEmail = async (newEmail) => {
            console.log(newEmail);
            const url = '/accounts/reset_email/';
            const token = auth.authToken;
            const data = {
                username: auth.username,
                newEmail: newEmail
            };
            const response = await axios.post(url, data, {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json',
                }
            });
            console.log(response);
        };

        

        const resetPassword = async () => {
            const enteredOldPassword = oldPasswordPass.value;
            const enteredNewPassword = newPassword1.value;
            const enteredNewPasswordRepeat = newPassword2.value;

            if (enteredOldPassword !== auth.password) {
                console.log('Password incorrect');
            } else if (enteredNewPassword !== enteredNewPasswordRepeat) {
                console.log('Your entered passwords do not match');
            } else {
                oldPasswordPass.value = '';
                newPassword1.value = '';
                newPassword2.value = '';
                await sendNewPassword(enteredNewPassword, enteredOldPassword);
            }
        };

        const sendNewPassword = async (newPassword, oldPassword) => {
            const url = '/api/authentication/password/change/';
            const token = auth.authToken;
            const data = {
                new_password1: newPassword,
                new_password2: oldPassword
            };
            const response = await axios.post(url, data, {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json',
                }
            });
            console.log(response.data);
        };
        const logout = () => {
            try {
                auth.logoutUser();
                router.push('/logout'); 
            } catch (error) {
                console.log(error);
                
            }
        };
        return {
            auth,
            newEmailInput,
            newPasswordInput,
            showEmail,
            showPassword,
            changeEmail,
            resetPassword,
            logout,
            newEmail,
            oldPassword,
            oldPasswordPass,
            newPassword1,
            newPassword2,
        };
    },
};
</script>

<style scoped>
.change {
    border-radius: 40px;
    background: azure;
    transition: transform 0.04s;
}
.change:hover {
    transform: scale(1.02);
    background: #b1e9b5;
}
.oldInfo {
    padding-top: 3rem;
    border: 1px solid;
    display: flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
    justify-content: space-around;
    padding-bottom: 2rem;
}
.logout {
    margin-top: 4rem;
    margin-left: 4rem;
}
span {
    display: inline-block;
    width: 1rem;
}
</style>
